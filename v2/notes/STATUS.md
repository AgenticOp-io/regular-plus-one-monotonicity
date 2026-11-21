# v2.0 status

Bar is 2.0. v1.0 is sent.

## Closed (named)

- **factor-moment** (Theorem factor-moment): every linear host with
  \(n^{1/2}=o(L)=o(n)\) and \(\min(L,D-L)=\omega(n^{1/3})\).
- **factor-rate** (Theorem factor-rate / former Conjecture factor-rate):
  complementary, dense-host, linear length, and \(n^{3/4}=o(L)\).
- **factor-rate-mid** (Theorem factor-rate-mid-fail): residue
  \(287(1-\lambda)/(216\lambda\,na)\).
- **long-step** (Theorem long-step / long-step-all).
- **unconstrained residual** (Theorem residual-unconstrained).
- **residual-moment** (Theorem residual-moment): matchings \(m=1\) on the
  McKay scale \(\delta(d+\delta)^2/n=o(1)\). The extension to
  \(1<m=o(\sqrt\delta)\) was withdrawn: the uniform-overlap factor
  \(1+O(K/\delta)\) does not control the second moment
  (Proposition overlap-mass). That range is part of
  Conjecture residual-factor-sharp.

## Open (named)

- **residual-moment-bim** (Conjecture residual-moment-bim): BIM length
  \(m=\Theta\sqrt{d\log n}\) with \(m/\sqrt\delta\to\infty\). Needs sparse MLLT /
  residual-law comparison (Proposition residual-two-gaps).
  Proposition bim-residual-scale: formal package scale
  \(\Theta(n/(\delta m))\) (conditional on residue persistence).
  Proposition package-not-persist: that residue cannot persist at \(m=1\),
  since matching variance is \(1/(6\delta^3)\to0\) while \(\Theta(n/\delta)\to\infty\).
  Proposition mllt-vanishing-margin: linear-margin weights degrade to
  \(\Theta(\lambda)\) as \(\lambda\to0\), so Theorem mllt-sparse does not transfer.
- **config-split**: open. Selection (iii) only on single orbits
  \(D\in\{1,n-2\}\). Proposition iii-two-sided:
  \(a-c_n=I_{\mathrm{low}}-I_{\mathrm{surv}}\); on \(n=6\) two-sided is
  \(0.019\,c_n\) (C₆) vs pointwise \(1.15\,c_n\); on \(n=8\) MC,
  \(C_5\cup C_3\) still \(\approx 0.09\,c_n\) below the mean.
- **Q**: open; conditional on BIM Conjecture 1.3 (Theorem process-to-Q).

## Also closed (strengthening / obstruction)

- **cycle-first-order** (Proposition cycle-first-order, 2026-11-19): for fixed D,
  \(\EE C_k=(D-1)^k/(2k)(1+f_1(k)/n+O(n^{-2}))\),
  \(f_1(k)=k(D(5-k)+2k-8)/(2D)\), with \(f_1(4)=2\). This settles the k=4 part of
  (R2\*) at fixed degree. The growing-D case is still open
  (`v2/notes/r25_lemma_L1.md`). r29 (`v2/notes/r29_growing_D_proof.md`): attempt, no new range proved; missing lemma L1' (uniform-in-D local variation of ln P(simple) to O(D/n^2)). r27 (`v2/notes/r27_growing_D.md`) is heuristic:
  the D^2/n^2 terms of ln R cancel for every host, and the same bookkeeping matches the
  exact edge and P3 probabilities. Conjecture: the same f1 holds with error
  O((D+k^2)/n^2) for D = o(n). A proof needs a log/cluster expansion or second-order
  switchings; the Bonferroni route only reaches D <= c sqrt(log n).
  r28 (`v2/notes/r28_growing_D_exact.md`) is exact numerical evidence for k=4, D=3..8:
  f1=2.000(2), and the 1/n^2 coefficient is c(D)~4, flat in D. That is stronger than O(D).

