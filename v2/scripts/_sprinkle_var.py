"""Sprinkle host degree variance vs G(n,p). Workshop only."""

from __future__ import annotations

from fractions import Fraction


def ratio(n: int, D: int, e: Fraction) -> Fraction:
    pi = Fraction(D, n - 1)
    p = (1 + e) * Fraction(D, n)
    q = (p - pi) / (1 - pi)
    var_s = (n - 1 - D) * q * (1 - q)
    var_b = (n - 1) * p * (1 - p)
    return var_s / var_b


def main() -> None:
    for e in (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)):
        print(f"--- e={float(e)} ---")
        for n, D in ((1000, 50), (5000, 100), (10000, 200), (20000, 400)):
            r = ratio(n, D, e)
            print(f"n={n} D={D} ratio={float(r):.6f}  ratio/e={float(r / e):.4f}")


if __name__ == "__main__":
    main()
