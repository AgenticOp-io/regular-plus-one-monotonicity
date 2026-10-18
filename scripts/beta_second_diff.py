"""Fast Delta-beta: Phi6 + VarW/2 + kappa4(X)/24 (star+path), vectorized Wick."""

from __future__ import annotations

import itertools
from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.multicolour_constant import laws
from scripts.next_order_sparse import (
    _matchings,
    phi6_coeff,
    sigma_and_cumulants,
    var_w_coeff,
)


def _pack_k3(kappa, m):
    ts, vals = [], []
    for t in itertools.product(range(m), repeat=3):
        v = float(kappa[t])
        if abs(v) > 1e-18:
            ts.append(t)
            vals.append(v)
    return np.asarray(ts, dtype=np.intp), np.asarray(vals, dtype=np.float64)


def ee_k3_vec(S, cols, vals, cov):
    """Vectorized E[prod_r k3(u_r)] over all nonzero k3 multi-indices."""
    R = cov.shape[0]
    nt = len(vals)
    n_edge = (3 * R) // 2
    pairings = list(_matchings(3 * R))
    n_pair = len(pairings)
    pairs = np.asarray(pairings, dtype=np.intp).reshape(n_pair, n_edge, 2)

    # All config index tuples: (N, R)
    grids = np.array(list(itertools.product(range(nt), repeat=R)), dtype=np.intp)
    N = grids.shape[0]
    base = np.prod(vals[grids], axis=1)  # (N,)

    # idxs[n, leg] colour
    idxs = cols[grids].reshape(N, 3 * R)  # (N, 3R)

    # For each pairing edge e, ra=ia//3
    ia = pairs[:, :, 0]  # (n_pair, n_edge)
    ib = pairs[:, :, 1]
    ra, rb = ia // 3, ib // 3
    cov_f = cov[ra, rb]  # (n_pair, n_edge)
    cov_w = np.prod(cov_f, axis=1)
    keep = np.abs(cov_w) > 1e-18
    if not np.any(keep):
        return 0.0
    ia = ia[keep]
    ib = ib[keep]
    cov_w = cov_w[keep]
    n_keep = cov_w.shape[0]

    # Chunk pairings; vectorize over configs (N). Pruning helps path/fork.
    acc = np.zeros(N, dtype=np.float64)
    chunk = 16 if N > 100_000 else 64
    for p0 in range(0, n_keep, chunk):
        p1 = min(p0 + chunk, n_keep)
        pt = np.broadcast_to(cov_w[p0:p1, None], (p1 - p0, N)).copy()
        for e in range(n_edge):
            ia_e = ia[p0:p1, e]
            ib_e = ib[p0:p1, e]
            # idxs[:, ia_e] -> (N, pc); transpose to (pc, N)
            pt *= S[idxs[:, ia_e].T, idxs[:, ib_e].T]
        acc += pt.sum(axis=0)
    return float(np.dot(base, acc))


def _kappa4_from_cov(S, cols, vals, cov, n5_over_n5):
    """kappa_4(f1..f4)/24 coeff of 1/n for one diagram type.

    n5_over_n5 = (#configs)/n^5, using scale-free cov (g0=2,g=1) so that
    (#configs)*(1/n)^6 * kappa_f = (n5_over_n5) * kappa_f / n.
    Then divide by 24: reh = n5_over_n5 * kappa_f / 24.
    """
    g0 = float(cov[0, 0])

    def e2(i, j):
        return ee_k3_vec(
            S, cols, vals, np.array([[g0, cov[i, j]], [cov[i, j], g0]])
        )

    E4 = ee_k3_vec(S, cols, vals, cov)
    # disconnected pairings of four mean-zero vars
    disc = e2(0, 1) * e2(2, 3) + e2(0, 2) * e2(1, 3) + e2(0, 3) * e2(1, 2)
    kap_f = (E4 - disc) / 1296.0
    return n5_over_n5 * kap_f / 24.0


def kappa4_star_path_num(S, kappa, m):
    """Star + path + fork (branched tree) 4-edge diagrams for kappa_4(X)/24."""
    cols, vals = _pack_k3(kappa, m)
    g0, g = 2.0, 1.0

    # Star K_{1,4}: # = n*C(n-1,4) / n^5 → 1/24
    cov_star = np.full((4, 4), g)
    np.fill_diagonal(cov_star, g0)
    star_reh = _kappa4_from_cov(S, cols, vals, cov_star, 1.0 / 24.0)

    # Path of 4 edges (5 verts): # ≈ n^5/2
    cov_path = np.zeros((4, 4))
    np.fill_diagonal(cov_path, g0)
    for i in range(3):
        cov_path[i, i + 1] = cov_path[i + 1, i] = g
    path_reh = _kappa4_from_cov(S, cols, vals, cov_path, 0.5)

    # Fork: hub edges 0,1,2; edge 3 attached to 2's far end.
    # # ≈ n * C(n-1,3) * 3 * (n-4) / n^5 → 1/2
    # (choose hub, 3 neighbours, which arm extends, extension vertex)
    cov_fork = np.zeros((4, 4))
    np.fill_diagonal(cov_fork, g0)
    for i, j in [(0, 1), (0, 2), (1, 2), (2, 3)]:
        cov_fork[i, j] = cov_fork[j, i] = g
    fork_reh = _kappa4_from_cov(S, cols, vals, cov_fork, 0.5)

    total = star_reh + path_reh + fork_reh
    return total, star_reh, path_reh, fork_reh


def pieces_num(a_val, lam_val=0.5):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    rows = []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=6)
        m = len(states[0])
        d6 = float(phi6_coeff(sig, kappa, m))
        dw = float(var_w_coeff(sig, kappa, m))
        S = np.array([[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)])
        if m == 1:
            dk4 = star = path = fork = 0.0
        else:
            dk4, star, path, fork = kappa4_star_path_num(S, kappa, m)
        rows.append(
            dict(
                d6=d6,
                dw=dw,
                dk4=dk4,
                star=star,
                path=path,
                fork=fork,
                total=d6 + dw + dk4,
            )
        )
    D = rows[2]["total"] + rows[0]["total"] - 2 * rows[1]["total"]
    return D, rows


def main():
    print("a | D | D*a", flush=True)
    for an in [
        Fraction(1, 5),
        Fraction(1, 6),
        Fraction(1, 8),
        Fraction(1, 10),
        Fraction(1, 12),
        Fraction(1, 15),
        Fraction(1, 20),
    ]:
        D, rows = pieces_num(an)
        print(f"a={an} D={D:.8f} D*a={D * float(an):.8f}", flush=True)
        for i, r in enumerate(rows):
            print(
                f"  m{i+1}: d6={r['d6']:.5f} dw={r['dw']:.5f} dk4={r['dk4']:.5f} "
                f"star={r['star']:.5f} path={r['path']:.5f} fork={r['fork']:.5f}",
                flush=True,
            )


if __name__ == "__main__":
    main()
