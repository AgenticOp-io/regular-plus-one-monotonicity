# r25: proof of Lemma L1 (local perturbation of P(simple)), hence f1=2 and R2*(k=4) for fixed D
Status: PROVED, except that the combinatorial estimate (E3) is written at sketch level (standard shape counting, no new idea needed).
Constants are checked symbolically by v2/scripts/r25_cycle_f1.py (sympy), and against the r24a exact-DP Richardson values for D=3,4,5.
No literature search was done. The general k-cycle formula below may already be known; we do not claim it is new.

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

**(E3) Uniform bound (sketch).** The total weight sum c_sigma over shapes of defect t is at most c_sigma0 * (C m^2)^t. Each unit of defect identifies one vertex or one pair of a site with one in an earlier site, and there are <= m^2 choices.
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
- (E3) is a sketch. A full write-up needs the shape-count bound c_sigma <= c_sigma0 (C m^2)^t written out: an injection that builds shapes by successive identifications. This is routine.
- D is fixed throughout. The constants grow with Delta, so the D-growing regime (L up to n^{1/2}) is NOT covered.
- The paper (v2/paper/main.tex) is not updated yet.
