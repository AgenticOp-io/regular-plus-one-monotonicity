# r15w1: lem:avoid-G-host (Hypothesis hyp:s3-avoid-G) is FALSE on the window W_{eta_n}

## Verdict
The hypothesis "Var_g Z <= eps_n (E_g Z)^2 uniformly for g in W_{eta_n}" is false in regime (B),
already for G = empty (so H uniform simple graph with degree sequence g), and for any
non-constant-ish g. Not a missing proof: a pairing-level exact blow-up (r4w2 Prop 1-3, re-used here
with roles swapped: factor degree m, host mean degree delta).

## Mechanism (r4w2, notes/r4_worker2_hosts.txt, Prop 1-3 and Thm 5)
Host degrees g_v = delta + y_v, s2^2 = (1/n) sum y_v^2. The overlap of two independent m-subgraph
choices has mean shifted from the minimiser S* of the pair-closure weight f by
Delta = n (delta-m)^2 s2^2/ delta^3 ... and
  log(E_pair Z^2/(E_pair Z)^2) ~ K = n (delta-m)^2 s2^4 / (2 m^2 delta^3) ~ n s2^4/(2 m^2 delta).
(Here r = m, "D" = delta-m; swapping roles in r4w2's K = n D^2 s2^4/(2 rho^2 hbar^3).)
Transfer to simple graphs costs only exp(O(delta^2)) (McKay as quoted in main.tex, r4w2 Thm 5),
and K >> delta^2 in (B).

## Why this kills the hypothesis
W_{eta_n} allows |y_v| <= sqrt(6 delta log n) >> sqrt(delta), i.e. every typical G(n,p)-type
sequence, s2^2 ~ delta: K ~ n delta/(2 m^2) = Theta(n d^{-1/3}...) -> infinity (m^2 = d log n,
delta = d^{2/3}(log n)^{1/3}, d = o(n^{3/8})).  Even |y_v| = 1 for all v (s2 = 1) gives
K ~ n/(2 m^2 delta) = n/(d^{5/3} polylog) -> infinity.  So the hypothesis fails for every g
with s2^4 >> m^2 delta / n, i.e. all but essentially-regular g.  It holds (pairing-exactly, Thm 6)
only when K = o(1): s2^2 = o(m sqrt(delta/n)) -- far narrower than W.

## Numerics (v2/scripts/residual/r15w1_pairing_check.py; exact pairing ratio, half +t half -t)
 delta=40 m=6 t=3: log ratio n=200..1600 = 3.99, 7.98, 15.98, 31.97 (K formula 4.06 at n=200); regular 0.013
 delta=40 m=6 t=5: 29.96, 59.9, 119.9, 239.9 (formula 31.4 at n=200); regular 0.013
 delta=60 m=8 t=6: 24.2, 48.4, 96.7, 193.5; regular 0.009
Exactly linear in n, regular host stays O(1).  (K printed by the script uses unswapped roles and is
wrong; use the formula above.)

## Consequences
* Step 3 item (ii) (degree-conditioned concentration) is vacuous/false as stated at width eta_n; with
  window shrunk to K=o(1) it is true but G(n,p) puts probability e^{-Theta(n)}-ish there.
* Repair must condition on a further host statistic (assortativity Lambda = sum_{ij in H} y_i y_j,
  r4w2 Sec 8, unproven) -- exponent beta^2 Var Lambda = K matches exactly.
* Note: this is only a variance statement; it does not show Z/E Z fails to -> 1 in probability.

## Honest status
Proved at pairing level (exact numerics + r4w2 propositions); simple-graph disproof conditional on
McKay's estimate as quoted in main.tex and on r4w2 Thm 5's window argument (not re-derived here;
Gaussian formula is ~10% accurate). No simple-graph computation was run. Hypothesis proof: impossible.
