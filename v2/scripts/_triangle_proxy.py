"""Conditional triangle first-moment factor vs (1+e)/(2+e). Workshop only."""

from __future__ import annotations

from fractions import Fraction


def p_over_denom(n: int, D: int, e: Fraction) -> Fraction:
    """p / (pi + (1-pi)p); tends to (1+e)/(2+e) for D=o(n), D->inf."""
    pi = Fraction(D, n - 1)
    p = (1 + e) * Fraction(D, n)
    return p / (pi + (1 - pi) * p)


def main() -> None:
    for e in (Fraction(1, 100), Fraction(1, 10), Fraction(1), Fraction(3)):
        target = (1 + e) / (2 + e)
        print(f"--- e={float(e)}  target={float(target):.8f} ---")
        for n, D in ((10**3, 40), (10**4, 100), (10**5, 500), (10**6, 2000)):
            r = p_over_denom(n, D, e)
            print(
                f"n={n} D={D} p/denom={float(r):.8f}  "
                f"err={float(r - target):.2e}"
            )


if __name__ == "__main__":
    main()
