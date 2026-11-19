# r17b: R2* lower bound (4-edge pattern avoidance) - status: NOT proved, no new numerics

## Status
Blocked. No new theorem, no counterexample, no new computation this round.

## What I did
Read the r17 brief and r16w1_report.md. The brief is ambiguous on exact statement (matchings of the host vs
L-regular subgraphs F containing a pattern S); I did not pick an interpretation and prove under it, to avoid
asserting something unverified.

## What is established (from r16w1, unchanged)
- Provable level is still switching-only (k<=3, n^{1/3} barrier).
- Exact small-n data (L=3,4; n<=12) show the 4-edge joint log-cumulant u(S) decays roughly n^-2..n^-3
  (C4, triangle+pendant largest); star4 at L=4 is a degree-saturation artefact. Too small to fix exponent or L-dependence.

## Suggested next step
Fix the precise statement first (what is counted, what "avoiding" means), then try a Heilmann-Lieb /
inclusion-exclusion bound for connected shapes (C4, triangle+pendant) separately from disconnected ones.
