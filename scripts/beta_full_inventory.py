"""Inventory of 1/n packages in Delta Re h beyond Phi6 + VarW/2.

Packages (leading share/equal gamma, coeff of 1/n in Re h):
  P64  = E[Phi6] + (1/2) Var(W)     [exact series known]
  K4   = kappa_4(X)/24              [star+path]
  C35  = -Cov(X, Im Phi5)           [from kappa2(Im Phi)/2]
  K3XW = -kappa_3(X,X,W)/6          [star 3-edge; vectorized Wick]

Reports D = d3+d1-2d2 and D*a on a grid.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_second_diff import ee_k3_vec, kappa4_star_path_num, _pack_k3
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import (
    phi6_coeff,
    sigma_and_cumulants,
    var_w_coeff,
    _matchings,
)


def _pack_kl(kappa, m, ell):
    ts, vals = [], []
    for t in itertools.product(range(m), repeat=ell):
        v = float(kappa[t])
        if abs(v) > 1e-18:
            ts.append(t)
            vals.append(v)
    return np.asarray(ts, dtype=np.intp), np.asarray(vals, dtype=np.float64)


def _edge_of_leg(leg_bounds, ia):
    """Map leg index -> edge id given cumulative leg counts."""
    for e, (lo, hi) in enumerate(leg_bounds):
        if lo <= ia < hi:
            return e
    raise ValueError(ia)


def ee_mixed_vec(S, packs, cov, leg_sizes):
    """Gaussian E[prod_r f_r(u_r)] with f_r = sum kappa[t] prod u_{t_j}.

    packs: list of (cols, vals) for each factor
    leg_sizes: legs per factor (e.g. [3,5] or [3,3,4])
    cov: (R,R) edge covariance scale (g0/g)
    """
    R = len(packs)
    assert R == len(leg_sizes) == cov.shape[0]
    n_legs = sum(leg_sizes)
    n_edge = n_legs // 2
    pairings = list(_matchings(n_legs))
    n_pair = len(pairings)
    pairs = np.asarray(pairings, dtype=np.intp).reshape(n_pair, n_edge, 2)

    # cumulative leg bounds
    bounds = []
    cur = 0
    for s in leg_sizes:
        bounds.append((cur, cur + s))
        cur += s

    # map each leg -> edge
    leg_edge = np.empty(n_legs, dtype=np.intp)
    for e, (lo, hi) in enumerate(bounds):
        leg_edge[lo:hi] = e

    ia = pairs[:, :, 0]
    ib = pairs[:, :, 1]
    ra = leg_edge[ia]
    rb = leg_edge[ib]
    cov_f = cov[ra, rb]  # (n_pair, n_edge)

    # cartesian product of nonzero multi-indices
    nts = [len(p[1]) for p in packs]
    grids = np.array(list(itertools.product(*[range(n) for n in nts])), dtype=np.intp)
    if grids.size == 0:
        return 0.0
    N = grids.shape[0]
    base = np.ones(N, dtype=np.float64)
    for r in range(R):
        base *= packs[r][1][grids[:, r]]

    # idxs[n, leg] colour
    idxs = np.empty((N, n_legs), dtype=np.intp)
    for r, (lo, hi) in enumerate(bounds):
        idxs[:, lo:hi] = packs[r][0][grids[:, r]]

    acc = np.zeros(N, dtype=np.float64)
    for p in range(n_pair):
        pt = np.ones(N, dtype=np.float64)
        for e in range(n_edge):
            pt *= cov_f[p, e] * S[idxs[:, ia[p, e]], idxs[:, ib[p, e]]]
        acc += pt
    return float(np.dot(base, acc))


def cov_x_phi5_coeff(S, kappa, m):
    """Coeff of 1/n in -Cov(X, Im Phi5). See prior docstring for combinatorics."""
    k3c, k3v = _pack_k3(kappa, m)
    k5c, k5v = _pack_kl(kappa, m, 5)
    if len(k5v) == 0 or len(k3v) == 0:
        return 0.0
    cov_sh = np.array([[2.0, 1.0], [1.0, 2.0]])
    C = ee_mixed_vec(S, [(k3c, k3v), (k5c, k5v)], cov_sh, [3, 5])
    return C / 1440.0


def kappa3_xxw_star(S, kappa, m):
    """Coeff of 1/n in -kappa_3(X,X,W)/6 from star 3-edge config (vectorized)."""
    k3c, k3v = _pack_k3(kappa, m)
    k4c, k4v = _pack_kl(kappa, m, 4)
    if len(k3v) == 0 or len(k4v) == 0:
        return 0.0
    g0, g = 2.0, 1.0
    cov3 = np.full((3, 3), g)
    np.fill_diagonal(cov3, g0)

    E334 = ee_mixed_vec(
        S, [(k3c, k3v), (k3c, k3v), (k4c, k4v)], cov3, [3, 3, 4]
    )
    cov2 = np.array([[g0, g], [g, g0]])
    E33 = ee_k3_vec(S, k3c, k3v, cov2)

    # E[k4(u)] with Cov = g0 S
    E4 = 0.0
    pair4 = list(_matchings(4))
    p4 = np.asarray(pair4, dtype=np.intp).reshape(len(pair4), 2, 2)
    for k in range(len(k4v)):
        idxs = k4c[k]
        wsum = 0.0
        for p in range(len(pair4)):
            pt = 1.0
            for e in range(2):
                ia, ib = int(p4[p, e, 0]), int(p4[p, e, 1])
                pt *= g0 * S[idxs[ia], idxs[ib]]
            wsum += pt
        E4 += k4v[k] * wsum

    E_conn = E334 - E33 * E4
    # -kappa_3/6: see prior docstring → -E_conn/(31104 n)
    return -E_conn / 31104.0


def var_phi5_coeff(S, kappa, m):
    """Coeff of 1/n in - (1/2) Var(Im Phi5) from adjacent pairs.

    Im Phi5 = sum (1/120) k5; Var ~ (#adj) * (1/120)^2 * C_share / n^5
    because 10 legs → 5 covs. #adj ~ n^3/2 → n^3/n^5 = 1/n^2, DROPS.

    Equal-edge: #eq ~ n^2, (2/n)^5 → n^2/n^5 = 1/n^3, drops.

    So leading Var(Phi5) is O(1/n^2). Return 0 at this order.
    """
    return 0.0


def inventory(a_val, lam_val=0.5):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    rows = []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=6)
        m = len(states[0])
        S = np.array([[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)])
        p64 = float(phi6_coeff(sig, kappa, m) + var_w_coeff(sig, kappa, m))
        if m == 1:
            k4 = c35 = k3xw = 0.0
        else:
            k4, _, _ = kappa4_star_path_num(S, kappa, m)
            c35 = cov_x_phi5_coeff(S, kappa, m)
            k3xw = kappa3_xxw_star(S, kappa, m)
        total = p64 + k4 + c35 + k3xw
        rows.append(dict(p64=p64, k4=k4, c35=c35, k3xw=k3xw, total=total))

    def Delta(key):
        return rows[2][key] + rows[0][key] - 2 * rows[1][key]

    return {k: Delta(k) for k in rows[0]}, rows


def main():
    print("a | D_total | D*a | D_p64 | D_k4 | D_c35 | D_k3xw", flush=True)
    for an in [Fraction(1, 5), Fraction(1, 8), Fraction(1, 10), Fraction(1, 12)]:
        Ds, rows = inventory(an)
        print(
            f"a={an} D={Ds['total']:.6f} D*a={Ds['total']*float(an):.6f} "
            f"p64={Ds['p64']:.6f} k4={Ds['k4']:.6f} "
            f"c35={Ds['c35']:.6f} k3xw={Ds['k3xw']:.6f}",
            flush=True,
        )
        for i, r in enumerate(rows):
            print(
                f"  m{i+1}: p64={r['p64']:.5f} k4={r['k4']:.5f} "
                f"c35={r['c35']:.5f} k3xw={r['k3xw']:.5f}",
                flush=True,
            )


if __name__ == "__main__":
    main()
