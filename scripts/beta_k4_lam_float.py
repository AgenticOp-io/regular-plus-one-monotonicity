"""Float kappa4 residue vs lambda (max_ell=3 only)."""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_second_diff import kappa4_star_path_num
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def ad_k4(a_val, lam_val):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    ks = []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=3)
        m = len(states[0])
        if m == 1:
            ks.append(0.0)
            continue
        S = np.array([[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)])
        k4, _, _, _ = kappa4_star_path_num(S, kappa, m)
        ks.append(k4)
    return float(a_val) * (ks[2] + ks[0] - 2 * ks[1])


def main() -> None:
    for ln in [
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(1, 2),
        Fraction(3, 5),
        Fraction(2, 3),
    ]:
        y20 = ad_k4(Fraction(1, 20), ln)
        y40 = ad_k4(Fraction(1, 40), ln)
        # y = b0 + b1 a => b0 = 2*y40 - y20 when a=1/40,1/20
        b0 = 2 * y40 - y20
        lam = float(ln)
        cands = {
            "3/8": 3 / 8,
            "3/(8*lam)": 3 / (8 * lam),
            "3(1-lam)/(8*lam)": 3 * (1 - lam) / (8 * lam),
            "3/(8*lam^2)": 3 / (8 * lam**2),
            "3(1-lam)/(8*lam^2)": 3 * (1 - lam) / (8 * lam**2),
        }
        print(f"lam={ln} y20={y20:.6f} y40={y40:.6f} b0~{b0:.6f}", flush=True)
        for name, val in cands.items():
            print(f"  vs {name}: err={b0 - val:+.5f}", flush=True)


if __name__ == "__main__":
    main()
