"""
Small-n probes for +1 monotonicity.

We cannot sample uniform G(n,d) efficiently for large n, but for tiny even n we can
enumerate regular graphs and measure:
  - fraction of d-regular G whose complement has a perfect matching
  - TV proxy between (uniform G) + (uniform matching in complement) vs uniform G(n,d+1)

This supports Lemma C/D intuition and catches bugs in future coupling code.
"""

from __future__ import annotations

import itertools
import random
from collections import Counter, defaultdict
from typing import Dict, FrozenSet, Iterable, List, Set, Tuple

Edge = FrozenSet[int]
Graph = FrozenSet[Edge]


def all_edges(n: int) -> List[Edge]:
    return [frozenset((i, j)) for i in range(n) for j in range(i + 1, n)]


def is_regular(n: int, edges: Iterable[Edge], d: int) -> bool:
    deg = [0] * n
    for e in edges:
        u, v = tuple(e)
        deg[u] += 1
        deg[v] += 1
    return all(x == d for x in deg)


def enumerate_regular(n: int, d: int) -> List[Graph]:
    """Brute-force enumerate d-regular graphs on n labeled vertices."""
    if (n * d) % 2 != 0:
        return []
    m = n * d // 2
    out: List[Graph] = []
    for combo in itertools.combinations(all_edges(n), m):
        if is_regular(n, combo, d):
            out.append(frozenset(combo))
    return out


def perfect_matchings(n: int) -> List[Graph]:
    """All perfect matchings on K_n (n even), as edge-sets."""
    assert n % 2 == 0
    verts = list(range(n))

    def helper(remaining: List[int]) -> List[List[Edge]]:
        if not remaining:
            return [[]]
        a = remaining[0]
        acc: List[List[Edge]] = []
        for i in range(1, len(remaining)):
            b = remaining[i]
            edge = frozenset((a, b))
            rest = remaining[1:i] + remaining[i + 1 :]
            for matching in helper(rest):
                acc.append([edge] + matching)
        return acc

    return [frozenset(m) for m in helper(verts)]


def complement_matchings(n: int, g: Graph, all_pm: List[Graph]) -> List[Graph]:
    return [m for m in all_pm if m.isdisjoint(g)]


def analyze(n: int, d: int) -> Dict[str, object]:
    regs_d = enumerate_regular(n, d)
    regs_dp1 = enumerate_regular(n, d + 1)
    pms = perfect_matchings(n)

    # Lemma C: every d-regular should extend if complement matching exists
    extendible = sum(1 for g in regs_d if complement_matchings(n, g, pms))
    # Build law of G ∪ M with M uniform in complement matchings
    h_counts: Counter = Counter()
    total = 0
    for g in regs_d:
        ms = complement_matchings(n, g, pms)
        if not ms:
            continue
        for m in ms:
            h = g | m
            h_counts[h] += 1
            total += 1

    # Compare to uniform on (d+1)-regular
    tv = None
    if regs_dp1 and total:
        unif = 1.0 / len(regs_dp1)
        # probabilities under G⊕M construction (only hits (d+1)-regular graphs)
        law = {h: h_counts[h] / total for h in regs_dp1}
        tv = 0.5 * sum(abs(law.get(h, 0.0) - unif) for h in set(law) | set(regs_dp1))

    return {
        "n": n,
        "d": d,
        "num_d": len(regs_d),
        "num_d1": len(regs_dp1),
        "extendible_frac": extendible / len(regs_d) if regs_d else None,
        "tv_uniform_matching_vs_Gd1": tv,
        "support_size_union_law": len(h_counts),
    }


def one_factorization_nested_ok(n: int) -> bool:
    """Sanity: classical nested regulars exist (not random)."""
    N = n - 1
    E = set()
    for r in range(N):
        matching = {frozenset((N, r % N))}
        for i in range(1, N // 2 + 1):
            matching.add(frozenset(((r + i) % N, (r - i) % N)))
        E |= matching
        deg = Counter()
        for e in E:
            u, v = tuple(e)
            deg[u] += 1
            deg[v] += 1
        if any(deg[i] != r + 1 for i in range(n)):
            return False
    return len(E) == n * (n - 1) // 2


def main() -> None:
    random.seed(0)
    print("one-factorization nested:", {n: one_factorization_nested_ok(n) for n in (6, 8)})

    # n=6 is already heavy combinatorially for full enumeration of all degrees;
    # n=4,6 are feasible.
    for n, d in [(4, 1), (4, 2), (6, 1), (6, 2), (6, 3)]:
        try:
            res = analyze(n, d)
        except MemoryError:
            print(f"n={n}, d={d}: memory error")
            continue
        print(res)


if __name__ == "__main__":
    main()
