# r29: growing-D cycle first-order constant: attempt, NO new range proved
Status: NOT PROVED beyond fixed D. This note records which route fails where, and the exact missing lemma. Nothing here is a theorem.

## Range actually proved
Only fixed D (r25, O(n^-2) constant depending on D). No explicit D-dependence of that constant was extracted, so even D <= c sqrt(log n) is NOT claimed. r27 estimates the Bonferroni route reaches D <= c sqrt(log n) after an e^{D^2/2}/n^2 loss. That needs the constants in L1/(E2)/(E3) rewritten with explicit Delta-dependence (the (8l^3)^{Delta^2} free-site factor, the Delta^{2m} collision remainders). Not done: unproved input.

## Route (a): cumulant expansion of ln P(simple)
Needed Lemma L1': for degree sequences d, d' differing by B in total, uniformly in 3 <= D <= n^eps,
  |ln P_d'(simple) - ln P_d(simple) - [G0(s')-G0(s)] - dF3| <= C B (1+D)/n^2,
with F3 the McKay-Wormald term (r27 step 1). This is McKay-Wormald's exponent with error O(D/n) instead of O(D^2/n), in differentiable form.
MISSING: not in the literature found (r27 search: McKay-Wormald, Gao-Wormald 1404.1250, Burstein-Rubin 1511.03738, MWW04 all have errors too coarse). Proving it needs a cluster expansion of ln E[1_{X=Y=0}] on pairings. The loop/double-pair polymer activity is about D^2/n per vertex, so convergence is plausible for D^2 << n, but the Kotecky-Preiss condition with overlaps through shared vertices (each vertex lies in ~D^2 potential sites) is not verified.

## Route (b): second-order switchings
Single switchings give ratios with error O(D^2/n) (the forbidden-parallel count loses D^2/n). O(D/n^2) needs a two-step (double-switching) analysis in the McKay 1002.3018 style, in the sparse regime. MISSING; not attempted in detail.

## Route (c): citation
- McKay 1002.3018 Thm 11 / Cor 5 are for the dense range. They do not cover D = o(n^{1/2}). Only first-order agreement was checked (r27), not applicability.
- Sparse results (McKay-Wormald, Gao-Wormald) have relative error O(D^2/n) or O(sqrt(xi)): too large for the 1/n coefficient.
No citation closes it.

## Missing lemma (precise)
L1' above, uniformly for 3 <= D <= n^eps, or the explicit-constant version of L1 for D <= c sqrt(log n). Given L1', the rest of r25 (application section, plus the r27 steps 2-4 cancellation of D^2/n^2) goes through formally. Steps 2-3 also need uniform-in-D versions of the Z-Bonferroni: E binom(Z,2) is O(n^-2) only for bounded D, and is O(D^4/n^2)-type for growing D until refined. So the stated error O((D+k^2)/n^2) needs that refinement too.

## Evidence
r28 exact data (k=4, D=3..8): f1 = 2, and the 1/n^2 coefficient is about 4, flat in D. This supports the conjecture and proves nothing.
