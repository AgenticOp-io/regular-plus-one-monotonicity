# r34: lemma L1' (uniform-in-D local variation of ln P(simple)): NOT PROVED
Status: no proof, no new range. This note records which routes were examined, why each stops, and one reduction. Nothing here is a theorem.

## Target (L1')
For degree sequences d, d' on [n] with max degree <= D, sum|d-d'| <= B, D <= n^c:
  ln P_d'(simple) - ln P_d(simple) = G0(s') - G0(s) + O(B(D+B)/n^2)
(G0 = -s2/(2 s1) - s2^2/(4 s1^2), as in r25). Fixed D is r25.

## Routes examined
1. **Asymptotic enumeration formulas (McKay-Wormald 1991, Isaev-McKay 2018, Gao).** They give ln P_d to an absolute error: D^3/n at best in the sparse range (regular case: -(D^2-1)/4 - D^3/(12n) + O(D^2/n)). A bounded error says nothing about a difference of two values at distance 1/n in s: the difference is only controlled to the same D^3/n. To use the formula one needs the error term to be differentiable in d with gradient O(D/n^2) per unit. None of the published statements gives a gradient bound, and the error is not given as a function of d. Conclusion: not usable as stated.
2. **Smoothness by Cauchy estimates / analyticity in d.** Would give gradient = error/(scale of analyticity). P_d is only defined on integer d, and an interpolation (real degrees) has no counting meaning. The Isaev-McKay proof does use a complex integral over the torus, but the degrees enter as a real exponent vector in a saddle-point integral. Varying d continuously there is natural (the integrand is analytic in d), so a differentiable-in-d version of their theorem looks plausible. That is a re-derivation of their argument with explicit d-dependence of every error term, not done here, and I make no claim about its range.
3. **Exact identity.** Counting pairs (G, v) with uv in G gives sum_v P_d(uv in G) = d_u. With a forbidden pair, N(d - e_u - e_v; uv forbidden) = N(d - e_u - e_v) - N(d - e_u - e_v; uv forced). This is exact, but it relates ratios of counts at degree sequences that differ by 2 units to each other. It is a recurrence for the very ratios L1' controls, so using it needs L1' at one lower order (circular, same as r31 for switchings). It does give a consistency check but not an evaluation.
4. **Cluster / cumulant expansion of ln P(X+Y=0).** Poisson-type cumulants: ln P = -E[X+Y] + (corrections from joint cumulants of loop/double indicators). Cumulant j contributes (D^2/n)^{j-1}-type connected clusters; to get O(D/n^2) one needs all clusters with weight >= D/n^2, which at growing D includes order ~ (D^2/n)^j for every j with (D^2/n)^j >= D/n^2. For D <= n^{1/2-e} that is a bounded number of clusters, but each cluster's value needs the *exact* factorial-moment weights (E3 of r25 with D-dependent constants) and the convergence of the cluster series needs D^4 <~ n so the combinatorial entropy (2e D^4 per site, r25 E3) is beaten. This is a plausible route to L1' for D <= c n^{1/4} but needs a cluster-convergence theorem for the hard-core-like dependence of loop/double events through shared points (they are not independent: sharing a point forbids co-occurrence). That is a polymer-model / Kotecky-Preiss verification. Not carried out.

## Error-budget table (v2/scripts/r34_budget.py)
Scan at n=1e6 of the largest D for which each route's bound is <= the target D/n^2 (constants dropped, so this is optimistic):
| route | max D |
| MW91 bounded error D^3/n | 0 |
| smooth gradient D^3/n^2 | 1 |
| single switching D^3/n^2 | 1 |
| double switching, if L1' were available (D^4/n^3) | 100 (= n^{1/3}) |
Reading: the only budget that clears target at growing D is the one that already assumes L1', matching r31. Everything else misses by a factor of at least D^2.

## Reduction (what would suffice)
For the cycle application only the following is used: a zeroth-order L1 (relative O(1/n) change under a bounded perturbation, uniformly in D <= n^c with the constant polynomial in D) plus the first-order term n*DeltaG0 = k(D-2) with error O((D+k^2)/n). Concretely it is enough to show, uniformly, ln P_d'(simple) - ln P_d(simple) = n^{-1}(grad G0 . n(s'-s)) + O(D^2/n^2)?? -- no: the needed final error is D/n^2 (r25: R has error O(n^-2) *times D*), so the weaker D^2/n^2 would give f1 with error O(D^2/n^2), i.e. D = o(n^{1/2})-compatible statement "f1(k)/n + O(D^2/n^2)". That weaker version is what a cluster expansion (route 4) at D <= n^{1/4} could deliver and is enough for (R2*, k=4) up to D <= n^{1/4}. Not proved.

## Honest outcome
- Proved: nothing new.
- Not proved: L1' in any growing-D range.
- Concrete next step with the best odds: route 4 for D <= c n^{1/4}, error stated as O(D^2/n^2) (weaker than L1'), via Kotecky-Preiss on the polymer gas of loop/double clusters with the D^4-per-site activity bound from r25 E3 (convergent when D^4 <= c n). Alternative: make Isaev-McKay's integral differentiable in d (route 2).
