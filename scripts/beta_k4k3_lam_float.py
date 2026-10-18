"""Float residues of kappa4 and kappa3 vs lambda (no Phi6)."""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_full_inventory import kappa3_xxw_path, kappa3_xxw_star
from scripts.beta_second_diff import kappa4_star_path_num
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def ad_k4_k3(a_val, lam_val):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    k4s, k3s = [], []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=4)
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
    af = float(a_val)
    return af * Dk4, af * Dk3


def main() -> None:
    print("lam | a | Da_k4 | Da_k3 | extrap guesses", flush=True)
    for ln in [
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(1, 2),
        Fraction(3, 5),
        Fraction(2, 3),
    ]:
        ys4, ys3 = [], []
        for N in [20, 40]:
            y4, y3 = ad_k4_k3(Fraction(1, N), ln)
            ys4.append((1 / N, y4))
            ys3.append((1 / N, y3))
            print(f"lam={ln} a=1/{N} k4={y4:.6f} k3={y3:.6f}", flush=True)
        # linear extrap y = b0 + b1 a
        (a0, y40), (a1, y41) = ys4
        b04 = (y40 * a1 - y41 * a0) / (a1 - a0) if a1 != a0 else y40
        (a0, y30), (a1, y31) = ys3
        b03 = (y30 * a1 - y31 * a0) / (a1 - a0)
        print(
            f"  extrap k4~{b04:.6f} k3~{b03:.6f} "
            f"3/8={0.375} -131/108={-131/108:.6f}",
            flush=True,
        )
        # compare to candidate forms
        lam = float(ln)
        cands = {
            "3/(8*lam)": 3 / (8 * lam),
            "3*(1-lam)/(8*lam)": 3 * (1 - lam) / (8 * lam),
            "3/(8*lam^2)": 3 / (8 * lam**2),
            "-131/(108*lam)": -131 / (108 * lam),
            "-131*(1-lam)/(108*lam)": -131 * (1 - lam) / (108 * lam),
            "-131/(108*lam^2)": -131 / (108 * lam**2),
        }
        for name, val in cands.items():
            if "3/" in name:
                print(f"    k4 vs {name}: {b04 - val:+.4f}", flush=True)
            else:
                print(f"    k3 vs {name}: {b03 - val:+.4f}", flush=True)


if __name__ == "__main__":
    main()
