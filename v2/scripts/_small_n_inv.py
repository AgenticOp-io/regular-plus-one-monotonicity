"""Exact E[1/N | containment] for n=6, D=2 iso-types. Workshop only.

Two isomorphism classes of simple 2-regular graphs on 6 labelled vertices:
Hamiltonian cycles C6, and disjoint unions of two triangles C3+C3.
For each class, compute the conditional expectation of 1/N given that a
fixed representative is contained in G(6,p), by enumerating the complement.
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from fractions import Fraction


def all_edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def cycle_edges(verts: list[int]) -> frozenset[tuple[int, int]]:
    m = len(verts)
    edges = []
    for i in range(m):
        a, b = verts[i], verts[(i + 1) % m]
        edges.append((min(a, b), max(a, b)))
    return frozenset(edges)


def labelled_c6(n: int = 6) -> list[frozenset[tuple[int, int]]]:
    # (n-1)!/2 directed cycles up to reflection, as edge sets
    out: set[frozenset[tuple[int, int]]] = set()
    for perm in itertools.permutations(range(1, n)):
        verts = [0, *perm]
        out.add(cycle_edges(verts))
    return sorted(out, key=lambda s: tuple(sorted(s)))


def labelled_two_triangles(n: int = 6) -> list[frozenset[tuple[int, int]]]:
    out: set[frozenset[tuple[int, int]]] = set()
    for triple in itertools.combinations(range(n), 3):
        other = [v for v in range(n) if v not in triple]
        # each K3 has a unique 3-cycle edge set
        e1 = cycle_edges(list(triple))
        e2 = cycle_edges(other)
        out.add(e1 | e2)
    return sorted(out, key=lambda s: tuple(sorted(s)))


def edge_index(n: int) -> dict[tuple[int, int], int]:
    return {e: i for i, e in enumerate(all_edges(n))}


def bitmask(edges: frozenset[tuple[int, int]], index: dict[tuple[int, int], int]) -> int:
    m = 0
    for e in edges:
        m |= 1 << index[e]
    return m


def expect_inv_n(
    g0: frozenset[tuple[int, int]],
    all_factors: list[int],
    n: int,
    p: Fraction,
) -> Fraction:
    index = edge_index(n)
    g0_mask = bitmask(g0, index)
    complement = [e for e in all_edges(n) if e not in g0]
    comp_bits = [index[e] for e in complement]
    total = Fraction(0)
    for bits in range(1 << len(complement)):
        host = g0_mask
        weight = Fraction(1)
        for i, b in enumerate(comp_bits):
            if bits & (1 << i):
                host |= 1 << b
                weight *= p
            else:
                weight *= 1 - p
        N = sum(1 for f in all_factors if f & host == f)
        assert N >= 1
        total += weight / N
    return total


def main() -> None:
    n = 6
    c6 = labelled_c6(n)
    tt = labelled_two_triangles(n)
    index = edge_index(n)
    all_factors = [bitmask(g, index) for g in c6 + tt]
    print(f"|C6|={len(c6)}  |C3+C3|={len(tt)}  |Omega|={len(all_factors)}")

    # one representative of each class
    g_c6 = c6[0]
    g_tt = tt[0]
    for e_num, e_den in ((1, 2), (1, 3), (2, 3), (1, 4), (3, 4)):
        p = Fraction(e_num, e_den)
        a = expect_inv_n(g_c6, all_factors, n, p)
        b = expect_inv_n(g_tt, all_factors, n, p)
        ratio = a / b
        print(
            f"p={p}:  E[1/N|C6]={float(a):.8f}  "
            f"E[1/N|C3+C3]={float(b):.8f}  ratio={float(ratio):.8f}"
        )


if __name__ == "__main__":
    main()
