"""Float kappa3 (star+path) residue vs lambda."""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_full_inventory import kappa3_xxw_path, kappa3_xxw_star
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def ad_k3(a_val, lam_val):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    ks = []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=4)
        m = len(states[0])
        if m == 1:
            ks.append(0.0)
            continue
        S = np.array([[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)])
        ks.append(kappa3_xxw_star(S, kappa, m) + kappa3_xxw_path(S, kappa, m))
    return float(a_val) * (ks[2] + ks[0] - 2 * ks[1])


def main() -> None:
    for ln in [
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(1, 2),
        Fraction(3, 5),
        Fraction(2, 3),
    ]:
        y20 = ad_k3(Fraction(1, 20), ln)
        y40 = ad_k3(Fraction(1, 40), ln)
        b0 = 2 * y40 - y20  # linear extrap
        cand = -131 / 108 * (1 - float(ln)) / float(ln)
        print(
            f"lam={ln} y20={y20:.6f} y40={y40:.6f} b0~{b0:.6f} "
            f"cand={cand:.6f} err={b0-cand:+.5f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
