"""Leading sparse second-difference pieces for multi-colour LLT.

Computes the coefficient of 1/n in E[Phi_6] and (1/2)Var(W) from the pair
laws, then D_partial = d3 + d1 - 2 d2.
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import sympy as sp

from scripts.multicolour_constant import laws


def _matchings(n: int):
    if n == 0:
        yield []
        return
    if n % 2:
        return

    def rec(remaining):
        if not remaining:
            yield []
            return
        a = remaining[0]
        for i in range(1, len(remaining)):
            b = remaining[i]
            rest = remaining[1:i] + remaining[i + 1 :]
            for m in rec(rest):
                yield [(a, b)] + m

    yield from rec(list(range(n)))


def wick_ee(idxs, V):
    k = len(idxs)
    if k % 2:
        return 0
    total = 0
    for pairing in _matchings(k):
        term = 1
        for i, j in pairing:
            term *= V[idxs[i], idxs[j]]
        total += term
    return total


def _set_partitions(n):
    def rec(remaining):
        if not remaining:
            yield []
            return
        first = remaining[0]
        for k in range(len(remaining)):
            for block_tail in itertools.combinations(remaining[1:], k):
                block = (first,) + block_tail
                leftover = [x for x in remaining[1:] if x not in block_tail]
                for part in rec(leftover):
                    yield [block] + part

    seen = set()
    for part in rec(list(range(n))):
        key = tuple(sorted(tuple(sorted(b)) for b in part))
        if key not in seen:
            seen.add(key)
            yield [list(b) for b in key]


def sigma_and_cumulants(states, probs, max_ell=6):
    m = len(states[0])
    R = range(m)
    mean = [sum(p * s[i] for s, p in zip(states, probs)) for i in range(m)]
    cen = [[s[i] - mean[i] for i in range(m)] for s in states]

    def mom(idxs):
        return sum(p * sp.Mul(*[c[i] for i in idxs]) for c, p in zip(cen, probs))

    kappa = {}
    for ell in range(2, max_ell + 1):
        for t in itertools.product(R, repeat=ell):
            # joint cumulant from centered moments
            total = 0
            for part in _set_partitions(ell):
                # skip partitions with singletons (centered => mom=0)
                if any(len(b) == 1 for b in part):
                    continue
                sign = (-1) ** (len(part) - 1)
                fac = sp.factorial(len(part) - 1)
                term = 1
                for block in part:
                    term *= mom(tuple(t[i] for i in block))
                total += sign * fac * term
            kappa[t] = sp.simplify(total)
    sig = sp.Matrix(m, m, lambda i, j: kappa[(i, j)])
    return sig, kappa


def phi6_coeff(sig, kappa, m):
    S = sp.simplify(sig.inv())
    R = range(m)
    C6 = sum(kappa[t] * wick_ee(t, S) for t in itertools.product(R, repeat=6))
    return sp.simplify(-sp.Rational(4, 720) * C6)


def var_w_coeff(sig, kappa, m):
    S = sp.simplify(sig.inv())
    R = range(m)
    # Cov(f_P, f_{P'}) with g0,g scaled: extract C where Cov = C/n^4
    # Wick E[k4(u)k4(v)] - E k4(u) E k4(v)
    C = 0
    for t1 in itertools.product(R, repeat=4):
        for t2 in itertools.product(R, repeat=4):
            idxs = t1 + t2
            wsum = 0
            for pairing in _matchings(8):
                pt = 1
                for ia, ib in pairing:
                    # g0=2 for same edge, g=1 for adjacent
                    same = (ia < 4) == (ib < 4)
                    pt *= (2 if same else 1) * S[idxs[ia], idxs[ib]]
                wsum += pt
            EE_prod = kappa[t1] * kappa[t2] * wsum
            # subtract disconnected: E k4(u) E k4(v) with g0=2
            eu = kappa[t1] * wick_ee(t1, 2 * S)
            ev = kappa[t2] * wick_ee(t2, 2 * S)
            # Only subtract once outside loops — fix below
            C += EE_prod
            # mark: we'll subtract E^2 separately
            _ = eu, ev
    EE_u = sum(kappa[t] * wick_ee(t, 2 * S) for t in itertools.product(R, repeat=4))
    C = sp.simplify(C - EE_u**2)
    return sp.simplify(sp.Rational(1, 1152) * C)


def pieces(a_val, lam_val):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    ds = []
    details = []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=6)
        m = len(states[0])
        d6 = phi6_coeff(sig, kappa, m)
        dw = var_w_coeff(sig, kappa, m)
        ds.append(sp.simplify(d6 + dw))
        details.append((d6, dw))
    D = sp.simplify(ds[2] + ds[0] - 2 * ds[1])
    return D, ds, details


def main():
    lam = sp.Rational(1, 2)
    states, probs = laws(sp.Rational(1, 10), lam)[0]
    sig, kappa = sigma_and_cumulants(states, probs, max_ell=4)
    p = lam
    print("kappa2", kappa[(0, 0)], "expect", p * (1 - p))
    print("kappa3", kappa[(0, 0, 0)], "expect", p * (1 - p) * (1 - 2 * p))
    print(
        "kappa4",
        kappa[(0, 0, 0, 0)],
        "expect",
        p * (1 - p) * (1 - 6 * p * (1 - p)),
    )

    if "--grid" in sys.argv:
        pts = [
            (Fraction(1, 10), Fraction(1, 2)),
            (Fraction(1, 20), Fraction(1, 2)),
            (Fraction(1, 50), Fraction(1, 2)),
            (Fraction(1, 7), Fraction(2, 5)),
        ]
        for an, ln in pts:
            print(f"computing a={an} lam={ln}...", flush=True)
            D, ds, details = pieces(an, ln)
            print(f"a={an} lam={ln}: D_partial={D}")
            print(f"  d1,d2,d3={ds}")
            print(f"  (d6,dw)={details}")


if __name__ == "__main__":
    main()
