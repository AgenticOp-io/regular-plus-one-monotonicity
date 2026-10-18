"""Exact Delta for kappa4(X)/24 star+path+fork at lambda=1/2.

Uses cleared-denominator integer Wick sums (exact).
"""

from __future__ import annotations

import itertools
from fractions import Fraction
from math import lcm

import sympy as sp

from scripts.multicolour_constant import laws
from scripts.next_order_sparse import _matchings, sigma_and_cumulants


def to_frac(x) -> Fraction:
    r = sp.Rational(x)
    return Fraction(int(r.p), int(r.q))


def pack_k3(kappa, m):
    cols, vals = [], []
    for t in itertools.product(range(m), repeat=3):
        v = kappa[t]
        if v != 0:
            cols.append(t)
            vals.append(to_frac(v))
    return cols, vals


def ee_k3_int(S_num, S_den, cols, vals_num, vals_den, cov_num, cov_den) -> Fraction:
    """Exact E[prod k3] via integer numerators; S = S_num/S_den, etc."""
    R = len(cov_num)
    n_legs = 3 * R
    pairings = list(_matchings(n_legs))
    # flatten pairings
    n_pair = len(pairings)
    n_edge = n_legs // 2
    ia = [[p[e][0] for e in range(n_edge)] for p in pairings]
    ib = [[p[e][1] for e in range(n_edge)] for p in pairings]
    ra = [[x // 3 for x in row] for row in ia]
    rb = [[x // 3 for x in row] for row in ib]

    nt = len(vals_num)
    # common value denominator V = lcm(vals_den)
    V = 1
    for d in vals_den:
        V = lcm(V, d)
    v_scaled = [vals_num[i] * (V // vals_den[i]) for i in range(nt)]

    # S common den
    SD = 1
    for row in S_den:
        for d in row:
            SD = lcm(SD, d)
    S_sc = [[S_num[i][j] * (SD // S_den[i][j]) for j in range(len(S_num))] for i in range(len(S_num))]

    # cov common den
    CD = 1
    for row in cov_den:
        for d in row:
            CD = lcm(CD, d)
    C_sc = [[cov_num[i][j] * (CD // cov_den[i][j]) for j in range(R)] for i in range(R)]

    # Each pairing edge contributes C_sc/CD * S_sc/SD
    # n_edge such edges; base has R factors of v_scaled/V
    # total = sum base * wsum, with den V^R * (CD*SD)^{n_edge}
    num_acc = 0
    den_global = (V**R) * ((CD * SD) ** n_edge)

    for idxs_t in itertools.product(range(nt), repeat=R):
        base = 1
        for r in range(R):
            base *= v_scaled[idxs_t[r]]
        colour = []
        for r in range(R):
            colour.extend(cols[idxs_t[r]])
        wsum = 0
        for p in range(n_pair):
            pt = 1
            for e in range(n_edge):
                pt *= C_sc[ra[p][e]][rb[p][e]] * S_sc[colour[ia[p][e]]][colour[ib[p][e]]]
            wsum += pt
        num_acc += base * wsum

    return Fraction(num_acc, den_global)


def frac_mat(S_frac):
    n = len(S_frac)
    return (
        [[S_frac[i][j].numerator for j in range(n)] for i in range(n)],
        [[S_frac[i][j].denominator for j in range(n)] for i in range(n)],
    )


def kappa4_trees(sig, kappa, m) -> Fraction:
    Sm = sp.simplify(sig.inv())
    S_frac = [[to_frac(Sm[i, j]) for j in range(m)] for i in range(m)]
    S_num, S_den = frac_mat(S_frac)
    cols, vals = pack_k3(kappa, m)
    if not vals:
        return Fraction(0)
    vals_num = [v.numerator for v in vals]
    vals_den = [v.denominator for v in vals]
    g0, g = Fraction(2), Fraction(1)

    def cov_mats(cov_frac):
        return frac_mat(cov_frac)

    def e2(c01: Fraction) -> Fraction:
        cov = [[g0, c01], [c01, g0]]
        cn, cd = cov_mats(cov)
        return ee_k3_int(S_num, S_den, cols, vals_num, vals_den, cn, cd)

    def from_cov(cov_frac, n5_weight: Fraction) -> Fraction:
        cn, cd = cov_mats(cov_frac)
        E4 = ee_k3_int(S_num, S_den, cols, vals_num, vals_den, cn, cd)
        disc = (
            e2(cov_frac[0][1]) * e2(cov_frac[2][3])
            + e2(cov_frac[0][2]) * e2(cov_frac[1][3])
            + e2(cov_frac[0][3]) * e2(cov_frac[1][2])
        )
        kap_f = (E4 - disc) / 1296
        return n5_weight * kap_f / 24

    cov_star = [[g0 if i == j else g for j in range(4)] for i in range(4)]
    star = from_cov(cov_star, Fraction(1, 24))
    print(f"    star done", flush=True)

    cov_path = [[g0 if i == j else Fraction(0) for j in range(4)] for i in range(4)]
    for i in range(3):
        cov_path[i][i + 1] = cov_path[i + 1][i] = g
    path = from_cov(cov_path, Fraction(1, 2))
    print(f"    path done", flush=True)

    cov_fork = [[g0 if i == j else Fraction(0) for j in range(4)] for i in range(4)]
    for i, j in [(0, 1), (0, 2), (1, 2), (2, 3)]:
        cov_fork[i][j] = cov_fork[j][i] = g
    fork = from_cov(cov_fork, Fraction(1, 2))
    print(f"    fork done", flush=True)

    return star + path + fork


def main() -> None:
    lam = sp.Rational(1, 2)
    a_sym = sp.Symbol("a")
    target = (-1022 * a_sym**2 + 511 * a_sym - 72) / (192 * (2 * a_sym - 1))
    print("exact kappa4 trees Delta", flush=True)
    for N in [8, 10, 12]:
        a = sp.Rational(1, N)
        ds = []
        for states, probs in laws(a, lam):
            probs = [sp.nsimplify(p) for p in probs]
            states = [tuple(int(x) for x in s) for s in states]
            m = len(states[0])
            print(f"a=1/{N} m={m} nonzero...", flush=True)
            if m == 1:
                ds.append(Fraction(0))
                continue
            sig, kappa = sigma_and_cumulants(states, probs, max_ell=3)
            ds.append(kappa4_trees(sig, kappa, m))
        D = ds[2] + ds[0] - 2 * ds[1]
        aD = Fraction(1, N) * D
        pred = to_frac(sp.simplify(target.subs(a_sym, a)))
        print(f"a=1/{N} D={D} aD={aD} pred={pred} match={aD == pred}", flush=True)


if __name__ == "__main__":
    main()
