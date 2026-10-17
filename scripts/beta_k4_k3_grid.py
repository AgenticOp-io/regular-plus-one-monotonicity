"""Residues of kappa4 star+path and kappa3 star alone."""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_full_inventory import kappa3_xxw_star
from scripts.beta_second_diff import kappa4_star_path_num
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def main() -> None:
    print("a | Da_k4 | Da_k3 | Da_sum", flush=True)
    for an in [
        Fraction(1, 10),
        Fraction(1, 12),
        Fraction(1, 16),
        Fraction(1, 20),
        Fraction(1, 30),
        Fraction(1, 40),
    ]:
        a = sp.nsimplify(an)
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
            S = np.array(
                [[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)]
            )
            k4, star, path, fork = kappa4_star_path_num(S, kappa, m)
            _ = star, path, fork  # available for diagnostics
            k3 = kappa3_xxw_star(S, kappa, m)
            k4s.append(k4)
            k3s.append(k3)
        Dk4 = k4s[2] + k4s[0] - 2 * k4s[1]
        Dk3 = k3s[2] + k3s[0] - 2 * k3s[1]
        af = float(an)
        print(
            f"a={an} Da_k4={Dk4*af:.6f} Da_k3={Dk3*af:.6f} "
            f"Da_sum={(Dk4+Dk3)*af:.6f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
