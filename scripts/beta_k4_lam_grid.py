"""Float kappa4 (star+path+fork) residue vs lambda; linear extrap in a."""

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
        print(f"    m={m} k4={k4:.6e}", flush=True)
    return float(a_val) * (ks[2] + ks[0] - 2 * ks[1])


def main() -> None:
    for ln in [Fraction(2, 5), Fraction(1, 2), Fraction(3, 5)]:
        print(f"lam={ln}", flush=True)
        y10 = ad_k4(Fraction(1, 10), ln)
        print(f"  a=1/10 aD={y10:.6f}", flush=True)
        y20 = ad_k4(Fraction(1, 20), ln)
        print(f"  a=1/20 aD={y20:.6f}", flush=True)
        # y = b0 + b1 a => b0 = 2*y20 - y10
        b0 = 2 * y20 - y10
        cand = 3 * (1 - float(ln)) / (8 * float(ln))
        print(f"  b0~{b0:.6f} cand={cand:.6f} err={b0 - cand:+.5f}", flush=True)


if __name__ == "__main__":
    main()
