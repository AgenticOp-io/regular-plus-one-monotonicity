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

    # Product over pairing edges, sum over pairings (loop pairings; vectorize N)
    acc = np.zeros(N, dtype=np.float64)
    for p in range(n_pair):
        pt = np.ones(N, dtype=np.float64)
        for e in range(n_edge):
            pt *= cov_f[p, e] * S[idxs[:, ia[p, e]], idxs[:, ib[p, e]]]
        acc += pt
    return float(np.dot(base, acc))


def kappa4_star_path_num(S, kappa, m):
    cols, vals = _pack_k3(kappa, m)
    g0, g = 2.0, 1.0
    cov_star = np.full((4, 4), g)
    np.fill_diagonal(cov_star, g0)
    E4s = ee_k3_vec(S, cols, vals, cov_star)
    E2s = ee_k3_vec(S, cols, vals, np.array([[g0, g], [g, g0]]))
    kap_star = (E4s - 3.0 * E2s * E2s) / 1296.0
    star_reh = kap_star / 576.0

    cov_path = np.zeros((4, 4))
    np.fill_diagonal(cov_path, g0)
    for i in range(3):
        cov_path[i, i + 1] = cov_path[i + 1, i] = g
    E4p = ee_k3_vec(S, cols, vals, cov_path)

    def e2(c01):
        return ee_k3_vec(S, cols, vals, np.array([[g0, c01], [c01, g0]]))

    E01, E23 = e2(g), e2(g)
    E02, E03, E13 = e2(0.0), e2(0.0), e2(0.0)
    E12 = e2(g)
    kap_path = (E4p - E01 * E23 - E02 * E13 - E03 * E12) / 1296.0
    path_reh = kap_path / 48.0
    return star_reh + path_reh, star_reh, path_reh


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
            dk4 = star = path = 0.0
        else:
            dk4, star, path = kappa4_star_path_num(S, kappa, m)
        rows.append(
            dict(d6=d6, dw=dw, dk4=dk4, star=star, path=path, total=d6 + dw + dk4)
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
                f"star={r['star']:.5f} path={r['path']:.5f}",
                flush=True,
            )


if __name__ == "__main__":
    main()
