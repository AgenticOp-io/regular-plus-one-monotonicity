# r37: weak law Z/E[Z | G, deg R = g] -> 1 ?  Answer: FALSE (sketch), small-subgraph conditioning / truncated 2nd moment not needed

Status: no proof of lem:avoid-G-host in any form. One rigorous lemma, one sketched disproof of the weak law
as stated, one corrected arithmetic slip in r33. Nothing edits main.tex.

## 1. Rigorous: weak law <=> total-variation closeness to the planted law
X := Z/E Z >= 0, E X = 1, P* (dP*/dP = X) the Z-weighted ("planted") law of H.
TV(P,P*) = E(1-X)_+ . Since 0 <= (1-X)_+ <= 1, bounded convergence gives
  X -> 1 in probability  <=>  TV(P,P*) -> 0.
(No uniform integrability needed.) So the weak law is a statement about distinguishing H from a planted H.
Hence a statistic Q(H) whose planted mean is >> its null s.d. (with comparable planted s.d.) kills the weak law:
TV >= 1 - O(1/z^2) by Chebyshev, and then X -> 0 in probability (E Z is carried by rare H).

## 2. Sketch: such a statistic exists, Lambda(H)=sum_{uv in H} y_u y_v, with z = sqrt(K)
Setting: pairing model, host degrees h_v = hbar+y_v (sum y=0, s2^2 = mean y^2), factor degree D (=m), rho=hbar-D.
Planted pairing (the second-moment object of r4w2 Prop 1): choose r_v=h_v-D points per cell, pair them uniformly
among themselves, pair the other D points per cell among themselves.
Exact means (uniform pairing on points with weights w: E sum_pairs w_i w_j = ((sum w)^2 - sum w^2)/(2(M-1))):
  null:    sum_i w_i = n s2^2,  -> E0 Lambda ~ n s2^4/(2 hbar)
  planted: R part n s2^4/(2 rho), F part ~0 (sum D y = 0)
  shift  = n s2^4 D /(2 rho hbar).
Null variance (Chung-Lu level) sigma^2 ~ (n hbar/2) s2^4. Therefore
  shift^2/sigma^2 = n D^2 s2^4 /(2 rho^2 hbar^3) = K   (the r4w2 constant),
i.e. the planted law is a mean shift of sqrt(K) null s.d. in Lambda: log-LR ~ beta*Lambda, beta = D/(rho hbar^2),
exactly the "Gaussian shift experiment" with E Z^2/(E Z)^2 = e^K. When K -> infinity: TV -> 1, X -> 0 in prob.
Numerics (v2/scripts/r37_shift.py, 1500 pairings each, two-type host y=+-t):
  n=2000 D=6 t=6: sqrtK 0.79, z 0.76, sd*/sd0 1.02
  n=2000 D=6 t=9: sqrtK 1.79, z 1.84, sd*/sd0 0.96
  n=4000 D=6 t=9: sqrtK 2.53, z 2.59, sd*/sd0 0.99
So z = sqrt(K) and the variance is unchanged, as the sketch predicts. (Only K<=6.4 reachable by MC; the K->infinity
claim is extrapolation of an exact formula, not simulated.)
Consequence (conditional on this sketch + transfer to simple graphs, neither proved):
 * Theorem residual-moment-bim-proof (ii) [Var(Z|G,deg R=g) <= eps (E Z)^2] cannot hold, and the weak-law form
   Z/E[Z|G,g] -> 1 fails too: it must be normalised by E[Z | G, g, host statistics].
 * This explains why "variance route" and "weak-law route" give the same answer here: there is no rare-overlap
   rescue. The typical overlap carries the e^K (r4w2: shift Delta ~ n puts the typical pair at f = e^K), so the
   second moment is dominated by typical pairs, i.e. by the Lambda-fluctuation of the host, not by a rare event.
   (r33's worry that the second moment might be dominated by a rare overlap is thereby answered: no.)

## 3. Why SSC / truncated second moment were not run
Both prove X -> 1 (or X -> W). For this X the answer is X ~ W = exp(beta Lambda - K/2) (log-normal, log-variance K),
so SSC *does* apply, but with the host statistics in place of cycle counts, and it yields X/W -> 1, not X -> 1.
Truncating the second moment to typical pairs removes nothing, since the typical pair already has f = e^K.
The right repaired target: Z / E[Z | G, g, Q(H)] -> 1, Q = joint-degree edge-count matrix e_H(class a, class b).
For a two-type host the cross kernel has dimension 3 - 2 = 1, so Q = Lambda up to degree-determined terms.

## 4. Correction to r33
r33_K_formula.py / r33_step2.md use K = n(delta-m)^2 t^4/(2 m^2 delta^3) "with m = factor degree". The exact
values 3.99 / 29.96 reproduce (my run: 3.97 / 29.95) only with factor degree D = 34 = delta-40+... i.e. in r15w1
"m" is the RESIDUAL degree rho and delta-m the factor degree D. With BIM's m = factor degree the correct formula
(r4w2) is K = n m^2 s2^4/(2 (delta-m)^2 delta^3), and r33's regime-B line `K = n delta^2/(2 m^2)` is the swapped
(wrong) expression. Corrected (s2^2=delta, d=n^(1/4)): K = 9.5e5, 3.1e7, 2.5e9 at n=1e6,1e9,1e12, versus
delta^2 = 5.8e2, 7.5e3, 9.1e4: K/delta^2 -> infinity still holds (the n=1e6 point is pre-asymptotic: m~21, delta-m~3).
r33's verdict stands; its arithmetic did not.

## 5. Not done / open
- Simple-graph transfer of the Lambda-shift (needs Var_null Lambda for uniform simple graph with degrees g, and a
  planted-law mean; McKay-type input). Pairing level only.
- Conditional second moment given Lambda (or Q): not computed. r16w2 saw the Lambda-conditioned ratio still growing
  (0.074, 0.136, 0.241): unexplained here; non-Gaussian / higher-statistic terms are the candidates. For the two-type
  host the Gaussian prediction is that conditioning on Lambda removes all of K; that residual growth contradicts or
  signals a finite-n effect, unresolved.
- v2/scripts/r4w2_pairing_shift.py log_ratio raises a math-domain error for h=40, D=6 (residual > factor); not chased,
  so the K<->exact check is only in the D=34 (rho=6) direction.
## Outcome: PROVED: TV lemma (sec 1). SKETCHED: weak law false for unconditioned E Z (sec 2). FAILED: SSC/truncation
route to the stated lemma (statement is false). NOT PROVED: any repaired conditional form.
