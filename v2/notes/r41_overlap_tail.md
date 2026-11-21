# r41: a-priori overlap tail for m_j = |F ∩ U_j| (gap 1 of r36) -- circularity broken

Status: **gap 1 closed at proof-sketch level (all steps elementary, constants not written). Gaps 2-4 of r36 untouched.**
Nothing edits main.tex.

## Key point: no induction on the peel index and no gas needed
r36 wanted a tail for m_j from Lemma decomp-overlap (only O(L^3/n)-accurate). Instead bound each *conditional one-step*
overlap X_i = |M'_i ∩ F| directly by switching (r35 §1), then sum over i<j with a martingale mgf argument.

## 1. One-step bound (switching, proved modulo constants)
M uniform PM of K_n − U, max deg(U) ≤ L' ≤ L ≤ √n/2, S ⊂ E(K_n)\U a matching with |S| = s ≤ εn. Then
  P(S ⊂ M) = Π_{i<s} P(e_i ∈ M | e_1..e_{i-1} ∈ M) ≤ (n − 2s − 2 − 4L)^{-s},
since given e_1..e_{i-1} ∈ M the rest is uniform PM of K_{n-2(i-1)} − U' (deg ≤ L) and r35 §1 applies at each step.
F has max degree ≤ L, so F has ≤ (nL/2)^k/k! k-matchings... precisely
  E C(X,k) ≤ C(nL/2,k)(n(1−3ε))^{-k} ≤ (eL/(2k(1−3ε)))^k  and  ≤ (L/(2(1−3ε)))^k/k!·(1+o(1))  (k ≤ εn).
Hence for 0 ≤ u ≤ u0: E(1+u)^X ≤ exp(uλ) + (tail k>εn, super-exponentially small), λ = (1+o(1)) L/2.
(Tail k>εn: P(X ≥ εn) ≤ (eL/(2ε(1−3ε)n)·c)^{εn}, negligible since L ≤ √n.)
So X is sub-Poisson(L/2) in mgf, *conditionally on any history* (only deg(U_i) ≤ L used).

## 2. Tilt and conditioning don't hurt
The peeling conditions on D (disjointness: already in "M uniform on K_n − U_i") and tilts by y^{X}, y ∈ [1/2, 2e] say.
Tilted mgf of (1+u)^X: E[(y(1+u))^X]/E[y^X] ≤ exp((y−1+yu)λ) (numerator by §1 with y(1+u) = 1+(y−1+yu);
denominator ≥ 1 for y ≥ 1; for y<1 use Jensen E y^X ≥ y^{EX}, EX ≤ λ).
Per step a deterministic factor e^{O(L)}; no dependence on history.

## 3. Sum over i<j: tail bound (sketch, standard)
m_j = Σ_{i<j} X_i, j ≤ L. Sequential conditioning (tower property) gives E[e^{t m_j}] ≤ exp(C_t L²), and Chernoff:
  P(m_j ≥ C L²) ≤ e^{-cL²}  (C large, c>0 depending on y-range only).
Moreover E m_j ≈ L(L−1)/2·(1−o(1)) (sub-Poisson: var < mean, see numerics). Uniform in j ≤ L and in the tilt range.
This is the circularity-free replacement: nothing here uses the gas, Lemma decomp-overlap, or earlier factors' accuracy.

## 4. Consequence for r36 linearisation
Dropped terms were ≤ L m/n² and m²/n³ per factor; on {m ≤ CL²}: ≤ C L³/n² + C² L⁴/n³ per factor, so ≤ C'L⁴/n²
after L factors = o(1) for L = o(√n) -- same order as the remainder from k≥3 clusters. On the bad event
(prob ≤ e^{-cL²}): need ln Z_j to be controlled by a crude bound ln Z_j ≤ ln E y^{X}≤ O(L)(+m-dependence ≤ O(Lm/n·…)); with
crude m ≤ nL/2 this is polynomial in n while the probability is e^{-cL²}, which is *not* enough when L² ≲ log n.
Handle by the mgf bound instead of truncation (E e^{t m} finite, tilt exponent γ m, γ = O(1/n), so e^{γ m} has mgf
≤ exp(C L²/n·…)): i.e. integrate out m exactly, not truncate. Sketched only.

## 5. Numerics (`v2/scripts/r41_tail_and_x.py`)
(b) Monte Carlo, disjoint-conditioned PMs by rejection (n=40,L=4: E m=5.78, var 5.0; n=60,L=5: E m=9.5, var 8.4;
predicted ~L(L−1)/2 = 6, 10; max ≈ 2.5× mean): sub-Poisson as claimed (small-n, not a test of the tail constants).
(a) x-scan of the r36 recursion: residual·n²/L⁴ → 0.124 (x=1.5), 0.99 (2), 6.94 (3), 49.6 (5) at n=1e6,L=300.
Bounded in L,n for every x, ≈ (x−1)³-ish (ratios ≈ 1/8, 1, 7, 50): so the residual is O(L⁴/n²) uniformly for fixed x ≠ 2
and carries the κ_3-type (x−1)³ term. Only second-order formula tested; **κ_k, k≥3 are not independently computed**
(they only appear as that bounded residual). Not checked: x growing with n.

## 6. Proved vs sketched
- Proved (elementary, iterated switching): conditional factorial-moment bound §1.
- Sketched (standard but constants/uniformity unwritten): §2 tilt, §3 tail, §4 integration of m.
- Still open from r36: gaps 2 (KP constants k≥3), 3 (error propagation through the backward recursion), 4 (κ_k, k≥3 / uniform y).
