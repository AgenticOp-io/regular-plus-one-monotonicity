"""Enumerate hosts where N_1(residual) varies with the peeled matching. Workshop only."""

from __future__ import annotations


def all_edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def perfect_matchings(n: int) -> list[frozenset[tuple[int, int]]]:
    out: list[frozenset[tuple[int, int]]] = []

    def rec(remaining: list[int], acc: list[tuple[int, int]]) -> None:
        if not remaining:
            out.append(frozenset(acc))
            return
        a = remaining[0]
        for b in remaining[1:]:
            rec(
                [v for v in remaining if v not in (a, b)],
                acc + [(min(a, b), max(a, b))],
            )

    rec(list(range(n)), [])
    return out


def main() -> None:
    n = 6
    edges = all_edges(n)
    idx = {e: i for i, e in enumerate(edges)}
    pms = perfect_matchings(n)
    pm_masks = []
    for pm in pms:
        m = 0
        for e in pm:
            m |= 1 << idx[e]
        pm_masks.append(m)
    print(f"perfect matchings={len(pms)}")

    multi = 0
    vary = 0
    for host in range(1 << len(edges)):
        contained = [pm for pm in pm_masks if pm & host == pm]
        if len(contained) < 2:
            continue
        multi += 1
        vals = []
        for g in contained:
            residual = host & ~g
            n1 = sum(1 for pm in pm_masks if pm & residual == pm)
            vals.append(n1)
        if max(vals) != min(vals):
            vary += 1
    print(f"hosts with >=2 PMs: {multi}")
    print(f"hosts with varying N_1(R): {vary}")


if __name__ == "__main__":
    main()
