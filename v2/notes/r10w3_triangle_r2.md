# r10w3: triangle second-order estimate r2(D) -- NOT proved; numerics; assembly of exp-form Thm 6

Labels: PROVED / NUMERIC / OPEN. main.tex untouched. Script: `v2/scripts/r10w3_fit.py` (numpy, seconds; reuses r9w3_tri/cross formulas and r7_data).

## Status of Theorem 6 (exp form), two-sided star hosts
- PROVED (r8w3): one-sided j-stars, c0=(j+1)^2/2+O(1/D) (j<=4 symbolic).
- PROVED (r9w3, given r1=3(D-1)/D): S1_1_0, c0=(9D^2-50D+45)/(2D^2) <= 9/2, uniform in D, no r2 needed.
- PROVED (exact reduction): S1_1_1 c0 = r2(D) - 9/2 - 15/D + 67/(2D^2).
- OPEN: r2(D) = n^-2 coefficient of E[#triangles in G(n,D)] / ((D-1)^3/6). I could not derive or bound it: it needs the second-order
  switching/saddle expansion (not in Gao20, McKay-Wormald-Wysocka give only n^-1). No exact computation of the triangle host term was obtained:
  vertex-transitivity gives no closed form for E[T] (T is not fixed-count), and the only exact source is the r7 DP (n<=24..80), i.e. the same data.
- OPEN: r1=3(D-1)/D itself is forced by requiring the n^-1 term to vanish, not independently proved (it IS consistent with S1_1_0 data, r9w3 cross-check).
So the exp-form Thm 6 is assembled only for hosts with w=0 and j,k<=1 (S1_1_0) plus one-sided stars; every host with a common neighbour
and every j,k>=2 two-sided host still needs r2 (and diamond counts for j,k>=2) -- exactly the item (a)+(b) of r9w3 sec 2.

## NUMERIC: r2(D) from S1_1_1 (r2 = (2D^2 c0 + 9D^2 + 30D - 67)/(2D^2), c0 fitted n^2*err = c0+c1/n+c2/n^2)
D=3..10: 3.78, 5.25, 6.25, 6.96, 7.54, 8.00, 8.40, 8.78.
Robustness (drop 2/4 smallest-n points): D<=7 moves <=0.1; D=8: 8.00/7.92/8.35; **D=9: 8.40/8.01/5.75, D=10: 8.78/9.29/5.67** -- D>=9 values are NOT reliable
(too few n, n<~D^2). Use D<=8 only.
Shape fits on D=5..10 (a+b/D+c/D^2): a=12.51, b=-43.7, c=62.1 (rms .013); adding 1/D^3: a=13.9 (rms .007).
Hold-out: D=3,4 predicted 4.83/5.46 vs data 3.78/5.25 (deg 2) -- the polynomial-in-1/D form does NOT extrapolate down to D=3 (D=3 off by 1.0).
=> a=25/2 is consistent with the data but the limit a is not determined (13.9 vs 12.5 with equally good fits); boundedness of r2 is NOT decided.
Constant extraction: best statement is r2(D)=O(1) numerically for D<=8 (monotone, increments 1.0,.71,.58,.46,.40 shrinking, consistent with bounded or log).

## NUMERIC: does c0 -> (j+k+w+1)^2/2 generalize? (all 130+ star hosts, D=5..10, free 3-parameter fit in 1/D)
One-sided (proved) reproduced: free a = 2.01, 4.55, 8.24 vs 2, 4.5, 8 (S0_1/2/3_0 and S1/2/3_0_0 identical by symmetry).
Two-sided: free a vs L: S1_1_0 4.33/4.5, S1_1_1 7.72/8, S1_2_0 7.61/8, S1_2_1 11.63/12.5, S2_2_0 11.58/12.5, S2_2_1 16.40/18, S2_2_2 21.66/24.5,
S3_2_2 28.9/32, S3_3_0 22.5/24.5, S3_3_2 37.4/40.5. Free a is systematically BELOW L by 4-12% and the gap grows with host size and D-window bias
(hosts need n>>D^2, data has n<=24..44 at D>=7). Pinned-at-L fits cost rms .01-.12.
Verdict NUMERIC: c0 <= (j+k+w+1)^2/2 plausible (never exceeded beyond fit noise except S1_5_1, S1_4_x with 4 D-points); equality NOT established; no growth seen. OPEN.

## Next step (what would close it)
Second-order switching estimate for T: E[T]=(D-1)^3/6(1+r1/n+r2/n^2) via configuration-model count of triangles with simple-graph conditioning
(P(simple)'s n^-2 term, McKay 1985 expansions) -- or exact transfer-matrix E[T] at D=3,4 for n up to ~200 to nail r2(3), r2(4) and test r2 formula guesses.
