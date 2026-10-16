"""Constant term of the formal multi-colour local limit expansion.

For a pair law on states s in Z^m with covariance Sigma, cumulant tensors
k3, k4, and S = Sigma^{-1}, the O(1) constant of log N_m (beyond entropy,
determinant and parity factors) is

    c_m = K4/4 - T3/12 - T1/4,
    K4 = k4_{abcd} S_ab S_cd,
    T3 = k3_{abc} k3_{def} S_ad S_be S_cf,
    T1 = w^T S w,  w_c = k3_{abc} S_ab.

The script checks c_1 against McKay-Wormald and prints
C = c_3 + c_1 - 2 c_2 for the two-factor second moment.
"""

import itertools
import sys
from fractions import Fraction

import sympy as sp


def constant(states, probs):
    m = len(states[0])
    mean = [sum(p * s[i] for s, p in zip(states, probs)) for i in range(m)]
    cen = [[s[i] - mean[i] for i in range(m)] for s in states]

    def mom(*idx):
        return sum(p * sp.Mul(*[c[i] for i in idx]) for c, p in zip(cen, probs))

    R = range(m)
    sig = sp.Matrix(m, m, lambda i, j: mom(i, j))
    S = sig.inv()
    k3 = {t: mom(*t) for t in itertools.product(R, repeat=3)}
    k4 = {}
    for a, b, c, d in itertools.product(R, repeat=4):
        k4[a, b, c, d] = (mom(a, b, c, d) - sig[a, b] * sig[c, d]
                          - sig[a, c] * sig[b, d] - sig[a, d] * sig[b, c])
    K4 = sum(k4[a, b, c, d] * S[a, b] * S[c, d]
             for a, b, c, d in itertools.product(R, repeat=4))
    T3 = sum(k3[a, b, c] * k3[d, e, f] * S[a, d] * S[b, e] * S[c, f]
             for a, b, c, d, e, f in itertools.product(R, repeat=6))
    w = [sum(k3[a, b, c] * S[a, b] for a in R for b in R) for c in R]
    T1 = sum(w[c] * S[c, f] * w[f] for c in R for f in R)
    return K4 / 4 - T3 / 12 - T1 / 4


def laws(a, lam):
    one = ([(0,), (1,)], [1 - lam, lam])
    two = ([(0, 0), (1, 0), (1, 1)], [1 - lam, lam - a, a])
    three = ([(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 0, 1), (1, 1, 1)],
             [1 - lam, lam - 2 * a + a**2 / lam, a - a**2 / lam,
              a - a**2 / lam, a**2 / lam])
    return one, two, three


def main():
    a, lam = sp.symbols("a lam", positive=True)
    one, two, three = laws(a, lam)
    c1 = sp.simplify(constant(*one))
    Lam = lam * (1 - lam)
    print("c1 - (-1/6 - 1/(12 Lam)) =", sp.simplify(c1 - (-sp.Rational(1, 6) - 1 / (12 * Lam))))
    if "--grid" in sys.argv:
        for an, ln in [(Fraction(1, 10), Fraction(1, 2)), (Fraction(1, 7), Fraction(2, 5)),
                       (Fraction(1, 20), Fraction(3, 4)), (Fraction(1, 5), Fraction(1, 2))]:
            o, t, h = laws(sp.Rational(an.numerator, an.denominator),
                           sp.Rational(ln.numerator, ln.denominator))
            val = sp.nsimplify(constant(*h) + constant(*o) - 2 * constant(*t))
            print(f"a={an} lam={ln}: C =", sp.simplify(val))
        return
    c2 = sp.simplify(constant(*two))
    c3 = sp.simplify(constant(*three))
    C = sp.factor(sp.simplify(c3 + c1 - 2 * c2))
    print("c2 =", sp.factor(c2))
    print("c3 =", sp.factor(c3))
    print("C  =", C)
    print("series in a:", sp.series(C, a, 0, 4))


if __name__ == "__main__":
    main()
