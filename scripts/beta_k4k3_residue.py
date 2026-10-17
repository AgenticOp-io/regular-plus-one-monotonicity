"""Extrapolate lim a->0 of a*Delta(kappa4 trees + kappa3 star/path)."""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_full_inventory import kappa3_xxw_path, kappa3_xxw_star
from scripts.beta_second_diff import kappa4_star_path_num
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def delta_k4k3(a_val: Fraction) -> float:
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
    D = (k4s[2] + k4s[0] - 2 * k4s[1]) + (k3s[2] + k3s[0] - 2 * k3s[1])
    return float(a_val) * D


def main() -> None:
    xs, ys = [], []
    for N in [8, 10, 12, 16, 20, 30, 40, 50, 60]:
        an = Fraction(1, N)
        y = delta_k4k3(an)
        xs.append(sp.Rational(1, N))
        ys.append(y)
        print(f"a=1/{N} aD={y:.10f}", flush=True)

    # Fit y = b0 + b1 a + b2 a^2 + b3 a^3 using last 4 points
    pts = list(zip(xs[-4:], ys[-4:]))
    A = sp.Matrix([[1, a, a**2, a**3] for a, _ in pts])
    b = A.solve(sp.Matrix([y for _, y in pts]))
    print(f"fit b0..b3 = {[sp.N(bi, 20) for bi in b]}", flush=True)
    print(f"b0 as rational ~ {sp.nsimplify(b[0], tolerance=1e-4)}", flush=True)
    # check earlier points
    for a, y in zip(xs, ys):
        pred = sum(b[i] * a**i for i in range(4))
        print(f"  check a={a}: pred={float(pred):.8f} actual={y:.8f}", flush=True)


if __name__ == "__main__":
    main()
