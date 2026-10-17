"""Exact rational Delta for kappa3(X,X,W) star+path at lambda=1/2."""

from __future__ import annotations

import itertools
from fractions import Fraction

import sympy as sp

from scripts.multicolour_constant import laws
from scripts.next_order_sparse import _matchings, sigma_and_cumulants


def _pack(kappa, m, ell):
    cols, vals = [], []
    for t in itertools.product(range(m), repeat=ell):
        v = kappa[t]
        if v != 0:
            cols.append(t)
            vals.append(sp.simplify(v))
    return cols, vals


def ee_mixed_exact(S, packs, cov, leg_sizes):
    """Exact E[prod f_r] with Fraction/sympy arithmetic."""
    R = len(packs)
    n_legs = sum(leg_sizes)
    pairings = list(_matchings(n_legs))
    bounds = []
    cur = 0
    for s in leg_sizes:
        bounds.append((cur, cur + s))
        cur += s
    leg_edge = [0] * n_legs
    for e, (lo, hi) in enumerate(bounds):
        for i in range(lo, hi):
            leg_edge[i] = e

    nts = [len(p[1]) for p in packs]
    total = sp.Integer(0)
    for idxs_t in itertools.product(*[range(n) for n in nts]):
        base = sp.Integer(1)
        for r in range(R):
            base *= packs[r][1][idxs_t[r]]
        # colour indices per leg
        cols = []
        for r, (lo, hi) in enumerate(bounds):
            cols.extend(packs[r][0][idxs_t[r]])
        wsum = sp.Integer(0)
        for pairing in pairings:
            pt = sp.Integer(1)
            for ia, ib in pairing:
                ra, rb = leg_edge[ia], leg_edge[ib]
                pt *= cov[ra][rb] * S[cols[ia], cols[ib]]
            wsum += pt
        total += base * wsum
    return sp.simplify(total)


def e_k4_exact(S, k4c, k4v, g0):
    pair4 = list(_matchings(4))
    total = sp.Integer(0)
    for idxs, val in zip(k4c, k4v):
        wsum = sp.Integer(0)
        for pairing in pair4:
            pt = sp.Integer(1)
            for ia, ib in pairing:
                pt *= g0 * S[idxs[ia], idxs[ib]]
            wsum += pt
        total += val * wsum
    return sp.simplify(total)


def ee_k3_exact(S, k3c, k3v, cov):
    return ee_mixed_exact(S, [(k3c, k3v)], cov, [3])


def k3_star_path_exact(sig, kappa, m):
    S = sp.simplify(sig.inv())
    k3c, k3v = _pack(kappa, m, 3)
    k4c, k4v = _pack(kappa, m, 4)
    if not k3v or not k4v:
        return sp.Integer(0)
    g0, g = sp.Integer(2), sp.Integer(1)

    # star
    cov_star = [[g0 if i == j else g for j in range(3)] for i in range(3)]
    E334 = ee_mixed_exact(
        S, [(k3c, k3v), (k3c, k3v), (k4c, k4v)], cov_star, [3, 3, 4]
    )
    cov2 = [[g0, g], [g, g0]]
    E33 = ee_mixed_exact(S, [(k3c, k3v), (k3c, k3v)], cov2, [3, 3])
    E4 = e_k4_exact(S, k4c, k4v, g0)
    star = -(E334 - E33 * E4) / 31104

    # path
    cov_path = [[g0 if i == j else 0 for j in range(3)] for i in range(3)]
    cov_path[0][1] = cov_path[1][0] = g
    cov_path[1][2] = cov_path[2][1] = g
    E_mid = ee_mixed_exact(
        S, [(k3c, k3v), (k4c, k4v), (k3c, k3v)], cov_path, [3, 4, 3]
    )
    E_end = ee_mixed_exact(
        S, [(k4c, k4v), (k3c, k3v), (k3c, k3v)], cov_path, [4, 3, 3]
    )
    cov_dis = [[g0, 0], [0, g0]]
    E_xx_adj = ee_mixed_exact(S, [(k3c, k3v), (k3c, k3v)], cov2, [3, 3])
    E_xx_dis = ee_mixed_exact(S, [(k3c, k3v), (k3c, k3v)], cov_dis, [3, 3])
    kap_mid = E_mid - E_xx_dis * E4
    kap_end = E_end - E_xx_adj * E4
    path = -(kap_mid + 2 * kap_end) / 10368

    return sp.simplify(star + path)


def main() -> None:
    lam = sp.Rational(1, 2)
    print("exact kappa3 star+path Delta", flush=True)
    pts = []
    for N in [8, 10, 12]:
        a = sp.Rational(1, N)
        ds = []
        for states, probs in laws(a, lam):
            probs = [sp.nsimplify(p) for p in probs]
            states = [tuple(int(x) for x in s) for s in states]
            sig, kappa = sigma_and_cumulants(states, probs, max_ell=4)
            m = len(states[0])
            if m == 1:
                ds.append(sp.Integer(0))
            else:
                print(f"  a={a} m={m}...", flush=True)
                ds.append(k3_star_path_exact(sig, kappa, m))
        D = sp.simplify(ds[2] + ds[0] - 2 * ds[1])
        print(f"a={a} D={D} aD={sp.simplify(a*D)}", flush=True)
        pts.append((a, sp.simplify(a * D)))

    # If three points of aD = b0 + b1 a + b2 a^2, solve
    A = sp.Matrix([[1, a, a**2] for a, _ in pts])
    b = A.solve(sp.Matrix([y for _, y in pts]))
    print(f"quadratic fit b0,b1,b2 = {b[0]}, {b[1]}, {b[2]}", flush=True)


if __name__ == "__main__":
    main()
