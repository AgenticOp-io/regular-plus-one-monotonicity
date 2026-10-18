"""Residues of a^{-1} packages vs lambda (float grid + C35 exact)."""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import sympy as sp

from scripts.beta_c35_exact import cov_x_phi5_exact
from scripts.beta_full_inventory import (
    cov_x_phi5_coeff,
    kappa3_xxw_path,
    kappa3_xxw_star,
)
from scripts.beta_second_diff import kappa4_star_path_num
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import phi6_coeff, sigma_and_cumulants, var_w_coeff


def float_pieces(a_val, lam_val):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    rows = []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=6)
        m = len(states[0])
        S = np.array([[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)])
        p64 = float(phi6_coeff(sig, kappa, m) + var_w_coeff(sig, kappa, m))
        if m == 1:
            k4 = c35 = k3 = 0.0
        else:
            k4, _, _, _ = kappa4_star_path_num(S, kappa, m)
            c35 = cov_x_phi5_coeff(S, kappa, m)
            k3 = kappa3_xxw_star(S, kappa, m) + kappa3_xxw_path(S, kappa, m)
        rows.append(dict(p64=p64, c35=c35, k4=k4, k3=k3))

    def D(key):
        return rows[2][key] + rows[0][key] - 2 * rows[1][key]

    return {k: D(k) for k in rows[0]}


def c35_exact_ad(a_val, lam_val):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    ds = []
    for states, probs in laws(a, lam):
        probs = [sp.nsimplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=5)
        m = len(states[0])
        ds.append(sp.Integer(0) if m == 1 else cov_x_phi5_exact(sig, kappa, m))
    D = sp.simplify(ds[2] + ds[0] - 2 * ds[1])
    return sp.simplify(a * D)


def main() -> None:
    print("=== float aD at a=1/40 ===", flush=True)
    a = Fraction(1, 40)
    for ln in [
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(1, 2),
        Fraction(3, 5),
        Fraction(2, 3),
        Fraction(3, 4),
    ]:
        Ds = float_pieces(a, ln)
        af = float(a)
        tgt_p64 = float((1 - ln) / (2 * ln))
        print(
            f"lam={ln} p64={Ds['p64']*af:.6f}(tgt {tgt_p64:.6f}) "
            f"c35={Ds['c35']*af:.6f} k4={Ds['k4']*af:.6f} "
            f"k3={Ds['k3']*af:.6f} tot={sum(Ds[k] for k in Ds)*af:.6f}",
            flush=True,
        )

    print("=== exact C35 aD -> residue via 3-pt quadratic ===", flush=True)
    for ln in [sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(3, 5)]:
        pts = []
        for N in [8, 12, 20]:
            a = sp.Rational(1, N)
            print(f"  C35 lam={ln} a={a}...", flush=True)
            y = c35_exact_ad(a, ln)
            pts.append((a, y))
            print(f"    aD={y}", flush=True)
        A = sp.Matrix([[1, a, a**2] for a, _ in pts])
        b = A.solve(sp.Matrix([y for _, y in pts]))
        print(f"  lam={ln} b0={b[0]} = {sp.N(b[0], 15)}", flush=True)


if __name__ == "__main__":
    main()
