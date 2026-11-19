# r21a: numerical check of c(D)=(D-2)/D  (MEASURED, exact counts; not proved)
Quantity: c_n(D) = Delta(P3) - 2 Delta(e) = D2 log Q, Q(H)=P(pairing simple | host H) = g(H) prod(D-h_v)!/(N-2L-1)!! (r17a identity),
g(H) = exact # simple D-regular labelled graphs containing H, from the degree-type DP + inclusion-exclusion (r5w3_exact.contains).
Scripts: v2/scripts/r21a_cD.py (data -> r21a_out_D{3,4,5,6}.txt), r21a_fit.py (extrapolation), r21a_u.py (side check). Reproduces r17a D=3 n=8..14 to all printed digits.

## Data (n*c_n)
D=3 n=20..100: .3916 .3709 .3610 .3553 .3515 .3469 .3441
D=4 n=20..100: .5685 .5443 .5327 .5259 .5215 .5160 .5127
D=5 n=20..60 : .6732 .6473 .6350 .6277 .6230
D=6 n=12..40 : .8008 .7635 .7424 .7288 .7157 .7071 .7029
Fit n*c = a + b/n (+ c2/n^2) on the largest points:
| D | a (2-term / 3-term) | (D-2)/D | b |
| 3 | .3333 / .3332 | .3333 | ~1.07 |
| 4 | .4999 / .4997 | .5000 | ~1.27 |
| 5 | .6000 / .5999 | .6000 | ~1.34 |
| 6 | .6667 / .6666 | .6667 | ~1.38 |
Agreement to 3-4 digits for D=3..6, n up to 100 (D=3,4), 60 (D=5), 40 (D=6). The earlier "~0.31" at D=3 was an under-extrapolation from n<=14 (1/n correction b~1 is large).
So c(D)=(D-2)/D is **numerically confirmed** for D=3,4,5,6 as the leading 1/n coefficient; the 1/n^2 remainder is visible (b/n^2, b~1-1.4, growing slowly with D) but only fitted, not bounded in D.

## Reconciling r20a's -0.11/n
r20a's first-order value "-1/(nD) = -0.11/n at D=3" is an arithmetic slip: 1/(nD) at D=3 is 0.333/n (0.11 = 1/D^2). With that fixed, the first-order Poisson value (D-2)/(nD) = 0.333/n at D=3 matches the exact data (and r20b's own formula). The "-0.31 exact" in r20a is the same r17a/r16w1 number as our n*c (~.31 at small n -> .333 asymptotically); the sign difference is a convention of the Ursell difference (not re-derived here; r21a_u.py shows the raw graph-level D2 log g tends to -log(D/(D-1)) + c - 2/N-type pieces, consistent with c above, but I did not re-match r16w1's exact sign convention).
Hence the "factor ~3 first-order failure" does NOT exist: it was an arithmetic error, and the doubt it cast on r20b should be withdrawn (for the adjacent-pair coefficient). The k=4 remark in r20a (first order contributes zero for non-star T) is unaffected and not tested here.

## Status
Measured: c(D) for D=3..6 (above). Proved: nothing new. Still open: rigorous derivation, O(D^b/n^2) remainder, uniformity in D, behaviour for L>=4.
