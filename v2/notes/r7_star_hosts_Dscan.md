# r7: is the exp-form n^-2 coefficient D-uniform for hosts touching u or v?  (D up to 10)

Labels: **numerical** only. Nothing here is proved. main.tex untouched.

## Method (new, `v2/scripts/r7_star.cpp`, driver `r7_run.py`, fits `r6_fit.py`/`r7_fit.py`/`r7_extrap.py`)
Hosts: star at u with j leaves, star at v with k leaves, w common leaves (name `S{j}_{k}_{w}`; Delta=max(j,k)); this is every host that
touches only u,v (|H1|=j+k up to 2D-2). Key reduction: remove u,v; the ensemble of G is then a sum over the other neighbours Y,Z' of u,v of
graphs on n-2 vertices with a **near-regular sequence** (residual degrees D, D-1, D-2). The count is a sum of O(D^3) terms of the class-count DP
N(c) (as in r5w3), with NO inclusion-exclusion over host edges; all DP terms are positive, so C++ doubles are exact enough
(N normalised by (M-1)!! to stay in (0,1]). Reachable DP states are few (16k at D=6,n=24), which is why D=10 is feasible.
Check: reproduces the r6 exact engine to all printed digits (D=4 n=24: edge_at_u .46873, common_nb -.86816, edge_at_both -.10985, star_both3 -5.48923).
Data `notes/r7_data/d{3..10}.txt`, columns `D host n n^2*err_prod n^2*err_exp`. Reach: D=3 n<=80, D=4 n<=60, D=5 n<=44, D=6 n<=44, D=7 n<=36, D=8 n<=32, D=9 n<=28, D=10 n<=24.
Limits: only star-type hosts (not far parts of H1, no host edges between leaves); n is small relative to D^2 for D>=8, so c0 fits are biased
(D=7: shrinking the fit window from n<=36 to n<=24 moves c0 by 0.07 (S1_1_1) and 0.35 (S3_3_3); expect >=0.3-0.5 at D=9,10).

## Result: c0(D) of the exp form (fit n^2*err = c0 + c1/n + c2/n^2)
| host | D=3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|
| S1_0_0 edge at u | 0.00 | .38 | .64 | .83 | .98 | 1.09 | 1.19 | 1.26 |
| S3_0_0 star 3 at u | - | .13 | 1.05 | 1.85 | 2.53 | 3.08 | 3.54 | 3.93 |
| S1_1_1 common nbr | -2.00 | -.91 | .09 | .89 | 1.58 | 2.15 | 2.65 | 3.11 |
| S2_2_0 | -4.38 | -2.72 | -.90 | .64 | 1.91 | 2.92 | 3.71 | 4.33 |
| S3_3_0 | - | -5.48 | -3.09 | -.52 | 1.96 | 3.88 | 5.41 | 6.54 |
| S3_3_3 (u,v same 3 nbrs) | - | -9.95 | -7.90 | -4.79 | -1.47 | 1.85 | 5.25 | 9.04 |
(far hosts stay at 0.50, D-independent: r6.)

## Verdict: NOT D-uniform in the naive sense; boundedness itself is UNDECIDED
- c0 is **not** D-free: for every host touching u or v it keeps changing with D through D=10 (far hosts: constant 1/2).
  So "same constant as far hosts" is false (**numerical**, robust: effect far larger than the fit bias).
- One-sided hosts (star at u only): increments of c0 shrink like ~7/D^2 (S1_0_0: rational fit a+bD/(D+1.5), rms .003, limit ~2.1). Looks saturating,
  consistent with a rational function of D and with the O(1+Delta^2) form (**numerical**, extrapolation, not a proof).
- Two-sided hosts: S1_1_1 (Delta=1) rises 0.09 -> 3.11 (D=5..10) with increments ~4.4/D; a+b ln D (b=4.35, rms .009) fits as well as a saturating
  rational (limit ~10, rms .007). The data cannot distinguish log growth from saturation. S3_3_3 (Delta=3, u and v share all neighbours,
  d~=D-3) is the worst: -7.9 .. 9.0, increments still growing at D=10 (no saturating fit; fit bias there is largest). 
- So at Delta=1..3 and D<=10, |c0| <= 9 ~ (1+Delta^2) = 10 is not violated, but the D-dependence at fixed Delta is strong and unresolved.
  I can neither confirm "error <= C(1+Delta^2)/n^2 with C independent of D" nor refute it. A true D-uniform statement, if it holds, has a large constant
  (ten-ish at Delta=3) rather than the 1/2 of far hosts; if c0 ~ ln D (S1_1_1) the claim fails mildly (log D/n^2), which would not break the n^{1/4} budget
  but would need the exp-form error stated as O((1+Delta^2) log D / n^2).
- Product form is worse (c0 ~ D^2-ish, 49-130 at D=7..10), as before.

## Not done
Far parts of large H1 combined with u,v stars; D>10 or n>>D^2 (needs the actual second-order switching/saddle-point formula, which would settle log-vs-bounded:
coefficients are rational in D, so S1_1_1's c0(D) should be a rational function; D=3..10 gives 8 points, enough to test a degree<=3/3 rational guess -- not attempted).
