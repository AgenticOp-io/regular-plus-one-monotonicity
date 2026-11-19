# r16 worker brief: R2* on n^{1/3} < L < n^{1/2}

Read first: v2/notes/r15w3_R2star_r2D.md, v2/notes/r2_worker2_peel.txt (R1 proved, R2* open).
Write only your own files: v2/notes/r16w1_* and v2/scripts/r16w1_*. Do not edit paper/main.tex.

## Goal
Prove (B*): |kappa_k| <= C^k k! L^{k+1} / n^{k-1} for k >= 4, L = o(n^{1/2}).
Equivalent: cluster expansion of p_S = P_nu(S subset F), connected corrections of order (c/n)^{|C|-1}.

## Known
- k <= 3 is covered by the switching bound t3 <= 8 L^3/n^3.
- Switching/avoidance arguments stop at n^{1/3}.

## Missing step
Two-sided second-order expansion of p_S for 4-edge S, i.e. matching-avoidance counts of a
regular host (same kind of gap as the conditioning term in r2(D)).

## Do
1. State the exact 4-edge-S expansion p_S = prod p_e (1 + sum of connected corrections) with
   explicit error O((L/n)^a). Find the smallest a you can prove, both directions.
2. Check numerically (exact small D / pairing model, scripts in v2/scripts) before claiming.
3. If the proof fails, say exactly which inequality fails and whether it is intrinsic.

Report: proved / numerically checked / not checked, separately.
