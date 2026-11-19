# r25: proof of Lemma L1 (local perturbation of P(simple)), hence f1=2 and R2*(k=4) for fixed D
Status: PROVED for fixed D. (E3) is written out in full (r26 update). The growing-D case is open: see the last section.
Constants are checked symbolically by v2/scripts/r25_cycle_f1.py (sympy), and against the r24a exact-DP Richardson values for D=3,4,5.
Literature (searched 2026-11-19): McKay-Wormald-Wysocka, EJC 11 (2004) R66, eq. (2.2), give E X_r = (d-1)^r/(2r) (1+O(r(r+d)/n)). Johnson, arXiv:1112.0704 Thm 11, gives a total-variation Poisson bound. Neither gives the explicit 1/n coefficient, and none was found elsewhere. f1(k) is not claimed new, but no source for it was found.

## Theorem
Fix D>=3 and k>=3. Let C_k be the number of k-cycles in a uniform simple D-regular graph on [n]. Then
  E C_k = (D-1)^k/(2k) * (1 + f1(k)/n + O(n^-2)),   f1(k) = k(D(5-k) + 2k - 8)/(2D).
In particular f1(4) = 2 for every D, and e1 = f1(3) = 3 - 3/D. These match r24a: f1 = 2.000007, 2.00010, 2.0021 and e1 = 1.99973, 2.25017, 2.4042 at D = 3, 4, 5.
**Corollary.** By r23a section D, R2*(k=4, all non-star connected T) holds for every fixed D.

## Notation
Fix a maximum degree Delta. Take degree sequences d on [n] with max d <= Delta and N = sum d >= n.
P_d is the uniform pairing on N points. X counts loops (pairs inside one vertex). Y counts unordered pairs of distinct pairs that join the same two distinct vertices. A pairing is simple iff X = Y = 0.
The normalized moments are s_r = n^-1 sum_v (d_v)_r for r = 1..Delta, so s ranges over a compact set K with s_1 >= 1.
Define G0(s) = -lam1 - lam2, with lam1 = s2/(2 s1) and lam2 = s2^2/(4 s1^2). For the D-regular sequence, lam1 = (D-1)/2 and lam2 = (D-1)^2/4.

**Lemma L1.** For each B there is a constant C(Delta,B) with the following property. If d and d' are on [n] and sum_v |d_v - d'_v| <= B, then
  | ln P_d'(simple) - ln P_d(simple) - [G0(s') - G0(s)] | <= C/n^2.

## Proof of L1
The claim follows from this expansion, which holds uniformly over all d in the class:
  (*)  P_d(simple) = e^{G0(s)} + H1(s)/n + O(n^-2),   with H1 a C^1 function on K.
Because e^{G0} is bounded below on K, (*) gives ln P_d = G0(s) + e^{-G0(s)} H1(s)/n + O(n^-2). Here s' - s = O(B/n), and the middle term is Lipschitz in s, so it changes by only O(n^-2). That proves L1.
The local change does not need the value of H1, only that H1 is smooth. This is why the Poisson bookkeeping of r24b was correct.

**(E1) Exact moments.** Let M_jk = E[(X)_j (Y)_k], counting ordered j-tuples of distinct loop sites and ordered k-tuples of distinct double sites. Group the point configurations by shape sigma: a multigraph H_sigma on abstract vertices V_sigma, with m = m(sigma) edges (pairs) and r_x = deg_H(x). Then
  M_jk = sum_sigma c_sigma * Pi_sigma(d) / F_m(N),   F_m(N) = prod_{i<m} (N-2i-1),   Pi_sigma(d) = sum over injective phi: V_sigma -> [n] of prod_x (d_phi(x))_{r_x}.
Here c_sigma does not depend on d. Two sites may share a pair (a triple edge), and shapes include those cases.

**(E2) Orders.** Every non-loop edge of H_sigma lies in a double site, so every adjacency in H_sigma has multiplicity >= 2. A component of H_sigma with c >= 2 vertices therefore has >= 2(c-1) >= c edges, and a component with one vertex has >= 1 loop. Hence m >= |V_sigma|.
Equality holds only when every component is a single loop or a 2-vertex double edge. Since the sites are distinct, that is exactly the vertex-disjoint shape sigma0.
Pi_sigma = n^{|V|} prod_x s_{r_x} + n^{|V|-1} * (polynomial in s) + O(|V|^4 Delta^{2m} n^{|V|-2}). The non-injective maps are handled by inclusion-exclusion over collisions. A product of (d_v)_r at one vertex is a function on {0..Delta}, so it is a linear combination of 1, (d_v)_1, ..., (d_v)_Delta, and its sum over v is n times an affine function of s.
Also N^m/F_m(N) = 1 + (polynomial in m)/n + O(m^4/n^2) for m^2 <= N.
So a shape with defect t = m - |V_sigma| contributes at order n^-t, and sigma0 contributes
  mu0_jk = (s2/2)^j (s2^2/4)^k / s1^{j+2k} = lam1^j lam2^k.
