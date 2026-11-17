# r9w3: exp-form Theorem 6 for two-sided hosts -- what is proved, what is missing

Labels: [P] proved (symbolic, scripts re-run), [N] numeric, [O] open. main.tex untouched.
Scripts (re-run): `v2/scripts/r9w3_tri.py`, `v2/scripts/r9w3_cross.py` (sympy + numpy, seconds). Data: r7_data (D=3..10).

## Verdict
The exp-form Thm 6 is NOT proved. Task 1 outcome: for the host families below it is reduced to ONE explicit estimate,
the n^-2 coefficient r2(D) of E[#triangles] of G(n,D); I do not have a proof of that estimate. Everything else is exact.

## 1. Exact reductions (vertex-transitivity)  [P]
E[T] = (D-1)^3/6 * (1 + r1/n + r2/n^2 + ...). Exp-form error as in r7 (err = P/(base e^{-A-B}) - 1, c0 = lim n^2 err).
- S1_1_1 (uw, vw, target uv): P = 6E[T]/(nD(D-1)) exactly.
  n^0 term vanishes; n^-1 term vanishes iff r1 = 3(D-1)/D  (this is how r1 is determined; it is an assumption, tested in section 3).
  Then c0(S1_1_1) = r2 - 9/2 - 15/D + 67/(2D^2).
- S1_1_0 (uw, vx distinct, target uv): ordered 3-paths = nD(D-1)^2 - 6T, disjoint directed edge pairs = nD(nD-4D+2), so
  P = [nD(D-1)^2 - 6E[T]]/[nD(nD-4D+2)]. T enters only at relative order 1/n, so r2 drops out and with r1 above:
  **c0(S1_1_0) = (9D^2 - 50D + 45)/(2D^2) -> 9/2 = (1+1+0+1)^2/2**, bounded for all D. [P] given r1.
  So the exp-form Thm 6 holds with an O(1) constant (uniform in D) for this two-sided host; it needs no triangle second-order term.
- One-sided stars: r8w3 (exact, no r1 needed).

## 2. What is missing, exactly  [O]
(a) Hosts with a common neighbour (w>=1, e.g. S1_1_1): c0 = r2(D) + explicit rational; need r2(D) = O(D^{1-eps}) uniformly (O(1) expected).
    This is a second-order estimate on E[#triangles]: n^-2 term of a degree-D random-regular triangle count, not available from Gao20 Thm 6/McKay-Wormald-Wysocka
    (those give only the n^-1 term, and r1 = 3(D-1)/D itself is not proven here, only forced).
(b) Hosts with j,k>=2 and w=0: overlaps of the two leaf sets are impossible, but the count of (j,k)-double stars through uv on the exact side still has
    triangle/diamond corrections (common neighbours of u,v), i.e. also diamond densities. Not carried out.
(c) General H1 (not stars) and the far part: no exactness; same as r8w3 "Not done".
(d) The independent-of-D remainder O(D^3/n^3) per edge (n^-3 term): not analysed.
So the single estimate to prove for the n^{1/4} program is (a)+(b): second-order triangle (and diamond) counts of G(n,D) with polynomial-in-D control.

## 3. Numerics  [N]
`r9w3_cross.py`: r2(D) extracted from S1_1_1 data, then c0(S1_1_0) PREDICTED (no free parameter) and compared with fitted data:
D=4..10 predicted/data: -.344/-.341, .400/.403, .958/.959, 1.388/1.383, 1.727/1.714, 2.000/1.975, 2.225/2.181 (agree <=.044, the residual is the n-fit bias).
This confirms r1 = 3(D-1)/D and the whole reduction chain.
r2(D) from S1_1_1 (D=5..10): 6.25, 6.96, 7.54, 8.00, 8.40, 8.78.
Fits (rms): a+b/D+c/D^2 free: a=12.514 (rms .013) -- matches 25/2 = 8 + 9/2 (the conjectured L=(j+k+w+1)^2/2=8 for c0); pinned a=12.5 same rms;
but a + b ln D + c/D also fits (rms .008, b=2.6). Data cannot separate bounded from log growth (same caveat as r8w3). Bounded <-> n^{1/4} with m=O(1); log growth also still n^{1/4} (r8w3 section 4: only r2 ~ D^{>=1} loses it).

## 4. Rate, conditional  [conditional on (a),(b),(c),(d)]
If L(D)=O(D^{1-eps}) uniformly (Delta_H <= 2m): per-edge error (1+m^2)L/n^2, sum m(1+m^2)L(delta)/n, need delta^3 m^3 L = o(n): m=O(1) gives sharp range
delta = o(n^{1/4}) (capped by budget (iv)), as in r8w3. Without (a): the proved Thm-6 route gives n^{1/5}.

## 5. Proposed patch for main.tex (do not apply)
1. Thm~\ref{thm:sharp-rate-short}: no change (n^{1/6}). The n^{1/5} extension stays conditional on [Gao20, Thm 6] as in the sharp-rate notes.
2. Add, after Remark rem:n16-barrier, a remark "Exact exp-form constants": state c0 = (j+1)^2/2+O(1/D) for one-sided j-stars (j<=4 symbolic, r8w3) and
   c0(S1_1_0) = (9D^2-50D+45)/(2D^2) (this note), both via vertex-transitivity; state as Conjecture: for star hosts exp-form error = c/n^2 + O(D^3/n^3), |c|<=(j+k+w+1)^2/2,
   with the reduction of w>=1 to the triangle coefficient r2. Mark clearly: not a theorem; extension past n^{1/5} requires it.
