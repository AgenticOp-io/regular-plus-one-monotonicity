"""Identify a*Delta(k4+k3) as rationals and interpolate the a->0 limit."""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_full_inventory import kappa3_xxw_path, kappa3_xxw_star
from scripts.beta_second_diff import kappa4_star_path_num
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def pieces(a_val: Fraction):
    a = sp.nsimplify(a_val)
    lam = sp.Rational(1, 2)
    k4s, k3s = [], []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=6)
        m = len(states[0])
        if m == 1:
            k4s.append(0.0)
            k3s.append(0.0)
            continue
        S = np.array([[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)])
        k4, _, _, _ = kappa4_star_path_num(S, kappa, m)
        k3 = kappa3_xxw_star(S, kappa, m) + kappa3_xxw_path(S, kappa, m)
        k4s.append(k4)
        k3s.append(k3)
    Dk4 = k4s[2] + k4s[0] - 2 * k4s[1]
    Dk3 = k3s[2] + k3s[0] - 2 * k3s[1]
    return Dk4, Dk3


def main() -> None:
    rows = []
    for N in [8, 10, 12, 15, 16, 20, 24, 30]:
        an = Fraction(1, N)
        Dk4, Dk3 = pieces(an)
        aD = an * (Dk4 + Dk3)
        # identify aD as rational
        r = sp.nsimplify(aD, tolerance=1e-9, full=True)
        print(
            f"a=1/{N} aD_float={float(aD):.12f} identified={r} "
            f"(k4={an*Dk4:.8f} k3={an*Dk3:.8f})",
            flush=True,
        )
        rows.append((sp.Rational(1, N), sp.simplify(r)))

    # Interpolate rational function of degree <= 3 in numerator/denom
    # Try: aD = (p0 + p1 a + p2 a^2)/(1 + q1 a) or polynomial
    a = sp.symbols("a")
    # polynomial degree 3 through first 4 points, check rest
    A = sp.Matrix([[1, ai, ai**2, ai**3] for ai, _ in rows[:4]])
    b = A.solve(sp.Matrix([yi for _, yi in rows[:4]]))
    print("poly3 coeffs", b, flush=True)
    print("b0", b[0], float(b[0]), flush=True)
    for ai, yi in rows:
        pred = sum(b[i] * ai**i for i in range(4))
        print(f"  a={ai} pred={pred} actual={yi} err={sp.simplify(pred-yi)}", flush=True)

    # Also try aD = b0 + b1 a + b2 a^2 + b3 a^3 + b4 a^4 on 5 pts
    A5 = sp.Matrix([[1, ai, ai**2, ai**3, ai**4] for ai, _ in rows[:5]])
    b5 = A5.solve(sp.Matrix([yi for _, yi in rows[:5]]))
    print("poly4 b0", b5[0], float(b5[0]), flush=True)
    for ai, yi in rows:
        pred = sum(b5[i] * ai**i for i in range(5))
        print(
            f"  a={ai} pred4={float(pred):.10f} actual={float(yi):.10f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
