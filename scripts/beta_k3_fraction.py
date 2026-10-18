"""Exact Fraction arithmetic for kappa3 Delta at fixed rational a."""

from __future__ import annotations

import itertools
from fractions import Fraction

import sympy as sp

from scripts.multicolour_constant import laws
from scripts.next_order_sparse import _matchings, sigma_and_cumulants


def to_frac(x) -> Fraction:
    r = sp.Rational(x)
    return Fraction(int(r.p), int(r.q))


def pack_frac(kappa, m, ell):
    cols, vals = [], []
    for t in itertools.product(range(m), repeat=ell):
        v = kappa[t]
        if v != 0:
            cols.append(t)
            vals.append(to_frac(v))
    return cols, vals


def ee_mixed_frac(S, packs, cov, leg_sizes):
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
    total = Fraction(0)
    for idxs_t in itertools.product(*[range(n) for n in nts]):
        base = Fraction(1)
        for r in range(R):
            base *= packs[r][1][idxs_t[r]]
        cols = []
        for r, (lo, hi) in enumerate(bounds):
            cols.extend(packs[r][0][idxs_t[r]])
        wsum = Fraction(0)
        for pairing in pairings:
            pt = Fraction(1)
            for ia, ib in pairing:
                ra, rb = leg_edge[ia], leg_edge[ib]
                pt *= cov[ra][rb] * S[cols[ia]][cols[ib]]
            wsum += pt
        total += base * wsum
    return total


def e_k4_frac(S, k4c, k4v, g0):
    pair4 = list(_matchings(4))
    total = Fraction(0)
    for idxs, val in zip(k4c, k4v):
        wsum = Fraction(0)
        for pairing in pair4:
            pt = Fraction(1)
            for ia, ib in pairing:
                pt *= g0 * S[idxs[ia]][idxs[ib]]
            wsum += pt
        total += val * wsum
    return total


def k3_coeff(sig, kappa, m) -> Fraction:
    Sm = sp.simplify(sig.inv())
    S = [[to_frac(Sm[i, j]) for j in range(m)] for i in range(m)]
    k3c, k3v = pack_frac(kappa, m, 3)
    k4c, k4v = pack_frac(kappa, m, 4)
    if not k3v or not k4v:
        return Fraction(0)
    g0, g = Fraction(2), Fraction(1)
    cov_star = [[g0 if i == j else g for j in range(3)] for i in range(3)]
    E334 = ee_mixed_frac(
        S, [(k3c, k3v), (k3c, k3v), (k4c, k4v)], cov_star, [3, 3, 4]
    )
    cov2 = [[g0, g], [g, g0]]
    E33 = ee_mixed_frac(S, [(k3c, k3v), (k3c, k3v)], cov2, [3, 3])
    E4 = e_k4_frac(S, k4c, k4v, g0)
    star = -(E334 - E33 * E4) / 31104

    cov_path = [[g0 if i == j else Fraction(0) for j in range(3)] for i in range(3)]
    cov_path[0][1] = cov_path[1][0] = g
    cov_path[1][2] = cov_path[2][1] = g
    E_mid = ee_mixed_frac(
        S, [(k3c, k3v), (k4c, k4v), (k3c, k3v)], cov_path, [3, 4, 3]
    )
    E_end = ee_mixed_frac(
        S, [(k4c, k4v), (k3c, k3v), (k3c, k3v)], cov_path, [4, 3, 3]
    )
    cov_dis = [[g0, Fraction(0)], [Fraction(0), g0]]
    E_xx_adj = ee_mixed_frac(S, [(k3c, k3v), (k3c, k3v)], cov2, [3, 3])
    E_xx_dis = ee_mixed_frac(S, [(k3c, k3v), (k3c, k3v)], cov_dis, [3, 3])
    path = -((E_mid - E_xx_dis * E4) + 2 * (E_end - E_xx_adj * E4)) / 10368
    return star + path


def main() -> None:
    lam = sp.Rational(1, 2)
    for N in [8, 10, 12]:
        a = sp.Rational(1, N)
        ds = []
        for states, probs in laws(a, lam):
            probs = [sp.nsimplify(p) for p in probs]
            states = [tuple(int(x) for x in s) for s in states]
            print(f"a=1/{N} m={len(states[0])}...", flush=True)
            sig, kappa = sigma_and_cumulants(states, probs, max_ell=4)
            m = len(states[0])
            ds.append(Fraction(0) if m == 1 else k3_coeff(sig, kappa, m))
        D = ds[2] + ds[0] - 2 * ds[1]
        aD = Fraction(1, N) * D
        print(f"a=1/{N} D={D} aD={aD}", flush=True)


if __name__ == "__main__":
    main()
