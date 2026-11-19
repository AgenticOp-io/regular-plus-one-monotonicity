# r15w2: conditions (A), (B) for near-regular hosts — consolidation, no new scripts
Sources: r3_worker1_host_terms.txt, r4_worker2_hosts.txt (Lemma 7, Props 1-3, Thms 5-6). `python scripts/r4w2_formula_check.py` re-run: still agrees (exact vs formula within ~10%).

## (B) PROVED, modulo exactly two cited facts
Setting: host degrees h_v = hbar + y_v, |y_v| <= Y_h = C sqrt(hbar log n); factor degree D; r = h - D residual, rho = eps D = hbar - D.
Need: TV(mu', mu_D) -> 0 where mu'(G0) ~ W(G0; r) (G0 a D-regular graph, W = number-of-completions weight).

Cited facts (nothing else is imported):
 (M1) [McKay 1985, Thm 4.6] as quoted in main.tex: W(G0;r) = W0(r) exp(-mu(r,G0) + O(Dhat^2/M)), mu = sum_{ij in G0} r_i r_j/(2M'), 2M' = sum r = n rho,
      uniformly for all D-regular G0, Dhat = Delta(r)^2 + Delta(r)D, under Dhat^2 = o(M'). (error term is G0-independent in sign-free form: it is a uniform O(.)).
 (M2) [McKay-Wormald 1991] P(simple pairing of D-regular cells) >= exp(-C1 D^2) (used only for P(A) >= e^{-C1 D^2}).
 Plus the switching-martingale concentration of pairings (Wormald 1999 Thm 2.19; or: expose partners point by point, a switch changes T by <= 4W^2, Azuma).
 I did not re-verify Wormald's exact constants; only the form P(|Y-EY|>=t) <= 2 exp(-t^2/(2 s^2)) with s^2 = (m/2)c^2 is used, and constants are immaterial.

Step 1 (algebra, exact). Write r = rho + y. For L-regular G0, sum_{ij in G0}(rho y_i + rho y_j) = rho D sum y = 0, so mu = const + T(G0)/(n rho), T = sum_{ij in G0} y_i y_j.
  Hence dmu'/dmu_D (G0) = e^{-Y}/E_{mu_D} e^{-Y} * (1+O(error)), Y = T/(n rho); the (1+O) factor is uniform and o(1) by M1's hypothesis.
Step 2 (Lemma 7, r4 Sec 5). mu_D = uniform pairing of nD points (cells of size D) conditioned on A = {simple}. Weights w_v = y_v, W = Y_h, den = n rho, Delta_P = D.
  P(|Y-EY|>=t) <= 2e^{-t^2/(2s^2)}, s^2 = (nD/2)(4Y_h^2/(n rho))^2.
  Condition s*D -> 0, i.e. D^3 Y_h^4/(n rho^2) -> 0, i.e. (Y_h^2 = C hbar log n ~ C D log n)  D^3 log^2 n = o(eps^2 n).
  Choose omega -> inf slowly, eta = s D omega -> 0, omega^2 > 8 C1. Conditioning on A (P(A) >= e^{-C1 D^2}) gives
  P(|Y-EY|>=k eta | A) <= 2 e^{-k^2 D^2 omega^2/2 + C1 D^2} <= 2 e^{-k^2 D^2 omega^2/4}.
  Peeling on k = 0,1,2,...: E[e^{-(Y-EY)}|A] <= e^{eta} + sum_{k>=1} e^{(k+1) eta} 2e^{-k^2 omega^2/4} = 1+o(1) (D >= 1, eta <= omega^2/16). Same with +Y, and E|Y-EY| |A <= eta+o(1).
Step 3 (TV). With Ybar = Y - EY, Z := e^{-Ybar}/E e^{-Ybar}: E Z = 1 and E|Z-1| = 2E(1-Z)_+ <= 2 E(Ybar)_+ /E e^{-Ybar} = o(1) since (1-e^{x})_+ <= x_+ and E e^{-Ybar} = 1+o(1).
  TV <= (1/2)E|Z-1| + o(1) = o(1). []
Condition: D^3 log^2 n = o(eps^2 n) (host spread within Y_h). Rate in terms of exact variance (r3 Sec 2): sd(Y) ~ (1+eps) sqrt(D)/(sqrt2 eps sqrt n); sharper condition D = o(eps^2 n) is only heuristic (Lemma 7 loses log^2 n and Lipschitz-vs-variance).
Result is uniform over every host sequence satisfying |y_v| <= Y_h and Dhat^2 = o(n rho); no assumption on the third/fourth host moments.
Caveat: nothing here uses the "sub-Gaussian at scale L" sketch of r3 Sec 3; it is replaced by Lemma 7 (the r3 sketch with b_max^2 = O(L log n) is the same argument with the conditioning on A handled by P(A) >= e^{-C1 D^2}, which r3 said was needed but did not do — that is the gap closed).

## (A) — exact status
(A) := E_h N^2/(E_h N)^2 = exp(sum_{k>=3} x^k/(2k))(1+o(1)), x = 1/(hbar-1), for a host degree sequence h.
 Pairing-level identity (proved, r4 Prop 1): E_pair Z^2/(E_pair Z)^2 = E_pi[f(S)1_{S even}], f depends on h only through the totals; y enters only via the overlap law pi.
 Prop 2/3 (proved): c(S*) = hbar^3/(2 n rho^2 D^2); E_pi S = S* + Delta, Delta = n D^2 s2^2/hbar^3 (1+O(Y/hbar)), s2^2 = mean y^2.
 Define K := c Delta^2 = n D^2 s2^4/(2 rho^2 hbar^3).
 Sharp statement (pairing level):
   * K -> 0  =>  ratio = sqrt((hbar-1)/(hbar-2))(1+o(1)), same as regular host. [Sufficient. Proof: Delta = O(sqrt(K/c)) = o(sigma_S) since c sigma_S^2 = hbar/(2(hbar-1)); the overlap law is a convolution of independent hypergeometrics (log-concave, variance sigma_S^2 ~ n rho^2 D^2/hbar^3 -> inf, sigma_S depends on y only at relative order s2^2/hbar^2), so a shift o(sigma_S) and relative variance change o(1) change the Gaussian integral of f by 1+o(1). The local-CLT step is stated, not written out with explicit Berry-Esseen constants.]
   * K bounded away from 0  => ratio >= sqrt(...) * e^{K(1+o(1))-...}: (A) false (rigorous lower bound: exp((|Delta|-2 sigma_S)^2/(4 n rho) - O(1)), which is weaker than K when K = O(1); the two-sided Gaussian formula exp(K (hbar-1)/(hbar-2)) was verified to ~10% numerically only).
   So the pairing-level truth is "(A) iff K = o(1)": s2^2 = o(eps hbar^{3/2}/sqrt n). 
 Typical G(n,p): s2^2 ~ hbar(1-p) => K ~ n/(2 eps^2 D) -> inf. (A) is FALSE there (fully rigorous at pairing level; at simple-graph level Thm 5 of r4 needs McKay as quoted).
 Simple-graph transfer on the class {K = o(1), Y_h-bounded, D^3 log^2 n = o(eps^2 n)}: host terms of the four-pairing exponent give Psi = const + A m2 with A m2 = (L-1) m2/h^3 (r3 Sec 1; exact sympy), which is o(1) there (K=o(1) forces m2 << hbar^2), and the pairing sums concentrate by Lemma 7. This yields (A) on the class, but I did NOT rewrite the four-pairing proof of thm:growing-degree-factor with non-constant cells; so on this class (A) is "proved at pairing level, simple-graph level reduced to the paper's proof + r3 Sec 1 + Lemma 7, not written out".
 Note the class is tiny for the application: almost-regular hosts (s2^2 << 1 for hbar ~ BIM), probability e^{-Theta(n)} under G(n,p). It does not help the actual problem.

## What the paper actually needs (sharpest correct replacement for (A))
Not E_h|Z-1| small for all typical h; that is false (E|Z-1|^2 -> inf, and the second moment bound is tight at pairing level).
Needed, in either form:
 (A*) conditional version: for hosts H uniform with degree sequence h, N(H)/E[N|h, Lambda(H)] -> 1 in L^1, where Lambda(H) = sum_{ij in H} y_i y_j (assortativity),
      equivalently E[N^2 | h, Lambda]/(E[N|h,Lambda])^2 = exp(sum_{k>=3} x^k/2k)(1+o(1)).
      Heuristic: K = beta^2 Var Lambda with beta = D/(rho hbar^2), Var Lambda ~ (n hbar/2) s2^4 (r4 Sec 8), i.e. K is exactly the log-variance of exp(-beta Lambda); conditioning on Lambda removes it. UNPROVEN AND UNTESTED.
 (A**) or an external lower bound P(N >= 1) >= 1/2 for G(n,p), np = (1+eps)D, so that averaging over d* (r4 Thm 8) closes, with (B) done above. Also not available from the paper's moments.
Also unresolved: after conditioning on Lambda, the remaining conditioning also changes (B): the tilt e^{-T(F)/(n rho)} must be re-expressed given Lambda; T(F) concentration (Lemma 7) is on the factor, not the host, so it should be unaffected, but this was not checked.

## Honest ledger
PROVED: (B) with the stated exponent condition, from M1+M2+switching concentration (Steps 1-3; Lemma 7 from r4, re-derived here with the TV step made explicit).
PROVED (pairing level): (A) iff K = o(1); (A) false for G(n,p) degree sequences.
REDUCED, not written: simple-graph (A) on the K = o(1) class.
OPEN: (A*) conditioned second moment; P(N>=1) lower bound; hence TV for G(n,p) hosts is still open.
Not checked: Wormald Thm 2.19 constants; local CLT constants; no new numerics beyond re-running r4w2_formula_check.py.
