"""Exact nu vs mu triangle density on n=6, D=2. Workshop only."""

from __future__ import annotations

import itertools
from fractions import Fraction

from _small_n_inv import (
    all_edges,
    bitmask,
    edge_index,
    expect_inv_n,
    labelled_c6,
    labelled_two_triangles,
)


def triangle_edges(a: int, b: int, c: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        {
            (min(a, b), max(a, b)),
            (min(b, c), max(b, c)),
            (min(a, c), max(a, c)),
        }
    )


def main() -> None:
    n = 6
    c6 = labelled_c6(n)
    tt = labelled_two_triangles(n)
    graphs = c6 + tt
    index = edge_index(n)
    factors = [bitmask(g, index) for g in graphs]
    T = triangle_edges(0, 1, 2)
    T_mask = bitmask(T, index)
    containing = [g for g in graphs if T <= g]
    print(f"|Omega_T|={len(containing)}  mu(T)={len(containing)}/{len(graphs)}")

    edges = all_edges(n)
    m = len(edges)  # 15
    for e_num, e_den in ((1, 2), (1, 3), (2, 3), (1, 4), (3, 4)):
        p = Fraction(e_num, e_den)
        # class-wise a-values
        a_c6 = expect_inv_n(c6[0], factors, n, p)
        a_tt = expect_inv_n(tt[0], factors, n, p)
        a_bar = (60 * a_c6 + 10 * a_tt) / 70
        # only C3+C3 graphs contain T; all ten have same a by S_n? wait - only ONE contains fixed T
        assert len(containing) == 1
        a_cond = a_tt  # that unique graph is C3+C3 type
        ratio_pred = a_cond / a_bar
        mu = Fraction(1, 70)
        nu_pred = mu * ratio_pred

        # direct: enumerate all hosts
        mass_nt_over_n = Fraction(0)
        mass_n_pos = Fraction(0)
        for bits in range(1 << m):
            weight = Fraction(1)
            host = 0
            for i in range(m):
                if bits & (1 << i):
                    host |= 1 << i
                    weight *= p
                else:
                    weight *= 1 - p
            N = sum(1 for f in factors if f & host == f)
            if N == 0:
                continue
            N_T = sum(1 for f in factors if f & host == f and (f & T_mask) == T_mask)
            mass_n_pos += weight
            mass_nt_over_n += weight * Fraction(N_T, N)
        nu_direct = mass_nt_over_n / mass_n_pos
        print(
            f"p={p}: mu={float(mu):.6f}  nu_pred={float(nu_pred):.6f}  "
            f"nu_direct={float(nu_direct):.6f}  nu/mu={float(nu_direct/mu):.6f}  "
            f"a_tt/a_bar={float(ratio_pred):.6f}"
        )


if __name__ == "__main__":
    main()
