"""Independence-approx relative second moment of N (log-space). Workshop only."""

from __future__ import annotations

from math import log


def log_rel_var(n: int, D: int, e: float) -> float:
    pi = D / (n - 1)
    p = (1 + e) * D / n
    s = D * n / 2
    m = n * (n - 1) / 2
    # G0-edge ratio a/b^2 == 1 (checked)
    c = 1 - pi**2 + pi**2 / p
    return (m - s) * log(c)


def main() -> None:
    for n, D, e in (
        (1000, 20, 0.1),
        (1000, 30, 0.1),
        (10000, 50, 0.05),
        (10000, 100, 0.1),
        (10**5, 200, 0.1),
        (6, 2, 1.0),
    ):
        lr = log_rel_var(n, D, e)
        print(
            f"n={n} D={D} e={e} logRV={lr:.4f}  "
            f"Dn/(2(1+e))={n*D/(2*(1+e)):.2f}  ratio={lr/(n*D/(2*(1+e))):.4f}"
        )


if __name__ == "__main__":
    main()
