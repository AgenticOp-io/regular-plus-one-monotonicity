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

## Exact triangle bias n=6, D=2

Fixed T on vertices 0,1,2: |Omega_T|=1, mu=1/70.
nu/mu = a(C3+C3)/a_bar (Corollary subgraph-bias), matched by direct host enumeration.

| p | nu/mu |
|---|-------|
| 1/4 | 0.933621 |
| 1/3 | 0.909366 |
| 1/2 | 0.885273 |
| 2/3 | 0.910459 |
| 3/4 | 0.941463 |

Script: v2/scripts/_small_n_triangle.py

## a(G0) vs target c_n (n=6, D=2)

c_n = P(N>=1)/(|Omega| p^6). Identity: a_bar = c_n exactly.

| p | a_C6/c_n | a_tt/c_n | a_bar/c_n |
|---|----------|----------|-----------|
| 1/4 | 1.0111 | 0.9336 | 1.0000 |
| 1/3 | 1.0151 | 0.9094 | 1.0000 |
| 1/2 | 1.0191 | 0.8853 | 1.0000 |

Item (iii) fails on this finite instance: types disagree with c_n, average matches.

## Weighted lower-tail vs pointwise (n=6, D=2, p=1/2)

\(M=1/c_n\approx 3.44\). Exact complement enumeration:

| type | \(a\) | \(\PP(N<M)\) | \(\int_1^M\PP(N<u)/u^2\,du\) | int/\(c_n\) |
|------|------:|-------------:|------------------------------:|-----------:|
| C₆ | 0.296 | 0.334 | 0.030 | 0.103 |
| C₃∪C₃ | 0.257 | 0.330 | 0.018 | 0.063 |

Pointwise mass \(\sim c_n\); weighted integral \(\sim 0.1\,c_n\). Remark
`rem:iii-weighted-n6`. Criterion still fails as \(o(c_n)\) on this instance.

## Switch connectivity on Omega_2

The 2-switch graph on all 70 simple 2-regular graphs is connected.
Each C6 has 3 switches to a C3+C3.
At p=1/2, a differs by relative factor 1.151 across such a switch edge.
So switch connectivity does not flatten a.

## Tilt comparison for Delta = K12-K012 (n=6, D=2, p=1/2, G0=C6)

Summation over Omega_2 x Omega_2:
- E_mu[p^{-Delta}] = 3.69653...
- E_tilt[p^{-Delta}] = 2.03587...
- tilted/untilted ≈ 0.55075

The p^{-K01-K02} tilt *decreases* the pairwise factor on this instance.