(Per ordered vertex pair, a double site has (d_u)_2 (d_w)_2 / 4 placements.)

**(E3) Uniform bound (proved).** Let l = j+k <= L+1 with L = ceil(log n), so m <= 2l = O(log n) and F_m(N) >= N^m/2 for large n.
Write l! E binom(X+Y, l) = sum over ordered l-tuples (sigma_1..sigma_l) of distinct sites of P(all present) <= 2 sum N^{-m}, where m is the number of distinct pairs in the union (tuples with clashing points have probability 0 and are dropped).
Read the tuple left to right. Site i adds p_i new pairs and q_i new vertices, so sum p_i = m and sum q_i = |V|. Classify site i:
- *fresh*: all its vertices are new (loop: q=p=1; double: q=p=2). Defect p_i - q_i = 0.
- *free*: a double site whose two pairs are both already present (q=p=0). Defect 0.
- *defect*: anything else. Then p_i - q_i >= 1. Check: a loop pair is never inside a double site and distinct loop sites are distinct pairs, so a loop at an old vertex has p=1, q=0. A double site with exactly one old vertex has q=1, and both pairs go to the new vertex, so p=2. A double site on two old vertices that is not free has p >= 1, q = 0.
So the total defect m - |V| = sum (p_i - q_i) >= t, the number of defect sites.
*Free sites are controlled by defect sites.* If site i is free, its two pairs come from two different earlier sites (one earlier site containing both would equal sigma_i). So the bundle u-w has >= 3 pairs, and some earlier site on that bundle had both vertices old with p >= 1, i.e. a defect site. A bundle has <= Delta pairs, so <= binom(Delta,2) free sites, giving f <= Delta^2 t.
*Weights.* Count choices site by site, each new pair weighted by 1/N and each new vertex by n <= N. A fresh loop weighs <= n Delta^2/N <= Delta^2. A fresh double weighs <= n^2 Delta^4/N^2 <= Delta^4. A defect site weighs <= (2l)^2 Delta^4 n^q N^{-p} <= 4 l^2 Delta^4/n, since old vertices give <= 2l choices. A free site weighs <= (2l)^2 Delta^2: two old vertices, then two of the <= Delta existing pairs between them, with no new pair or vertex. (The factor 2 for the site type, loop or double, is absorbed into the constants. 2Delta^4 >= 1, so replacing a fresh weight by 1 only loosens the bound.) Choosing which positions are defect or free gives <= binom(l,t) binom(l,f) <= l^{t+f} patterns. Hence
  l! E binom(X+Y,l) <= 2 (2Delta^4)^l sum_{t>=0} (8 l^3/n)^t sum_{f <= Delta^2 t} (8 l^3)^f
                    <= 2 (2Delta^4)^l (1 + R_l),   R_l <= sum_{t>=1} ((Delta^2+1) 2 (8l^3)^{1+Delta^2}/n)^t <= C_Delta l^{c_Delta}/n,
for l <= L+1 and n large (so the ratio is <= 1/2), with c_Delta = 3 + 3 Delta^2.
**Consequences.**
- (Truncation) E binom(X+Y, L+1) <= 4 (2Delta^4)^{L+1}/(L+1)! <= 4 (2e Delta^4/(L+1))^{L+1} = O(n^-3).
- (Defect >= 2 is O(n^-2)) Restricted to tuples with total defect >= 2 (t >= 2, or t = 1 with a site of defect 2), the same count gives <= 2 (2Delta^4)^l C l^{2c_Delta}/n^2. The extra n^{-1} in the t = 1, p-q = 2 case comes from the second new pair.
- (Defect 0 and 1 are explicit) Tuples of defect 0 are the vertex-disjoint shape sigma0 (fresh sites only, since a free site forces t >= 1). Tuples of defect 1 have t = 1 and f <= Delta^2, so they form a finite list of shapes sigma for each (j,k). Each contributes c_sigma Pi_sigma(d)/F_m(N). By the collision expansion in (E2) (two-term Bonferroni over the events phi(x) = phi(y), remainder <= binom(|V|,2)^2 Delta^{2m} n^{|V|-2}), this is n^{|V|-m} * (polynomial in s)/s1^m * (1 + O(m^4/n)).
Summing with weights 1/(j!k!): sum_l (2Delta^4)^l l^{2c_Delta}/l! < infinity. So all the polylog factors are absorbed into constants depending only on Delta.
With (E2) this gives, for m <= c sqrt(n):
  M_jk = mu0_jk + mu1_jk(s)/n + rho_jk,   |mu1|, |grad mu1| <= C^m m^2,   |rho| <= C^m m^4 / n^2,   M_jk <= 2 C^m.
