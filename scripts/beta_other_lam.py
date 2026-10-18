from fractions import Fraction

import sympy as sp

from scripts.beta_full_inventory import inventory


def main() -> None:
    for lam in [sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(3, 5)]:
        print("lam", lam, flush=True)
        for N in [10, 20, 40]:
            Ds, _ = inventory(Fraction(1, N), lam)
            a = 1 / N
            print(
                f"  a=1/{N} Da_tot={Ds['total']*a:.4f} "
                f"p64={Ds['p64']*a:.4f} c35={Ds['c35']*a:.4f} "
                f"k4={Ds['k4']*a:.4f} k3={Ds['k3xw']*a:.4f}",
                flush=True,
            )


if __name__ == "__main__":
    main()
