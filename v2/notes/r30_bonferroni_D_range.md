# r30: explicit D-dependence in the r25 Bonferroni argument; provable growth range
Status: a theorem for D <= c (ln n)^{1/4} with error exp(O(D^4))/n^2, conditional on ONE re-derivation flagged below (S1). Nothing beyond that range is claimed. r27's "D <= c sqrt(log n)" is NOT reached by this route.
Notation: Delta = max degree = D (all degree sequences used are within B = O(k) of D-regular), L = max(ceil(2e^2 D^4), ceil(3 ln n)), l <= L+1, m <= 2l.

## Step-by-step D-dependence of r25
(E1) Exact moments: no constants.
(E2) Collisions. r25 uses the absolute remainder binom(|V|,2)^2 Delta^{2m} n^{|V|-2} (relative to nothing). (S1) For d within B of D-regular, Sum_v (d_v)_{a+b} <= n (D)_{a+b}(1+O(B/n)) <= n (D)_a (D)_b (1+O(B/n)) and s_r = (D)_r(1+O(B/n)) or 0 for r > D, so each collision term is a RELATIVE O(|V|^2/n) correction to the leading product, and the 2-term Bonferroni remainder is relative O(|V|^4/n^2). The leading term is prod_x (D)_{r_x}/N^m <= D^m n^{-m} (N = Dn), i.e. weight D per pair. This replaces Delta^{2m} by an honest D^m (no factor beyond what (E3) already carries) and gives |rho_jk|, |mu1_jk|, |grad mu1_jk| <= (c D^2)^l poly(l) n^{-2 or -1}, bounded by the (E3) sum. I checked this at the sketch level only (uniform-in-D version of r25 line 54-57 was not written out line by line). If S1 fails, the proven range below shrinks (Delta^{2m} = exp(O(D^4 ln D)) would give D <= c (ln n / ln ln n)^{1/4}).
(E3) Site weights (fresh loop <= D^2, fresh double <= D^4, defect <= 4l^2 D^4/n, free <= 4l^2 D^2), free sites f <= D^2 t. Result: l! E binom(X+Y,l) <= 2(2D^4)^l (1+R_l), R_l <= sum_t (2(D^2+1)(8l^3)^{D^2+1}/n)^t.
 - Needed (G1): 2(D^2+1)(8(L+1)^3)^{D^2+1} <= n/2. With L ~ max(15 D^4, 3 ln n): (D^2+1)(ln 8 + 3 ln(L+1)) + ln(2(D^2+1)) <= ln n - ln 2. This holds iff D^2 ln D <~ ln n, i.e. D <= c sqrt(ln n / ln ln n). It is NOT the binding constraint.
 - Needed (G2): m^2 <= N for F_m(N) >= N^m/2: trivial here.
(E4) Truncation at L: tail <= 4(2e D^4/(L+1))^{L+1} <= 4 e^{-(L+1)} <= 4 n^-3 by the choice of L (this is where L >= 2e^2 D^4 enters).
 Error sum: n^-2 sum_{l<=L+1} (c D^2)^{l-ish} 2^l poly(l) l^{c_D}/l! with c_D = 3+3D^2, using the (E3) weights (2D^4)^l (crude, from r25): <= n^-2 e^{2D^4} (L+1)^{3D^2+7}. Define
   E(n,D) = exp(2 D^4) (L+1)^{3D^2+7}.
 For D >= 3: ln E <= 5 D^4 + (3D^2+7) ln ln n (up to lower order). THIS is the binding constant: it is where D^4 (not D^2) enters, because (E3) bounds the absolute weight per site by 2D^4 although the true Poisson mean is lam1+lam2 ~ D^2/4.
L1 (local perturbation): ln P_d = G0 + e^{-G0}H1/n + O(e^{-G0} E/n^2). Here e^{-G0} = e^{(D-1)/2+(D-1)^2/4} <= e^{D^2/4+D}, and C^1 bounds on H1 are E(n,D) by (E4). Changing s by O(B D^2/n): L1 error  <= C B D^2 e^{D^2/2+D} E / n^2 (the extra factor D^2 from |s'-s|).  Requires e^{-G0}E/n <= 1/2 (G3).
Application:
 - E binom(Z,2) <= (k D^2)^2/2 * (N^-2) * (P_cond/P_d <= 2 by L1 at order 0) = O(k^2 D^2/n^2) : polynomial in D (r27/r29 feared D^4; with N = Dn it is D^2). Needs only (G3).
 - E[Z 1_A] = (k D/n)(1 + O(D^3 e^{...}/n)) P_d: error O(k D^4 E'/n^2), polynomial times E.
 - G0 difference: n(G0(s')-G0(s)) = k(D-2) exactly; second-order term of G0 is O(B^2 D^4/n^2), polynomial.
 - Prefactor expansion: relative n^-2 error O(k^4 (1+ 1/D)... ) polynomial in k, D (F_k(N) with N = Dn).
Total: E C_k = (D-1)^k/(2k) (1 + f1(k)/n + O_k(D^4 e^{D^2/2+D} E(n,D) / n^2)).

## Theorem (proved modulo S1)
There are absolute constants c0, n0, A and, for each K, C_K, such that for n >= n0, 3 <= k <= K, 3 <= D <= c0 (ln n)^{1/4}, with nD even,
  | E C_k / ((D-1)^k/(2k)) - 1 - f1(k)/n | <= C_K exp(A D^4) / n^2,  f1(k) = k(D(5-k)+2k-8)/(2D).
(Take A = 8, c0 = 1/(20)^{1/4}... such that exp(A D^4) <= n^{1/2}; then the right side is <= C_K n^{-3/2}, and f1/n is genuinely the first-order term.) Conditions used: G1 (holds for D <= c sqrt(ln n/ln ln n)), G3 and ln E <= (1/2) ln n, the latter being binding: 8 D^4 <= (1/2) ln n.
Proof: the step list above; each constant is explicit.

## What fails beyond D ~ (ln n)^{1/4}
Exact failing step: the Bonferroni series must be truncated at L >= e^2 * (site weight) = Omega(D^4) in the r25 bookkeeping, and the sum of absolute values of the n^-2 remainders over l <= L is e^{Theta(D^4)}. Beating n^-1 (needed so f1/n is leading) requires D^4 <~ ln n. The (E3) ratio condition alone (G1) would allow D ~ sqrt(ln n/ln ln n), and replacing the crude site weight 2D^4 by the true weights D/2 (loop) and D^2/4 (double) would give error e^{O(D^2)}, plausibly D <= c sqrt(ln n) (r27). That refinement requires re-deriving the defect and free-site weights with N = Dn rather than N >= n and is NOT done here, so it is not claimed. (Note: absolute remainders also lose the true cancellation of the alternating series; getting beyond sqrt(ln n) would need the cumulant route of r29.)

## Numerics
v2/scripts/r30_range_check.py evaluates the explicit conditions G1 and ln E <= (ln n)/2 with the constants above: no admissible D >= 3 until ln n ~ 2300 (n ~ 1e1000), D=6 at n=1e10000, D=21 at 1e1000000. So the range is rigorous but practically asymptotic only; the constants (5 D^4, 3 D^2 ln ln n) are not optimised.
