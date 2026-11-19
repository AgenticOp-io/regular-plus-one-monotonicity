# r16w2: conditioning on assortativity as a repair of lem:avoid-G-host (pairing level only)

Script: v2/scripts/r16w2_cond_cross.py (run `python -W ignore v2/scripts/r16w2_cond_cross.py 100 200 400` from repo root).

## Setup (exact)
Two-type host: n/2 cells of degree delta+t, n/2 of delta-t; factor degree D=delta-m, residuals r=m+-t.
Pairing edges y_i y_j sum: Lambda = t^2 (#pairs - 2x), x = number of cross (P-Q) pairs. So for two types
**conditioning on Lambda == conditioning on x**, and E[Z|x], E[Z^2|x] are exactly computable:
count (S1,S2) by overlaps (B+,B-) (pi_P, pi_Q = convolutions of hypergeometrics), then the four classes pair
internally with W(a,b,x)=C(a,x)C(b,x)x!(a-x-1)!!(b-x-1)!! cross-pairings; convolve in x.
R(x) = Wtot(x) * sum_{B+,B-} pi_P pi_Q [conv_x of 4 class W] / [conv_x of 2 class W]^2.
Validation: summing over x reproduces r4w2 log_ratio (n=100: 1.988 vs 1.988; 200: 3.986/3.987; 400: 7.976/7.984).

## Result  (delta=40, m=6, t=3; log R(x | x) at x = mean; flat in x within +-2sd, moves ~0.01)
| n   | unconditioned | conditioned on Lambda |
| 100 | 1.99          | 0.074 |
| 200 | 3.99          | 0.136 |
| 400 | 7.98          | 0.241 |
(regular host ~0.013). t-dependence at n=200: t=2: 0.81 -> 0.035; t=3: 3.99 -> 0.136.
So conditioning removes ~97% of K (slope in n drops 0.020 -> 0.0006) **but the conditioned log-ratio still grows
linearly in n** (increments 0.062, 0.105). Conditioning on Lambda alone does NOT make it bounded; it does push the
blow-up to n >~ 1/6e-4 ~ 2000 at these parameters. Residual ratio t=2->3 is 5.6x (t^4 gives 5.06x): looks like a
second-order term ~ n s2^4 * small constant (unproven; maybe a second host statistic, e.g. sum_{ij} y_i^2 y_j^2).

## Verdict
* Suggested repair (condition on Lambda): leading-order K removed (consistent with r4w2 Sec 8), but a residual
  linear-in-n term remains at pairing level. Not a true bounded-ratio lemma on the window, as far as computed.
* Sharpest true statement available: pairing-level R = exp(K+o) uncond (r15w1); conditioned on Lambda, R = exp(c n s2^4 / ...)
  with c ~ 1/30 of K at t=3 (numerical only). hyp:s3-avoid-G would need conditioning on further statistics
  (higher assortativity moments) or a window with K_cond = o(1) -- or abandoning the variance route for a
  direct TV/small-subgraph-conditioning argument.

## Proved / numerically checked / not checked
* Proved: nothing new. (Lambda is a function of x for two types: trivial identity.)
* Numerically checked: exact conditional ratio table above; unconditional agreement with r4w2.
* NOT checked: t=4,5 conditional values are unreliable (windowing truncation; t=5 gave R<1, impossible, t=4 likely
  biased) -- only t=2,3 trusted; n=800 not run (slow); non-two-type hosts (continuous y; Lambda then not a
  function of one count); simple-graph transfer (McKay) -- item 3 (independent re-derivation of McKay's estimate)
  NOT done; the second-order mechanism is a guess.
