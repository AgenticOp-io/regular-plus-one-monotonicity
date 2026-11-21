# r38: L1 without H1-smoothness (direct termwise Lipschitz); what it does and does not make unconditional
Chosen: option B (re-derive the smoothness step of L1 using r32's S1), not L1' as a standalone. Status: **sketch-level proof of L1 for the classes used (D-regular, or D-2 on k vertices) with error B*poly(D)*e^{-G0}E(n,D)/n^2, conditional on E3 exactly as stated in r25/r30.** I did NOT independently re-verify E3 for growing D beyond re-reading it (weights look consistent; G1 is the only D-constraint). r30's theorem is therefore reduced from "S1 + C^1 smoothness of H1" to "E3 only". Not a full unconditional proof. L1' (arbitrary d, d', D up to n^c) is untouched.

## Key observation
r25/r30 prove L1 via (*) P_d = e^{G0} + H1(s)/n + O(E/n^2) with H1 C^1 in s. The C^1 norm of H1 w.r.t. the D moments s_r was only "sketched" (r32). It is not needed. Compare d, d' (both in the class, deficit B') *termwise* in the Bonferroni sum P = sum_l (-1)^l sum_{j+k=l} M_jk/(j!k!):

1. Defect >= 2 shapes: each of d and d' is already <= 2(2D^4)^l C l^{2c_D}/n^2 (E3), so the difference is too. No Lipschitz needed.
2. Defect 1 shapes (size n^-1 in E3): M_sigma = c_sigma Pi_sigma(d)/F_m(N), c_sigma >= 0 independent of d. By r32 (d), |Pi(d)-Pi(d')| <= n^v lead [vB'/n(1+v^2/2n)+v^4/8n^2]; and F_m(N)/F_m(N') = 1+O(mB/N). So the relative change is <= C l B'/n (v<=m<=2l). Hence the defect-1 sum changes by <= C l B' * (defect-1 weight <= 2(2D^4)^l R_l)/n = O(B' E/n^2) after summing over l<=L+1 (the extra l is absorbed in (L+1)^{3D^2+7}).
3. Defect 0 (vertex-disjoint shapes, exact formula M0_jk = v! e_v(f)/(2^j 4^k F_m(N)), f_u=(d_u)_2, v=m=j+2k): the leading part (sum_u f_u)^v/N^m = (s2/s1)^v/... is an exact function of s whose series is e^{G0(s)} (so G0(s')-G0(s) appears exactly, truncation tail <= 4n^-3). The remainders are: collision term -C(v,2)-type (nonneg polynomial in s, size v^2/n, relative Lipschitz vB'/n by r32(d), so change O(v^3 B'/n^2)); the N^m/F_m(N) = 1+m^2/N+... factor (change O(m^2 B'/n^2)); the Bonferroni remainder v^4/8 n^-2 (r32(c)). All are n^-2 per shape with weights (2D^4)^l/l! summing to e^{O(D^4)}.
Total: P_d' - P_d = e^{G0(s')}-e^{G0(s)} + delta, |delta| <= C B' poly(D) E(n,D)/n^2.
4. Logarithm: P_d >= e^{G0}/2 under (G3). Write P'/P = 1 + (e^{G0'}-e^{G0})/P + delta/P with e^{G0}/P = 1+O(e^{-G0}E/n); and G0'-G0 = O(B' D^2/n) (from |s'-s|). Hence
 ln P_d' - ln P_d = G0(s')-G0(s) + O(B' D^2 e^{-G0} E(n,D)/n^2), the r30 L1 error, no H1 needed.

## What this changes for r30
- S1 (proved, r32) + this termwise argument replace "mu1 sums to a smooth H1". Remaining dependence: E3 weights, G1, G3 (D <= c (ln n)^{1/4} from e^{O(D^4)} <= n^{1/2}).
- Also gives the zeroth-order L1 (P(A|e)/P = 1+O(1/n)) directly from step 2 + 3 at deficit 2.
- Does NOT extend the range: binding constraint is still the crude site weight 2D^4 in E3 (truncation L >~ e^2 D^4).

## Numerics (v2/scripts/r38_defect0_lipschitz.py, mpmath 80 digits, exact F_m(N), exact e_v)
Step 3 only (defect-0 part T0, d = D-regular vs d' = D-2 on k vertices): n^2*[(T0'-T0)-(e^{G0'}-e^{G0})] converges as n grows (n=200..3200):
 D=3: k=1 -0.376, k=4 -1.506 ; D=4: k=1 -0.374, k=4 -1.495 ; D=6: k=1 -0.039, k=4 -0.157.
So the residual is O(1/n^2), grows ~k^2 (4x for k=1->4, i.e. 4x not 16x? 1.506/0.376 = 4.0, matching B'^2 or k^2 scaling), and does not grow with D (decreases). Steps 1, 2 and the log step are not tested numerically (no exact P(simple) at large n for growing D here).

## Not done / risks
- E3 for growing D not independently re-proved; relative-Lipschitz (d) applied to shapes with r_x up to D uses r32's polynomial-with-nonneg-coefficients argument, which was only script-checked at D<=7, n<=11.
- L1' (general d, D <= n^c) remains open: this argument needs the e^{O(D^4)} E3 weights and so is confined to D <= c (ln n)^{1/4}.
