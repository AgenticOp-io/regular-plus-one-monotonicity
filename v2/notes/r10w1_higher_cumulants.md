# r10w1: higher cumulants of the host statistic S, and what is still missing for (iii')

Scripts: `v2/scripts/r10w1_cum.py` (exact cumulants k2..k5 over ALL 2^m subgraphs, rational arithmetic, then exact rational regression on subgraph counts of H), `r10w1_dlog.py` (exact Delta log E e^{-cT}). Run: `python r10w1_cum.py n d p #samples`.
Labels: PROVED / EXACT-NUMERIC (exact rational arithmetic on finite cases, no general proof) / NUMERIC (floats) / OPEN. main.tex untouched.
Setting as r9w1: G0 D-regular, H = complement (d-regular), X ~ G(H,p), S = w1|E_X| + 2 P2(X) (+const); T = same with w1=2.

## 1. (a) Cumulants k>=4: which host statistics enter [EXACT-NUMERIC]
Exact fits (zero residual, 16-19 distinct d-regular H, regression on 1,t,c4,c5,diamond,K4 of H; columns dropped only if rank-dependent):
- n=10,d=3,p=1/2: k2: none. k3: t only (3/4 = 48 (pq)^3). k4: t (9/2), c4 (3/2). k5: t, c4 (15), c5 (15/4). No diamond/K4 for S.
- n=10,d=3,p=1/3 (S): k3 t coef 128/243; k4 c4 coef 2048/2187; k5 c5 coef 40960/19683. n=9,d=4,p=1/2: same c4,c5 coefficients, t and the k5-c4 coefficient double (d=3 -> 4).
Pattern found (two p values, two (n,d)):
  **coefficient of the k-cycle count c_k(H) in kappa_k(S) is exactly k! (2pq)^k, independent of d, n, w1** (k=3: 48 p^3q^3; k=4: 384 p^4q^4 = 3/2 at p=1/2, 2048/2187 at p=1/3; k=5: 3840 p^5q^5 = 15/4, 40960/19683 ok).
  Sub-leading coefficients (t in k4, c4 in k5) carry a factor (d-2) (p=1/2) and, at p!=1/2, w1-dependence; not derived.
Structural reason [PROVED, elementary]: a connected k-tuple of terms (edge or cherry) has overlap graph connected, so its union has <= k+1 edges. Joint cumulant is bounded by C_k p^{|union|}. Non-induced counts of any connected subgraph of a d-regular H with <= k+1 edges are, by closed-walk inclusion-exclusion, polynomials in n,d and c_3..c_{k+1}(and diamond/K4-type counts for larger shapes). So kappa_k(S|H) = poly(n,d,p,w1) + sum_{l<=k+1} b_{k,l} c_l(H)+... . The explicit cancellation of non-cycle shapes (diamond, K4 absent for S; c_{k+1} absent at k) is observed, not proved [OPEN: general proof].
Consequence for the tilt (exponent e^{-cS}): the leading cycle term of order k contributes (c^k/k!) k!(2pq)^k Delta c_k = **(2cpq)^k Delta c_k(H)**, the k=3 case being r9w1's (2cpq)^3 Delta t0. Direct check [NUMERIC, `r10w1_dlog.py`, n=10 d=3 p=1/2, extreme pair (t=0 vs t=6)]: exact Delta log E e^{-cT} = -8.1e-5, -5.1e-4, -2.4e-3 (c=.05,.1,.2) vs cycle-leading series k<=5: -9.2e-5, -7.2e-4, -5.6e-3: same sign and order, leading series overshoots (omitted sub-leading terms are negative); agrees as c->0.
Size [heuristic from the pattern, OPEN as theorem]: p ~ (hbar-D)/d so d p = O(1); sub-leading terms cost a factor ~ c d p q = O(c) per order, so with c = O(1/D) (r9w1 scale B gives c ~ 1/(190 D)) the series is geometric with ratio O(c * hbar-D) < 1 and Delta log -> 0 follows from (3-term) + (geometric tail) provided the coefficient pattern holds to all orders. Worst case |Delta c_k(H)| <= n^k/(2k) with pq n = O(1) gives terms <= (6c)^k/(2k): fine for c < 1/6.

