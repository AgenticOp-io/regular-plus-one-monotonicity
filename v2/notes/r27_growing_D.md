# r27: growing D for the cycle first-order constant: the D^2/n^2 obstruction cancels (heuristic, NOT proved)
Status: HEURISTIC plus exact anchors. The fixed-D proof (r25) still does not extend; see "What a proof needs".
Script: v2/scripts/r27_growing_D.py (sympy, asserts all claims below).

## Question
r25 proves E C_k = (D-1)^k/(2k) (1 + f1(k)/n + O(n^-2)) with f1(k) = k(5-k)/2 + k(k-4)/D for FIXED D.
For D = D(n) -> infinity, the question is how large the second-order term is in D. That fixes the range of D where f1/n is the true correction.

## Literature (searched 2026-11-19)
No sparse enumeration with relative error o(1/n) uniformly in growing D was found.
- McKay-Wormald (degrees o(n^1/2)): the exponent has the D^3/n term, with error O(d^3/M) = O(D^2/n), which is too coarse.
- Gao-Wormald, arXiv:1404.1250, Thm 1: error O(sqrt(xi)).
- Burstein-Rubin, arXiv:1511.03738 (degree switching to arbitrary order): ratio errors O(S^(-2 tau)), digraph setting.
- MWW04 eq. (2.2): O(r(r+d)/n).
So growing D cannot be closed by citation.

## Heuristic second order
In the r25 factorisation, ln R = [ln P_d'(A) - ln P_d(simple)] + ln P(Z=0 | A).
Use the McKay-Wormald exponent ln P_d(simple) ~ G0(s) + F3 with
  F3 = -M2^2 M3/(2M1^4) + M2^4/(4M1^5) + M3^2/(6M1^3),  M_r = sum (d_v)_r,
whose regular value is -D^3/(12n) (this is checked). Then track every n^-2 term with the top power D^2:
1. **Local change of F3.** Host H with e(H) edges, where each host vertex loses deg_H points: dF3 = +e(H) D^2/(2n^2) + O(D/n^2). This is linear in the total defect 2e(H).
2. **Z-shift.** Given a rest pair e parallel to a host edge, P(A|e)/P(A) = exp(dG0 - #{extra forbidden parallels}/N) = exp((D-1)/n - D/n + ...). The D/n terms cancel, so there is no D^2/n^2 term.
   (The first draft of this round dropped the extra forbidden parallel and got a spurious -k D^2/n^2. The exact edge anchor below caught it.)
3. **Z factorial cumulant.** Two rest pairs on the same host edge make a double edge, which A excludes. Each host edge therefore gives -(E Z_e)^2/2 = -D^2/(2n^2), and pairs on different edges give O(D^2/n^3).
4. **G0 second order, prefactor.** O(k^2/n^2), with no D growth.
Total coefficient of D^2/n^2 in ln R: e(H)/2 - e(H)/2 = **0**, for every host.

## Anchors and consistency
- **Exact edge:** P(uv in G) = D/(n-1) gives R = (nD-1)/(D(n-1)) and ln R = (1-1/D)/n + O(1/n^2), with no D^2/n^2 term. The heuristic gives 1/2 - 1/2 = 0. ✓
- **Exact path P3:** P = D(D-1)/((n-1)(n-2)), again with no D^2/n^2 term. The heuristic gives 1 - 1 = 0. ✓
- **Dense consistency:** for D = lambda n, a fixed subgraph appears with probability lambda^{e}(1+O(1/n)), so every pure term k (D/n)^j must vanish. f1 has no D/n term (it is bounded in D), and the k D^2/n^2 term vanishes. ✓ The D-independent part k(5-k)/2 of f1 also agrees with the dense correction exp(-(1-lambda)k/(lambda n)) after (n)_k p^k is rewritten in terms of D. (That dense formula is quoted from memory and was not re-checked against McKay's paper.)

## Conjecture (growing D)
For 3 <= D = o(n) and fixed k,
  E C_k = (D-1)^k/(2k) (1 + f1(k)/n + O((D + k^2)/n^2)),   f1(k) = k(5-k)/2 + k(k-4)/D.
In particular f1(4) = 2 stays the first-order constant for every D = o(n), and the error is uniformly O(k^2/n) in D. This is sharper than MWW04's O(k(k+D)/n).
Caveat: the k(k-4)/(Dn) part of f1 is smaller than the conjectured O(D/n^2) error once D^2 >~ n. So the D-dependent part of f1 is meaningful only for D = o(n^{1/2}), while the D-free part k(5-k)/2 is meaningful for D = o(n).

## What a proof needs (not done)
- The r25 Bonferroni route fails for growing D. The alternating sums cancel from e^{+D^2/4} down to e^{-D^2/4}, so the relative error is e^{D^2/2}/n^2. That restricts the route to D <= c sqrt(log n), and the free-site bound (8l^3)^{D^2} is worse still.
- A proof should expand the LOG (a cluster/cumulant expansion of ln P(simple) on the pairing model) or use second-order switchings, so that no e^{D^2} cancellation occurs. Step 1 above says the needed input is the local variation of the n^-1 term of ln P_d(simple) to accuracy o(1/n^2), uniformly in D. Equivalently, McKay-Wormald's exponent is needed with error O(D/n) in place of O(D^2/n), in a form that can be differentiated in d.