- **peel-second-moment-third** (two-sided sandwich): Lemmas avoid-overlap
  (factor case) and decomp-overlap are two-sided; Theorem
  peel-second-moment-third is now
  \(\exp(\pm C(L^3+1)/n)\) rather than a one-sided upper bound.
  Range still \(L=o(n^{1/3})\) for variance \(\to0\); the gap remains the
  averaged cubic (Proposition peel-cubic-gap).
- **package-not-persist** (Proposition package-not-persist): mid-window
  five-package residue cannot persist at matching length on sparse hosts.

## Rounds r40-r41 (2026-11-21; main.tex Remark rounds-r40-r41; all SKETCH)
- **SKETCH** r40: E3 with fresh weight (D^2-1)/4 and bundle-level free sites; r30 range
  D<=c(ln n)^{1/4} -> D<=sqrt(ln n)-4 ln ln n-O(1). Conditional on unrechecked r30/r38 items.
  sqrt(ln n) is intrinsic to absolute-value Bonferroni. Numerics reproduce (`scripts/r40_E3_check.py`).
- **SKETCH** r41: a-priori tail P(m_j>=CL^2)<=e^{-cL^2} via one-step switching + mgf; only the
  one-step bound is proof-grade. Closes r36 gap 1 at sketch level; gaps 2-4 OPEN.
  r45 (numerics): gap 3 backward map contractive; r45's L^6/n^2 total shift (=> n^{1/3}) double-counted the m-factor. r46 recount: slope error ~0.37/n^2 per step, total ~0.083 L^4/n^2 = o(1) for L=o(n^{1/2}), k<=2 clusters only; k=3 clusters (gap 2): r48 numerics (tree-like, mean overlap, x=2) give backward-map shift ~-0.031 L^5/n^3 and direct term ~L^4/(12 n^2), both o(1) for L=o(n^{1/2}); the feared n^{2/5} cap is not seen; k>=4, overlap fluctuations, rigorous signed KP still open (`notes/r45.md`, `r46.md`, `r48.md`). r47: Stein/Janson/Bethe reduce to L1'; all-edge zero-free interpolation fails numerically (`notes/r47.md`). r47: Stein/Janson/Bethe reduce to L1'; all-edge zero-free interpolation fails numerically (`notes/r47.md`). r49 (numerics, exact): Re z<=0 zero-freeness of P_H checked at n=8,9,10, D=3,4,5 on cycle/path hosts: no counterexample (max Re -0.109, nearest root to 1 >=1.11); but the claim is FALSE for D=2 and complement D=n-3 (Hamiltonian-cycle host, Re up to 3.9; r47 omitted that host) (`notes/r49.md`).
  Numerics reproduce (`scripts/r41_tail_and_x.py`; MC values vary by seed).

## Rounds r32-r38 (2026-11-21; see main.tex Remarks rounds-r32-r38, weak-law-false)

- **PROVED** r32: S1 collision/Bonferroni bound uniform in D (`notes/r32_S1_proof.md`).
  Range D <= c(ln n)^{1/4} not shrunk; binding e^{O(D^4)} is E3's site weight, untouched.
  r37: weak law <=> TV(P,P*)->0 (bounded convergence).
- **SKETCH** r38: L1 for D-regular / D-2-on-k classes via termwise Lipschitz from S1; r30 now
  rests on E3 only (E3 not re-proved; only defect-0 part numerically checked). Range unchanged.
  r35: t3 = O(L^3/n^3) under nu_L (switching) and unconditioned (R2*) on L=o(n^{1/2}).
  r36: exact one-factor identity (proved); 2nd-order cluster expansion, L^3/n is a deterministic
  coefficient matching kappa_2, residual O(L^4/n^2) (numerics, x=2 only).
  r44 correction: q_k=n^{-k}e^{phi(k)}, phi=k^2/n+psi(k), NOT product-form; plain Kotecky-Preiss does not apply
  (sketch). Gaussian-decoupling attempt on gap 2 did not close it (`notes/r44.md`); gaps 2-4 OPEN.
