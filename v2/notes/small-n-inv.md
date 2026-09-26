# Small-n inverse-count gap

## Exact: n=6, D=2

Via `v2/scripts/_small_n_inv.py`.

|Ω₂| = 60 (C₆) + 10 (C₃∪C₃) = 70.

| p | E[1/N|C₆] | E[1/N|C₃∪C₃] | ratio |
|---|-----------|---------------|-------|
| 1/4 | 0.72041447 | 0.66523446 | 1.08295 |
| 1/3 | 0.56823917 | 0.50904796 | 1.11628 |
| 1/2 | 0.29623897 | 0.25733183 | 1.15119 |
| 2/3 | 0.12227463 | 0.10968909 | 1.11474 |
| 3/4 | 0.07264160 | 0.06772858 | 1.07254 |

## Monte Carlo: n=8, D=2

Via `v2/scripts/_small_n8_inv.py` (2000 trials, p=1/2, seed 0).

|Ω₂| = 2520 (C₈) + 672 (C₅∪C₃) + 315 (C₄∪C₄) = 3507.

| type | E[1/N]≈ | ratio to C₈ |
|------|---------|-------------|
| C₈ | 0.044390 | 1 |
| C₅∪C₃ | 0.039835 | 1.114 |
| C₄∪C₄ | 0.043470 | 1.021 |

Recorded in the manuscript as Remark `rem:small-n-inv`.
Not a conjecture close: shows iso-type flatness is nontrivial already at n=6.
