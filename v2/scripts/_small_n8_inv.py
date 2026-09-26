"""Monte Carlo E[1/N|containment] for n=8, D=2 iso-types. Workshop only."""

from __future__ import annotations

import itertools
import random
from collections import defaultdict


def all_edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def cycle_edges(verts: list[int]) -> frozenset[tuple[int, int]]:
    m = len(verts)
    edges = []
    for i in range(m):
        a, b = verts[i], verts[(i + 1) % m]
        edges.append((min(a, b), max(a, b)))
    return frozenset(edges)


def labelled_cycles(n: int, lengths: tuple[int, ...]) -> list[frozenset[tuple[int, int]]]:
    """All simple 2-regular graphs with the given cycle type (sorted lengths)."""
    assert sum(lengths) == n
    out: set[frozenset[tuple[int, int]]] = set()
    # assign vertices to cycle slots
    for perm in itertools.permutations(range(n)):
        edges: set[tuple[int, int]] = set()
        idx = 0
        for L in lengths:
            block = list(perm[idx : idx + L])
            idx += L
            edges |= set(cycle_edges(block))
        out.add(frozenset(edges))
    return list(out)


def edge_index(n: int) -> dict[tuple[int, int], int]:
    return {e: i for i, e in enumerate(all_edges(n))}


def bitmask(edges: frozenset[tuple[int, int]], index: dict[tuple[int, int], int]) -> int:
    m = 0
    for e in edges:
        m |= 1 << index[e]
    return m


def mc_expect(
    g0: frozenset[tuple[int, int]],
    all_factors: list[int],
    n: int,
    p: float,
    trials: int,
    rng: random.Random,
) -> float:
    index = edge_index(n)
    g0_mask = bitmask(g0, index)
    complement = [e for e in all_edges(n) if e not in g0]
    comp_bits = [index[e] for e in complement]
    total = 0.0
    for _ in range(trials):
        host = g0_mask
        for b in comp_bits:
            if rng.random() < p:
                host |= 1 << b
        N = 0
        for f in all_factors:
            if f & host == f:
                N += 1
        total += 1.0 / N
    return total / trials


def main() -> None:
    n = 8
    rng = random.Random(0)
    types = {
        "C8": (8,),
        "C5+C3": (5, 3),
        "C4+C4": (4, 4),
    }
    reps: dict[str, frozenset[tuple[int, int]]] = {}
    all_graphs: list[frozenset[tuple[int, int]]] = []
    for name, lengths in types.items():
        graphs = labelled_cycles(n, lengths)
        print(f"{name}: {len(graphs)}")
        reps[name] = graphs[0]
        all_graphs.extend(graphs)
    index = edge_index(n)
    factors = [bitmask(g, index) for g in all_graphs]
    print(f"|Omega|={len(factors)}")
    trials = 2000
    p = 0.5
    vals = {}
    for name, g0 in reps.items():
        vals[name] = mc_expect(g0, factors, n, p, trials, rng)
        print(f"p={p} trials={trials}  E[1/N|{name}]≈{vals[name]:.6f}")
    base = vals["C8"]
    for name, v in vals.items():
        if name != "C8":
            print(f"ratio C8/{name}≈{base / v:.4f}")


if __name__ == "__main__":
    main()
