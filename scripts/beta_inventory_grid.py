"""Finer a-grid for package residues (run after beta_full_inventory)."""

from __future__ import annotations

from fractions import Fraction

from scripts.beta_full_inventory import inventory


def main() -> None:
    print("a | Da_tot | Da_p64 | Da_k4 | Da_c35 | Da_k3 | c35(m2,m3)", flush=True)
    for an in [
        Fraction(1, 8),
        Fraction(1, 10),
        Fraction(1, 12),
        Fraction(1, 16),
        Fraction(1, 20),
    ]:
        Ds, rows = inventory(an)
        a = float(an)
        c35s = (rows[1]["c35"], rows[2]["c35"])
        print(
            f"a={an} Da_tot={Ds['total']*a:.6f} Da_p64={Ds['p64']*a:.6f} "
            f"Da_k4={Ds['k4']*a:.6f} Da_c35={Ds['c35']*a:.6f} "
            f"Da_k3={Ds['k3xw']*a:.6f} c35={c35s}",
            flush=True,
        )


if __name__ == "__main__":
    main()
