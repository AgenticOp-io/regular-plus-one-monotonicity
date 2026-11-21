# r35: peel past n^{1/3} -- what is and is not proved

Status: **no new theorem. (R2*) is NOT closed.** The averaged cubic itself is already
cancelled (Prop peel-cubic-cancels, A+B/(2λ)−(1/λ−1)²/2 = 0), so "break the barrier" is moot:
the only open input is (R2*), uniformly for L=o(n^{1/2}). Nothing here edits main.tex.

## 1. Proved (sketch-level, elementary) : the triangle input t3 = O(L^3/n^3) under nu_L
Switching: for G a graph on [n] with max degree < L <= n^{1/2}/2 and uv an edge of K_n-G, a uniform
perfect matching M of K_n-G has P(uv in M) <= 1/(n-2-4L). Map M∋uv to M' = M-xy+ux+vy, choosing
xy∈M with ux,vy∉G: at least (n-2)/2-2L choices (x,y ordered: twice that); M' determines M
(its u- and v-partners are unique). So #(M∋uv)(n-2-4L) <= #(M without uv) <= #M.
Expose M_1..M_L conditioned on disjointness (each is uniform on K_n minus the earlier union). A
triangle uses edges from three distinct matchings, so E[Tri | D] <= C(n,3)·L³·(C/n)³ = O(L³), i.e.
t3 = O(L³/n³): exactly the hypothesis of Remark peel-kappa3. **This discharges the k=3 term of
(R2*) on L=o(n^{1/2})** (kappa3 = 5L⁴/n² + n³(t3−L³/n³)² + ..., all o(1)). The remark listed this
as open; the argument is new this round but only sketched (constants not written out).

## 2. Structural reduction (key observation, checked)
For L-regular F, the k-matching counts m_k(F), k<=2, are F-independent; m_3 = a(n,L) − Tri(F)
(exact, `v2/scripts/r35_matchpoly_tri.py`, n=24, L=4, 60 samples, slope −1, residual 0).
Fixed F1, *independent unconditioned* M'_1..M'_L:
  E[y^T | F1] = g(F1)^L,  g(F) = Σ_k (y−1)^k m_k(F)/((n−1)(n−3)…(n−2k+1)).
g is a monomer–dimer polymer gas with edge activity z=(y−1)/(n−1); each edge conflicts with <=2(L−1)
others, so Kotecky–Preiss converges for zL·C<1 (true, L<<n). Cluster terms of order k are
<= L(CL/n)^{k-1}; the k=1,2 terms are F-independent (regularity), k=3 depends on F only via Tri/n³.
So L·ln g(F1) = deterministic + O(L⁴/n² + L·Tri/n³): the **unconditioned (Poissonised) version of
(R2*) holds on L=o(n^{1/2})**, heuristically-to-sketch rigorous (cluster-expansion constants not
written out; no code verification beyond the m_3 identity).

## 3. Why this does NOT prove the peel bound
nu_L conditions on D (pairwise disjointness) in both F1 and F2. The factor E[x^K 1{M'_j ∩ U_1=∅}]
is a perfect-matching count in K_n−U1 with a forbidden set of density ~L/n: not a small-activity
gas, and Lemma avoid-overlap gives it only to relative O(L²/n) per factor, i.e. O(L³/n) total: the
original barrier, re-located. Also P(D)=exp(−L²/4+O(L³/n)) is only known to O(L³/n) and cancels
only if the same conditioning structure is matched. Closing needs a second-order (O(L/n²)-per-factor)
avoid-overlap expansion, e.g. cluster expansion of the *hole* polymer gas (matching in K_n−U is
dense; expand around the K_n matching measure with excluded-edge cluster weights of size L/n), or
a direct comparison nu_L vs the independent-matchings law with explicit Radon–Nikodym control.
Not done.

## 4. Not done / not checked
- Factorial cumulants kappa_k, k>=4 under nu_L; tail summability: only via §2 heuristic/unconditioned.
- Triangle bound constants; hole-gas expansion; the r23–r26 host formulas were not needed here
  (they concern G, not nu_L) and were not used.
- Brute force at n<=8 cannot test L-scaling.
