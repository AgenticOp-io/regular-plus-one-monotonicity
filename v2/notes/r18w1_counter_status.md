# r18w1: exact u_T for D=3 paths to n=240 (P6 to 640); P6 changes sign, slope -> ~3

## What was done
No new counter was needed. The existing r5w3_exact.contains (degree-count-state DP + inclusion-exclusion) is already polynomial
for D=3: P6 at n=28 takes ~0.15 s (the r17 "too slow" came from float/small-n use, not the DP). New driver
scripts/r18w1_big.py: same contains(), logs taken in 80-digit Decimal (the alternating sum cancels ~n^-k out of O(1) logs, so floats fail at large n).
Validated: only that it reuses contains() unchanged and reproduces r16_longpath.py floats at n=28 (P3..P6 u agree to printed digits, e.g. P6 n=28 u=-1.98e-05).
NOT independently validated against a second counter or brute force here (the n<=28 "match" is the same code path with higher precision).
Runtimes: ~10 s per shape up to n=240; P6 n=320/480/640: 33 s / 110 s / 375 s. Exact integers throughout; only the final logs are 80-digit decimal.
Data: scripts/r18w1_out_*.txt, slopes: scripts/r18w1_slopes.txt (r18w1_slopes.py).

## Results (D=3, local slope = -dlog|u|/dlog n)
- 2e: slope 1.00, n u at 240 = 0.668: n^-1.
- P3: slope 0.99 at 160->240, n u = -0.331: n^-1, flat.
- P4: slope 2.01, n^2 u = -0.7835 (slowly drifting down, 0.82 -> 0.78): n^-2.
- P5: slope 3.03 at 160->240 (was 3.2 at n<=28, decreasing monotonically to 3); n^3 u = -2.54 still drifting (-3.23 -> -2.54).
  Consistent with n^-3 = n^-(k-2) with a slow correction; limit not pinned down.
- P6: u NEGATIVE up to n=120, ZERO crossing between 120 and 160, POSITIVE after: u = +2.49e-9 (160), 2.35e-9 (240), 1.32e-9 (320),
  4.86e-10 (480), 2.25e-10 (640). Local slope 240->320: 2.0, 320->480: 2.5, 480->640: 2.7 (increasing).
  The earlier "4.6 stable" reading was pre-asymptotic: it is a negative n^-4.6-ish term overtaken by a positive term.
  n^4 u is NOT flat (it grows positive). n^3 u at 640 = +58.9, at 480 = +53.8, at 320 = +43.3: still rising, so the slope has not reached 3 or is above 3 limit is unclear;
  data are compatible with a positive n^-3 term (the r17 heuristic count for P6) but do not prove it; no exponent claimed.
- Disjoint shapes P2+P2, P3+e (k=4): slope 1.95 at 160->240, n^2 u -> -0.21 (still creeping, both nearly identical): n^-2 plausible, not claimed.

## Verdict
n^(k-2) u flattens (slowly, from above in |.|) for k=3,4; for P5 it is still drifting (slope 3.03). P6 exhibits a sign change, so any
"u_T has fixed sign / exponent from n<=28 slopes" reading is wrong at k=6; asymptotics need n>>640 or analytic second-order cumulants.

## r19 validation
scripts/r19_validate.py: brute-force labelled cubic graphs n=6,8 (counts match Nseq) vs contains() for P3..P6,2e,P3+e: all match. Counter now independently validated at small n (not at large n).