Here mu1 is a rational function of s, smooth on K because s1 >= 1.

**(E4) Bonferroni.** Write P(X+Y=0) = sum_l (-1)^l E[binom(X+Y, l)], where binom(X+Y, l) = sum_{j+k=l} (X)_j (Y)_k/(j! k!). Truncate at l = L = ceil(log n), so m <= 2L << sqrt(n). The truncation error is at most sum_{j+k=L+1} M_jk/(j!k!) <= (4C)^{L+1}/(L+1)! = O(n^-3). Now substitute (E3).
- The mu0 series sums to e^{-lam1-lam2} = e^{G0}, with tail O(n^-3).
- H1 = sum (-1)^{j+k} mu1_jk/(j!k!) converges in C^1.
- The rho terms add up to O(n^-2) sum C^m m^4/(j!k!) = O(n^-2).
This proves (*), and L1 follows.

## Application: R for a k-cycle (makes r24b rigorous, for general k)
Fix a k-cycle Cyc in K_n. Each cycle vertex has (D)_2 = D(D-1) point choices, so
  P(Cyc in G) = (D(D-1))^k / F_k(N) * P_d'(A and Z=0) / P_d(simple).
Here d' is D everywhere except D-2 at the k cycle vertices, A = {X=Y=0 in the rest}, and Z counts rest pairs parallel to a cycle edge. Z has k(D-2)^2 possible sites.
- Bonferroni in Z: P(A, Z=0) = P(A) - E[Z 1_A] + O(E binom(Z,2)), and E binom(Z,2) = O(n^-2).
- E[Z 1_A] = sum_e P(e) P(A | e). Given e, the rest is a pairing on d'' (two more deficient points), with one more forbidden parallel pair. L1 at zeroth order gives P(A | e) = P_d(simple)(1+O(1/n)), so E[Z 1_A] = (k(D-2)^2/N) P_d(simple)(1 + O(1/n)).
- P_d'(A)/P_d(simple) = exp(G0(s') - G0(s)) (1+O(n^-2)) by L1, where n(s'-s) = (-2k, k[(D-2)(D-3) - D(D-1)]). This gives grad G0 = ((D-1)/2, -1/2) at the regular point, and n * Delta G0 = k(D-2).
- So R = 1 + [k(D-2) - k(D-2)^2/D]/n + O(n^-2) = 1 + 2k(D-2)/(D n) + O(n^-2). This is 6(D-2)/(Dn) for k=3, as r24a conjectured for Q(K3), and 8(D-2)/(Dn) for k=4, as r24b found.
- Prefactor: n^(k)/(2k) (D(D-1))^k / F_k(N) = (D-1)^k/(2k) (1 + [-k(k-1)/2 + k^2/D]/n + O(n^-2)).
Adding the two first-order terms gives f1(k) = -k(k-1)/2 + k^2/D + 2k - 4k/D = k(D(5-k)+2k-8)/(2D).

## Remaining gaps
- (E3) is closed (above).
- D is fixed throughout, and the D-growing regime (L up to n^{1/2}) is NOT covered. The obstruction is concrete: the free-site bound f <= Delta^2 t gives R_l ~ l^{3+3Delta^2}/n, and the Bonferroni truncation needs L >~ e^2 * 2Delta^4. Both fail already for Delta ~ log n. Growing D would need a different route, such as switchings in the McKay-Wormald-Wysocka style carried to second order, with the free-site bookkeeping replaced by bundle-level inclusion-exclusion. The exact bundle weight is (-1)^mu (1-mu) for a bundle of mu parallel pairs, since sum over covering edge sets B of K_mu of (-1)^|B| equals (-1)^mu (1-mu).
- Paper: Proposition cycle-first-order was added after Remark peel-kappa3 in v2/paper/main.tex.
