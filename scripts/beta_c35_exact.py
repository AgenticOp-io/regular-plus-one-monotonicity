"""Exact rational a*D for C35 at lambda=1/2; series residue."""

from __future__ import annotations

import itertools
from fractions import Fraction

import sympy as sp

from scripts.multicolour_constant import laws
from scripts.next_order_sparse import _matchings, sigma_and_cumulants


def cov_x_phi5_exact(sig, kappa, m):
    S = sp.simplify(sig.inv())
    R = range(m)
    k3 = {t: kappa[t] for t in itertools.product(R, repeat=3)}
    k5 = {t: kappa[t] for t in itertools.product(R, repeat=5)}
    # E[k3(u)k5(v)] with cov [[2,1],[1,2]]
    C = 0
    pairs = list(_matchings(8))
    for t3 in itertools.product(R, repeat=3):
        for t5 in itertools.product(R, repeat=5):
            idxs = t3 + t5
            wsum = 0
            for pairing in pairs:
                pt = 1
                for ia, ib in pairing:
                    ra = 0 if ia < 3 else 1
                    rb = 0 if ib < 3 else 1
                    g = 2 if ra == rb else 1
                    pt *= g * S[idxs[ia], idxs[ib]]
                wsum += pt
            C += k3[t3] * k5[t5] * wsum
    return sp.simplify(C / 1440)


def main() -> None:
    lam = sp.Rational(1, 2)
    print("exact C35 second difference", flush=True)
    for an in [Fraction(1, 8), Fraction(1, 10), Fraction(1, 12), Fraction(1, 20)]:
        a = sp.Rational(an)
        ds = []
        for states, probs in laws(a, lam):
            probs = [sp.nsimplify(p) for p in probs]
            states = [tuple(int(x) for x in s) for s in states]
            sig, kappa = sigma_and_cumulants(states, probs, max_ell=5)
            m = len(states[0])
            if m == 1:
                ds.append(sp.Integer(0))
            else:
                ds.append(cov_x_phi5_exact(sig, kappa, m))
        D = sp.simplify(ds[2] + ds[0] - 2 * ds[1])
        print(f"a={an} D={D} aD={sp.simplify(a*D)}", flush=True)

    # series at symbolic a via several points → interpolate residue
    # Use a=1/N for N=8,12,20,30 and fit aD = b0 + b1 a + b2 a^2
    pts = []
    for N in [8, 12, 20, 30]:
        a = sp.Rational(1, N)
        ds = []
        for states, probs in laws(a, lam):
            probs = [sp.nsimplify(p) for p in probs]
            states = [tuple(int(x) for x in s) for s in states]
            sig, kappa = sigma_and_cumulants(states, probs, max_ell=5)
            m = len(states[0])
            ds.append(
                sp.Integer(0)
                if m == 1
                else cov_x_phi5_exact(sig, kappa, m)
            )
        D = sp.simplify(ds[2] + ds[0] - 2 * ds[1])
        pts.append((a, sp.simplify(a * D)))
        print(f"interp point a={a} aD={pts[-1][1]}", flush=True)

    # fit quadratic in a: aD = b0 + b1 a + b2 a^2 using first 3 pts, check 4th
    a0, y0 = pts[0]
    a1, y1 = pts[1]
    a2, y2 = pts[2]
    A = sp.Matrix([
        [1, a0, a0**2],
        [1, a1, a1**2],
        [1, a2, a2**2],
    ])
    b = A.solve(sp.Matrix([y0, y1, y2]))
    print(f"fit b0,b1,b2 = {b[0]}, {b[1]}, {b[2]}", flush=True)
    a3, y3 = pts[3]
    pred = sp.simplify(b[0] + b[1] * a3 + b[2] * a3**2)
    print(f"check a={a3}: pred={pred} actual={y3}", flush=True)


if __name__ == "__main__":
    main()
