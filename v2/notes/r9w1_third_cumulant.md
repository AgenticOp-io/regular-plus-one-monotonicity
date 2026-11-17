# r9w1: third cumulant of the host statistic S and what (iii') needs

Scripts (re-run before this note, asserts pass): `v2/scripts/r9w1_k3.py` (exact kappa_3 by connected-triple enumeration, rational arithmetic, vs brute force over all 2^m subgraphs), `r9w1_fit.py` (exact rational fit over random regular H), `r9w1_check.py` (G0-difference identity, Var(S) formula, scale table).
Labels: [P] proved, [X] exact (rational arithmetic) check on finite cases, no general proof written, [N] floating numerics, [O] open. main.tex untouched, nothing committed.

## 1. Setting
G0 D-regular on n vertices, H = complement (d = n-1-D regular), X ~ G(H,p) (q=1-p), host degree = D + rho_v.
S = sum_v (D+rho_v)^2 = const + w1*|E_X| + 2*P2(X), w1 = 2+4D, P2 = # 2-paths of X. (r8w1 used T = sum rho_v^2, i.e. w1 = 2; same result below, the coefficient does not depend on w1.)

## 2. Task 1: exact third cumulant [X]
**Result: kappa_3(S) = A(n,D,p,w1) + 48 p^3 q^3 * t(H), with NO dependence on 4-cycles of G0 or H, and no D/w1 dependence in the coefficient of t(H).**
Since t(H) = C(n,3) - m0(n-2) + sum_v C(d_v,2) - t0(G0) and m0, d_v are fixed, for two D-regular G0, G0' on n vertices:

  **kappa_3(S | G0) - kappa_3(S | G0') = -48 p^3 q^3 (t0(G0) - t0(G0')).**

Evidence [X]:
- Enumeration code equals brute force exactly (Fractions, p=3/10 and 1/2): n=6 (C6, 2xK3), n=8 (Q3, 2xK4), n=10 (G0 = complement of C10, C5+C5, C3+C7, C4+C6, C3+C3+C4; t0 = 50,50,49,50,48). The identity above holds exactly in every pair, e.g. C6 vs 2xK3 at p=.3: 0.889056 = 48*.3^3*.7^3*2; Q3 vs 2xK4: 3.556224 = 48*.009261*8.
- Exact rational regression of kappa_3 on (1, t(H), c4(H)) over random d-regular H: n=8 d=2,3,4; n=9 d=4; n=10 d=4,5,6 (5 graphs with distinct (t,c4) each, zero residual). Coefficient of t(H) is 48p^3q^3 for every (n,d); coefficient of c4(H) is 0. (n=7 had too few graphs, rank-deficient, skipped.) The C4+C6 vs C10 pair (c4(G0) = 201 vs 200, same kappa_3) is a direct instance.
- Structural reason (why only triangles can appear) [P-sketch]: three terms (edge or 2-path monomials) with connected overlap span at most 4 edges, so the only cyclic unions are triangle, paw and C4. The code shows the C4 and paw contributions combine so that d-dependence and c4 cancel; I did NOT write a symbolic proof of that cancellation. [O: general (n,d) proof]
- r8w1's "proportional to triangle deviation" is now an identity (on the tested range), and its worry that 4-cycle counts enter is answered: they do not at order 3.
- mean and variance are G0-independent for regular G0 (r8w1); I also checked Var(S) closed form: Var = w1^2 m pq + 8 w1 n C(d,2) p^2 q + 4[n C(d,2)(p^2-p^4) + 2m(d-1)(2d-3) p^3 q], m = nd/2, equals brute force exactly (n=8,D=3,p=.3).

## 3. Task 2: size of the third-order term
Exponent: weight e^{-cS}, so log E_{G0} e^{-cS} difference at order 3 is -(c^3/6) Delta kappa_3, whose size is
  **|E3| = (c^3/6)*48 p^3 q^3 |Delta t0| = (2 c p q)^3 |Delta t0|.**   [X, from Sec. 2]
