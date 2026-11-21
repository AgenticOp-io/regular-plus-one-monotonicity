# r32: step S1 (collision / Bonferroni bound, uniform in D) written out
Status: **S1 is PROVED** in the form below (elementary, no D-dependence in the collision step at all). The r30 range D <= c (ln n)^{1/4} is therefore NOT shrunk by S1. What is still NOT re-verified here: the other r30 steps (E3 weights, L1 gradient/Lipschitz step, G3). Only S1 was in scope.
Numerics: v2/scripts/r32_S1_check.py (brute force, 400 random cases D<=7, n<=11, v<=4: all inequalities below hold; worst ratio to the stated remainder 0.33).

## Correction to the r30 wording
r30 (S1) bounds Sum_v (d_v)_{a+b}. That is the wrong object. A collision phi(x)=phi(y)=v contributes (d_v)_a (d_v)_b (a product, not (d_v)_{a+b}). The correct bound is simpler: (d_v)_a (d_v)_b <= (D)_a (D)_b when d_v <= D. No (D)_{a+b} <= (D)_a(D)_b step is needed.

## Setting
Shape with v vertices, vertex degrees r_1..r_v (r_x <= D, else Pi = 0 since (d)_r = 0 for r > d). d on [n] with d_u <= D and deficit B' = Sum_u (D - d_u) (the r25/r30 classes: D-regular, or D-2 on k vertices, so B' <= 2k). Define
 Pi(d) = Sum_{phi injective} prod_x (d_phi(x))_{r_x},  lead = prod_x (D)_{r_x}, S_r = Sum_u (d_u)_r, C_ab = Sum_u (d_u)_a (d_u)_b.

## Statement S1
(a) Pi <= n^v lead.
(b) Pi >= (n-B')^v lead - C(v,2) n^{v-1} lead, so 1 >= Pi/(n^v lead) >= 1 - (vB' + v^2/2)/n.
(c) Pi = prod_x S_{r_x} - Sum_{x<y} C_{r_x r_y} prod_{z != x,y} S_{r_z} + theta * (v^4/8) n^{v-2} lead, theta in [0,1].
(d) (relative Lipschitz) for d, d' of the class: |Pi(d) - Pi(d')| <= n^v lead [ v B'/n (1 + v^2/(2n)) + v^4/(8 n^2) ] (B' = max deficit; for d' = D-regular the (n)_v vs n^v mismatch adds v^2/(2n), see script).
All constants absolute: independent of D, r, n.

## Proof (line by line)
1. All summands are >= 0. For u: (d_u)_r <= (D)_r, hence S_r <= n (D)_r and C_ab <= n (D)_a (D)_b.
2. (a): dropping injectivity only adds nonnegative terms: Pi <= prod S_{r_x} <= n^v lead.
3. Deficit: (D)_r - (d)_r <= (D-d) * max_j r (D-1)_{r-1}... precisely (D)_r - (D-1)_r = r (D-1)_{r-1} = (r/D)(D)_r <= (D)_r (r <= D), and (.)_r is increasing, so (D)_r - (d)_r <= (D-d)(D)_r. Thus S_r >= (n - B')(D)_r.
4. Collision events E_xy = {phi(x)=phi(y)}. Pi = Sum_phi w(phi) 1[no E_xy]. Bonferroni (w >= 0): S0 - S1' <= Pi <= S0 - S1' + S2' where S0 = prod S_r, S1' = Sum_{x<y} Sum_phi w 1[E_xy] = Sum C_{r_x r_y} prod_{z != x,y} S_{r_z} (other coordinates unrestricted: exact), and S2' = Sum over pairs of distinct events of Sum_phi w 1[both].
5. A pair of distinct events is either x=y=z (one vertex u, weight (d_u)_a(d_u)_b(d_u)_c <= (D)_a(D)_b(D)_c) or x=y, z=w disjoint. Either way the sum is <= n^{v-2} lead (v-2 free vertex sums each <= n (D)_r, collided classes <= n lead-factors). Number of pairs <= C(C(v,2),2) <= v^4/8. This is (c).
6. (b): S1' <= C(v,2) n^{v-1} lead by step 1 and prod S >= ((n-B')^v) lead by step 3.
7. (d): write s_r = S_r/n in [(D)_r(1 - B'/n), (D)_r]. Both prod S and S1' are polynomials with nonnegative coefficients in s_q (use (d)_a(d)_b = Sum_j C(a,j)C(b,j) j! (d)_{a+b-j}, checked numerically). A monomial in <= v factors, each moved by relative <= B'/n, moves by <= v B'/n of its value at s = (D)_.; the value of S1'-part at s=(D) is <= C(v,2) n^{v-1} lead. Add the two remainders (each <= v^4/8 n^{v-2} lead). Gives (d) up to the stated absolute constants (the script verifies it with ratio <= 0.4). QED.

## Feeding into M_jk (the part S1 is for)
M_jk = Sum_sigma c_sigma Pi_sigma(d)/F_m(N), c_sigma >= 0 (counts), so (a)-(d) apply termwise. Write W_l for the E3 weight: Sum over ordered l-tuples of n^{v} lead/N^m (new vertex weight n, old <= 2l, pair weight 1/N). E3 bounds exactly this: W_l <= 2 (2D^4)^l (1+R_l) (E3 counts vertex choices as <= n per new vertex, i.e. without injectivity, so it dominates the n^v lead sum; the shape sum over sigma is the same as the tuple sum). Also 1/F_m <= 2/N^m when m^2 <= N/2 (m <= 2(L+1) ~ 30 D^4, so needs D^7 <~ n: fine for D <= (ln n)^{1/4}).
Hence, with v <= m <= 2l, the collision remainder of E binom(X+Y,l) = Sum_{j+k=l} M_jk/(j!k!) is at most
 2 l^4 * 2 (2D^4)^l (1+R_l) / (l! n^2).
Summed over l <= L+1, using Sum_l l^4 x^l/l! = e^x(x^4+6x^3+7x^2+x) <= 1.1 x^4 e^x (x = 2D^4 >= 162) and R_l <= 1/2 (condition G1):
 total collision remainder <= 110 D^16 e^{2 D^4} / n^2.
This is the polynomial-times-e^{2D^4} term, NOT the (L+1)^{3D^2+7} factor. The latter comes only from defect >= 1 shapes (E3, R_l), as r30 already had.
The explicit first-order collision term (the -S1'/n part) of a shape with defect t >= 1 is bounded by n^{-1} times the t >= 1 part of W_l, i.e. n^{-1} R_l ~ (L+1)^{3D^2+3}/n^2: again inside r30's E(n,D). The defect-0 collision term and the F_m expansion m^2/N go into mu1 (explicit, polynomial in s, positive-coefficient so (d) gives the Lipschitz bound with relative constant v B'/n).

## Verdict
- S1 holds uniformly in D with absolute constants. r30's claimed range D <= c (ln n)^{1/4} stands as far as S1 goes; the fallback range (ln n/ln ln n)^{1/4} is not needed.
- Not proved / not rechecked here: E3 itself in the D-growing regime (taken from r25/r30), the C^1/Lipschitz step of L1 beyond (d), G3. In particular the claim that mu1 sums to a smooth H1 with norm <= E(n,D) rests on (d) plus E3 and was only sketched at the level above.
- The binding exponent e^{O(D^4)} is untouched by S1 (it comes from the crude site weight 2D^4 in E3, see r30).
