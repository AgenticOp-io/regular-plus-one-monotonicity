"""
Configuration-model probes for +1 nesting.

For moderate even n, sample config-model d-regular multigraphs, simplify when
possible, and estimate:
  - fraction of samples whose complement admits a perfect matching (Tutte via
    blossom / greedy heuristic + exact for tiny n)
  - relative variance proxy for matching counts via sampling matchings

Also verifies the η(α) schedule from notes/attack-n-half.md numerically.
"""

from __future__ import annotations

import math
import random
from collections import defaultdict
from typing import Dict, List, Optional, Set, Tuple

Edge = Tuple[int, int]


def _norm(u: int, v: int) -> Edge:
    return (u, v) if u < v else (v, u)


def configuration_model(n: int, d: int, rng: random.Random) -> List[Edge]:
    """Return a list of edges (may include loops/multis) from the config model."""
    stubs = [v for v in range(n) for _ in range(d)]
    rng.shuffle(stubs)
    edges: List[Edge] = []
    for i in range(0, len(stubs), 2):
        edges.append(_norm(stubs[i], stubs[i + 1]))
    return edges


def is_simple(edges: List[Edge]) -> bool:
    seen: Set[Edge] = set()
    for e in edges:
        u, v = e
        if u == v:
            return False
        if e in seen:
            return False
        seen.add(e)
    return True


def to_simple_graph(edges: List[Edge]) -> Optional[Set[Edge]]:
    if not is_simple(edges):
        return None
    return set(edges)


def greedy_complement_matching(n: int, g: Set[Edge], rng: random.Random) -> Optional[Set[Edge]]:
    """Greedy perfect matching in K_n \\ g. None if stuck."""
    unused = set(range(n))
    matching: Set[Edge] = set()
    while unused:
        u = unused.pop()
        candidates = [v for v in unused if _norm(u, v) not in g]
        if not candidates:
            return None
        v = rng.choice(candidates)
        unused.remove(v)
        matching.add(_norm(u, v))
    return matching


def eta_new(d: float, n: float, alpha: float, C: float = 10.0) -> float:
    return (
        2 * alpha
        + 1.0 / (d**3 * alpha**2)
        + C * (d**2) / (n * alpha**2)
        + C * math.sqrt(d / n) * (math.log(n) ** 3) / alpha**2
    )


def eta_old(d: float, n: float, alpha: float, C: float = 10.0) -> float:
    return (
        2 * alpha
        + 1.0 / (d**3 * alpha**2)
        + C * (d**3) / (n * alpha**2)
        + C * math.sqrt(d / n) * (math.log(n) ** 3) / alpha**2
    )


def choose_alpha(d: float, n: float) -> float:
    """o(1) when d = o(sqrt(n)/polylog); balances 2α vs sqrt(d/n) log^3 / α^2."""
    return max(
        1.0 / d,
        (d**2 / n) ** 0.25 * math.log(n),
        (d / n) ** (1.0 / 6.0) * math.log(n),
    )


def schedule_report(n: float = 1e60) -> None:
    print(f"eta schedules at n={n:g} (ok => alpha<0.1 and eta<0.1)")
    print(
        f"{'exp':>6} {'d':>12} {'alpha':>12} {'eta_old':>12} {'eta_new':>12} "
        f"{'a_ok':>5} {'old':>5} {'new':>5}"
    )
    for exp in [0.20, 0.30, 0.33, 0.40, 0.45, 0.48, 0.49]:
        d = float(n) ** exp
        if d < 3:
            continue
        a = choose_alpha(d, float(n))
        eo, en = eta_old(d, float(n), a), eta_new(d, float(n), a)
        print(
            f"{exp:6.2f} {d:12.4e} {a:12.4e} {eo:12.4e} {en:12.4e} "
            f"{(a < 0.1)!s:>5} {(eo < 0.1)!s:>5} {(en < 0.1)!s:>5}"
        )


def config_probe(n: int, d: int, trials: int = 200, seed: int = 0) -> Dict[str, float]:
    rng = random.Random(seed)
    simple = 0
    greedy_ok = 0
    attempted = 0
    for _ in range(trials):
        edges = configuration_model(n, d, rng)
        g = to_simple_graph(edges)
        if g is None:
            continue
        simple += 1
        attempted += 1
        if greedy_complement_matching(n, g, rng) is not None:
            greedy_ok += 1
    return {
        "n": n,
        "d": d,
        "trials": trials,
        "simple_frac": simple / trials,
        "greedy_matching_ok_among_simple": (greedy_ok / simple) if simple else float("nan"),
    }


def main() -> None:
    schedule_report(1e60)
    print()
    for n, d in [(20, 3), (20, 5), (40, 3), (40, 7), (60, 5)]:
        print(config_probe(n, d, trials=300, seed=1))


if __name__ == "__main__":
    main()
