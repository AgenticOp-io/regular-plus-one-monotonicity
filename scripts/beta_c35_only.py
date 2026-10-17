"""Residue of C35 = -Cov(X, Im Phi5) alone, including smaller a."""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_full_inventory import cov_x_phi5_coeff
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def main() -> None:
    print("a | D_c35 | a*D | m2 | m3", flush=True)
    for an in [
        Fraction(1, 8),
        Fraction(1, 12),
        Fraction(1, 16),
        Fraction(1, 20),
        Fraction(1, 30),
        Fraction(1, 40),
        Fraction(1, 50),
    ]:
        a = sp.nsimplify(an)
        lam = sp.Rational(1, 2)
        vals = []
        for states, probs in laws(a, lam):
            probs = [sp.nsimplify(p) for p in probs]
            states = [tuple(int(x) for x in s) for s in states]
            sig, kappa = sigma_and_cumulants(states, probs, max_ell=5)
            m = len(states[0])
            if m == 1:
                vals.append(0.0)
                continue
            S = np.array(
                [[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)]
            )
            vals.append(cov_x_phi5_coeff(S, kappa, m))
        D = vals[2] + vals[0] - 2 * vals[1]
        print(
            f"a={an} D={D:.6f} aD={D*float(an):.6f} m2={vals[1]:.6f} m3={vals[2]:.6f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
