"""Exact-rational signed Gao main term after a matching host of t edges.

Workshop only. Do not treat output as a theorem.
"""

from __future__ import annotations

from fractions import Fraction


def signed_q(n: int, L: int, t: int) -> Fraction:
    M = Fraction(L * n - 2 * t)
    M2 = Fraction(n * L * (L - 1) - 4 * t * (L - 1))
    phi = Fraction(L * L - 4 * L + 2) - Fraction(2 * (L - 1) * M2, M)
    wsum = Fraction(2 * t * (L - 1) ** 2, M * M)
    mom = 1 - M2 * M2 / (M**3) - M2 / (M * M) - wsum
    return (L * L / M) * mom * (1 - phi / M)


def unsigned_q(n: int, L: int, t: int) -> Fraction:
    M = Fraction(L * n - 2 * t)
    return Fraction(L * L, M)


def p(n: int, L: int) -> Fraction:
    return Fraction(L, n - 1)


def report(n: int, L: int, t: int) -> None:
    pq = p(n, L)
    qs = signed_q(n, L, t)
    qu = unsigned_q(n, L, t)
    rs = qs / pq - 1
    ru = qu / pq - 1
    print(
        f"n={n} L={L} t={t}  signed-1={float(rs):+.6e}  "
        f"unsigned-1={float(ru):+.6e}  "
        f"signed*n^2={float(rs * n * n):+.4f}  "
        f"unsigned*n={float(ru * n):+.4f}"
    )


def report_diff(n: int, L: int, t: int) -> None:
    pq = p(n, L)
    qs = signed_q(n, L, t)
    lead = Fraction(2 * t, L * n)
    d = qs / pq - 1 - lead
    print(
        f"n={n} L={L} t={t}  d={float(d):+.6e}  "
        f"d*n^2={float(d * n * n):+.4f}  "
        f"d*n^2/t={float(d * n * n / max(t, 1)):+.4f}  "
        f"d*n^2/L^2={float(d * n * n / (L * L)):+.4f}"
    )


def main() -> None:
    for L in (4, 10):
        print(f"--- L={L} empty ---")
        for n in (200, 800, 3200):
            report(n, L, 0)
        print(f"--- L={L} diffs ---")
        for n, t in ((800, 2), (3200, 2), (3200, 8), (3200, 16), (12800, 16), (3200, L * L), (12800, L * L)):
            report_diff(n, L, t)


if __name__ == "__main__":
    main()
