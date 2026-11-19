# r15w3: R2* and r2(D) -- status (nothing new proved)

## r2(D), hosts with a common neighbour
- r2(D) = (D-1)(11D-16)/D^2 = 11 - 27/D + 16/D^2 is ALREADY determined by r13w1 (supersedes the "open" in r10w3/r14w2).
  Re-run today (v2/scripts/r13w1_r2_formula.py): fit vs formula D=3..7:
  3.77778/3.77778, 5.25/5.25, 6.24/6.24, 6.94441/6.94444, 7.46898/7.46939 (D=7 is an out-of-sample check).
- Status: NUMERIC-EXACT (3 parameters matched to 5 exact-DP values). Pairing-model part (2D^2-27D+58)/D^2 is algebra;
  the conditioning remainder 3(3D^2-14)/D^2 = 9-42/D^2 is NOT proved (needs P(simple | degree sequence) to relative n^-2,
  same gap as r1=3(D-1)/D). I found no way to close it here.
- Consequence carried: c0(S1_1_1) = (13D^2-84D+99)/(2D^2) < 8; c0(j,k,D) polys of r14w2 stand (conditional on r1, r2).

## R2* (n^{1/3} < L < n^{1/2})
- NOT proved. Reduction unchanged (r6): R2* on L=o(n^{1/2}) <=> (B*) |kappa_k| <= C^k k! L^{k+1}/n^{k-1}, k>=4;
  equivalently a cluster expansion of p_S = P_nu(S subset F) with connected corrections (c/n)^{|C|-1}.
  t3 <= 8L^3/n^3 (switching) handles k<=3; every product-form (switching/avoidance) bound stops at n^{1/3}.
- Precise lemma needed (k=4 suffices to test): for every 4-edge S, log p_S - 4 log(L/(n-1)) - (connected k<=3 parts)
  = O(L^a n^-3) with the 4-cycle / diamond host counts entering only via their known densities; r2(D)-type second-order
  host counts are the analogue of the unproved conditioning term above, so both gaps are the same kind: second-order
  (n^-2) expansion for matching-avoidance counts of a regular host.
- No script written: no new computation would discriminate beyond r6/r13w1.
