# Experiment log

Command: `python src/experiments.py`

## Results

| n | d | #G(n,d) | #G(n,d+1) | extendible | TV(G⊕unif M vs G(n,d+1)) |
|---|---|--------:|----------:|----------:|--------------------------:|
| 4 | 1 | 3 | 3 | 100% | **0** |
| 4 | 2 | 3 | 1 | 100% | **0** |
| 6 | 1 | 15 | 70 | 100% | **0.143** |
| 6 | 2 | 70 | 70 | 100% | **0.057** |
| 6 | 3 | 70 | 15 | **85.7%** | 0 (on support) |

## Interpretation

1. **Lemma C is sharp:** at \((n,d)=(6,3)\), not every 3-regular graph extends by a complementary perfect matching (extendible fraction < 1). Any coupling must fail on that positive fraction *or* use a different \(H\) law — but if \(H\) is exactly uniform \(G(n,4)\), those non-extendible \(G\) cannot appear as subgraphs. So a successful coupling must bias away from non-extendible \(G\), or the event \(G\subset H\) fails with probability bounded below on a naive product space.

2. **Lemma D is sharp:** already at \(n=6\), uniform matching in the complement does **not** produce uniform \(G(n,d+1)\) (TV ≈ 0.06–0.14). TV→0 as \(n\to\infty\) is exactly conjecture (★).

3. **Tiny \(n\) can be exact:** \(n=4\) accidentally has TV=0.

## Next experiments

- Importance-sample configuration model for \(n\le 20\), \(d\le 5\), estimate TV empirically.
- Count extendible fraction vs \(d\) for enumerated \(n=8\) (may be slow; use nauty/geng if installed).