So the third-order term is negligible iff **c p q |Delta t0|^{1/3} -> 0** (c = tilt per unit of S). It is not an obstruction unless the tilt per unit S is of order 1/(pq t0^{1/3}), i.e. enormous.

Scale table [N, `r9w1_check.py`], p = (hbar-D)/(n-1-D), hbar=12, D=9, Delta t0 = D^{3/2} (typical) or n D^2/6 (worst case, any D-regular graph):
- (A) c = beta/(2(n hbar-1)), beta = D/(3 hbar^2) [assumption: M = n hbar stubs; this is my reading of r8w1's c = beta/(2(M-1))]: n=1e3..1e6: E3 ~ 4e-24 .. 4e-42 (typ), 2e-21 .. 2e-36 (worst). Here c*sd(S) ~ n^{-1/2} -> 0: the S-tilt is tiny, **the sqrt(K) -> inf spread of N comes from the pairing, not from S** (this refines r8w1 Sec 2, where t = L was used: with that standardized scale the quantity that matters is c*sd(S) = L).
- (B) forced standardized scale c = sqrt(K)/sd(S) with K = n/1550 (r6 fit): c*sd(S)=0.8..25 (genuinely growing), yet E3 = 4e-16 .. 4e-25 (typ), 2e-13 .. 2e-19 (worst).
- Dense host p=.3, D=9, K = D^2/9 fixed: E3 <= 3e-8 (worst) at n=100, decreasing like n^-6.
Reason: p^3 q^3 = O(n^-3) in the sparse regime and sd(S)^3 >= n^{3/2}*poly in every regime; in the dense regime sd(S)^2 ~ n^3.
**Conclusion [N + exact identity]: beta^3 Delta kappa_3 -> 0, at both the r6 tilt scale and the forced sqrt(K)-standardized scale, for every D-regular G0 (not just typical), polynomially fast. No counterexample regime exists at order 3 within hbar,D fixed or dense p; one would need c >= 1/(pq t0^{1/3}).** A genuine counterexample regime would be a tilt c of order >= 1/(p q |Delta t0|^{1/3}), outside anything in r4-r8.

## 4. Task 3: what (iii') needs, what is proved
Needs: log E_{G0} e^{-f(S)} - log E_bar e^{-f(S)} -> 0 for mu_D-most G0 (then Y -> 1), not TV (r8w1 Sec 2).
- Proved [P, r8w1 Sec 2]: TV closeness is insufficient; Gaussian mean/scale shifts need delta = o(K^{-1/2}), s^2-1 = o(1/K).
- G0-independence at order 1,2 [P/X]: mean and variance of S identical for all regular G0. Order 3 [X]: difference exactly -48 p^3 q^3 Delta t0, and by Sec 3 negligible by many orders (E3 <= 1e-13 over the tested scales). Triangle count of G0 is the only G0-statistic at order 3.
- NOT done [O]: (a) orders k >= 4 (kappa_4 depends on c4 and likely d; r8w1 found Delta kappa_4 != 0 at n=6,8; no coefficient derived; the code extends by quadruple enumeration but is not run); (b) uniform control of the full cumulant series (an analytic route: S is a quadratic polynomial in independent edge indicators, so a cumulant bound |kappa_k| <= n C^k (poly) with tilt c ~ n^{-1} would give Delta log E = O(n^{-(k-1)}) per order, but this needs a proof, only sketched); (c) concentration of t0 under mu_D (cite: cycle counts of random regular graphs are asymptotically Poisson for D = o(sqrt n) [McKay-Wormald-Wysocka, not re-verified here]; not needed for the worst-case bound in Sec 3, which holds for all G0 up to n D^2/6); (d) f nonlinear in S and the true form of c, K (assumptions A,B above are read off r6/r8w1, not rederived); (e) simple-graph / configuration-model transfer.
- Net status: the specific worry in r8w1 ("beta^3 Delta kappa_3 -> 0?") is resolved yes (Sec 3). (iii') itself is NOT proved: orders >= 4 and the series tail are open, and the requirement that the host statistic S capture all G0-dependence of E[1/N|G0] is still conjecture [r6 Sec 2].