## 2. (c) Re-check against the r6 tilt: S is NOT the right statistic [EXACT-NUMERIC + argument]
r6 tilts by Lambda(P) = sum over pairs in the pairing of y_i y_j with y per STUB (point) = h_v - hbar. Its pairing-mean is (W^2 - Q)/(2(M-1)), W = sum_stubs y = sum_v h_v y_v, Q = sum_stubs y^2 = sum_v h_v y_v^2. Hence the host statistic entering r6's beta is
 Lambda_bar = (W^2 - Q)/(2(M-1)), W = S - hbar M (+...), Q = sum h^3 - 2 hbar sum h^2 + hbar^2 sum h:
 it involves sum h_v^3 (and M = sum h, W^2), not only S = sum h^2. r8w1 (c = beta/(2(M-1)) linear in S) and r9w1's scale table used only the S-part (the -Q/(2(M-1)) piece, which is the correct leading term since W^2/M = O(chi^2) is a G0-nearly-independent O(1) term; but note it was never shown). beta itself = D/(rho hbar^2) matches r6 (rho=3,hbar=12: 0.0208), r9w1 used D/(3 hbar^2): consistent.
Exact cumulants of the extra statistics (p=1/2):
- sum h^3: k2 G0-independent; k3: t only; k4: t, c4, diamond, K4 (3-stars have 3 edges, so unions of k terms reach 2k+1 edges).
- F = W^2 - Q (r6 pairing-mean numerator, exact): **Var depends on t and c4 already at order 2** (n=10,d=3: Delta Var(F_true) = 18 Delta t + 6 Delta c4; n=9,d=4: 27, 3/2), since W^2 is quartic in edge indicators; k3..k5 are not fit by {t,c4,c5,dia,K4} (more shapes). The effect is relatively small here (Var F ~ 7e6 at n=10) but its n,d scaling is [OPEN]; it enters through beta^2 Var(F)/(4(M-1)^2) so one needs |Delta Var F| = o(M^2/beta^2) ~ o(n^2 hbar^2/beta^2): plausible (coefficients are O(1)-O(n^?) times Delta t,c4 of G0 <= n D^3), not proved.
So the r9w1 conclusion (order-3 negligible) is for the S-part only; for the true r6 statistic the G0-dependence starts at order 2 in the W^2 term, with tiny coefficients but an unproved scaling.

## 3. (b) Does S capture all host dependence of the tilted ratio N/E[N]? [OPEN]
Not decidable from the repo notes (N, its conditional-on-host law are defined in the r4/r6 pairing model; no exact small-n enumerator of N|host exists in v2/scripts). From Sec 2 the right candidate sufficient statistic is the degree sequence of the host (hence all of sum h^j through the pairing-count formula), not S alone: the pairing second-moment reduction (r6 Sec 2) depends on the host only through y_v. Precise lemma needed:
 LEMMA (open). For mu_D-most G0, with U = (W^2 - Q)/(2(M-1)): log E[e^{-beta ... }|G0] difference |log E_G0 e^{-beta U} - log E_bar e^{-beta U}| -> 0 [needs (i) cumulants k>=3 of U, G0-dependence through c_l(H), l<=k+1 with the coefficient bound b_{k,l} <= C^k (pq)^l (d p)^{k+1-l}; (ii) c_l(H) fluctuations under mu_D (McKay-Wormald-Wysocka-type, cited not checked); (iii) uniform tail: the geometric ratio O(beta d p q n^{-1})].
Missing estimate named: **uniform-in-k bound on the sub-leading cycle coefficients b_{k,l}** (observed (d-2)-linear for l=k-1; unproved for l<=k-2 and k>=6) plus the F=W^2-Q cross-terms.
Also unaddressed: f nonlinear in S (r5 residual statistic), simple-graph transfer.

## 4. Status
- PROVED: connectivity bound (union <= k+1 edges, so only cycles of length <= k+1 can appear at order k) for S; r8w1's TV-insufficiency (earlier).
- EXACT-NUMERIC: no t/c4 dependence at k2,k3(c4),k4(c5); coefficient k!(2pq)^k of c_k in kappa_k for k=3,4,5 (two p, two (n,d)); extra statistic sum h^3 and F=W^2-Q dependence structure (Sec 2).
- OPEN: all-k proof; sub-leading coefficients; scaling of order-2 F-dependence; (b).