- **FALSE (sketch, pairing level)** r37: weak law Z/E[Z|G,deg R=g]->1 fails; Lambda shift = sqrt K,
  TV->1. Lemma avoid-G-host / residual-moment-bim in degree-conditioned form cannot be proved as
  stated; repaired target Z/E[Z|G,g,Q(H)] untouched. r33 K formula had m role-swapped; corrected
  (conclusion K/delta^2->inf stands). Simple-graph transfer not done.
- **OPEN** (R2*) past n^{1/3}: r36 gaps (overlap tail for linearisation, signed KP constants,
  recursion error propagation, kappa_k k>=3). r34: L1' (arbitrary d, D<=n^c) open; routes:
  differentiable Isaev-McKay, KP cluster expansion on D<=c n^{1/4}.

## Also open (not named)

- Peel second moment past \(n^{1/3}\) (Proposition peel-cubic-gap /
  peel-transfer-threshold). Containment and decomposition overlap are both
  two-sided; the gap remains the averaged \(O(L^3/n)\) after quadratic
  cancellation.
- Lower tail of the matching count \(Y\) (blocked routes unchanged).
- Residual-moment past McKay scale \(\delta(d+\delta)^2/n\not\to0\).

## Next

1. **Mostly closed 2026-11-11**: Theorem growing-degree-factor gives
   relvar -> 0 for every m with delta^3=o(n), min(m,delta-m)^7=o(delta^2 n),
   min(m,delta-m) <= (1/2-c) delta (covers the BIM range on the McKay
   scale). Still open there: the rate itself, the band m ~ delta/2, nearly
   regular hosts, and the residual-law comparison.
   Original item: prove Conjecture residual-factor-sharp (rate \(O(m^2/\delta^3)\), length
   \(m=o(\delta^{3/2})\), including the withdrawn range \(m=o(\sqrt\delta)\)):
   Laplace at overlap \(K\sim nm^2/(2\delta)\), not at the uniform mean
   \(\Theta(m^2)\). The switching bound \(O(\ell/(mn)+m/n)\) accumulates to
   \(\exp(O(nm^3/\delta^2))\) on that overlap and does not tend to \(1\) for
   \(m\ge 2\) (Proposition switching-sparse-mode). At BIM scales
   \(m^2/\delta^3=\Theta(1/d)\to0\) (Proposition residual-sharp-bim).
   **Fixed degree closed** (Theorem fixed-degree-factor): for fixed
   \(\delta\ge3\) and every \(1\le m\le\delta-1\), relvar \(\to
   \exp(\sum_{k\ge3}x^k/(2k))-1\), \(x=1/(\delta-1)\), the matching limit,
   \(m\)-free. The pairing second moment is an exact 1-D hypergeometric sum
   (Lemma factor-one-dim), so there is no overlap-window problem. The gap
   left for \(\delta\to\infty\) is the passage from the pairing to the simple
   graph at relative error \(o(\delta^{-3})\) (Remark fixed-degree-sharp).
   The one-dimensional overlap sum does not determine the McKay weight for
   \(m\ge 2\): \(\lambda\) depends on \(\sum(a_v-\bar a)^2\), and at the mean
   profile the linear shift of \(\lambda^2\) is \(m^2/(2\delta)+O(\delta^{-2})\)
   (Proposition overlap-not-weight). That is not yet a conditional-on-\(A\)
   estimate. At \(m=1\) the exponent at overlap \(1/\delta\) is exactly the
   loop and double-edge correction (Proposition mode-phi).
2. Tilt comparison under \(\mu_D\) / orbit-flat inverse counts → config-split.
3. Cancel the averaged cubic in the two-sided containment ratio → peel
   past \(n^{1/3}\).

See `PROGRAM.md` for the full closed/blocked ledger.
