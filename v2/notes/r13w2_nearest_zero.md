# r13w2: nearest zero of P(y)=E y^T, sturdier solver

Script: `v2/scripts/r13w2_zeros.py L n [dps]`. Fixes vs r10w2:
- histogram of T=|E(G1)∩E(G2)| is an **exact integer** count (r10w2 used float64 coefficients);
- Taylor shift to w=y-1 done in exact integers;
- roots = eigenvalues of the companion matrix (`mp.eig`, 60–80 digits). No bracketing, no Durand–Kerner
  (mpmath `polyroots` failed to converge on these; that was the earlier error);
- G1 over isomorphism-class representatives (WL hash bucket + exact `is_isomorphic`), G2 over all labeled graphs;
  assert sum(hist)=N^2. Root self-check: relative residual ≤1e-60 in every run.

R = |w| of the zero nearest y=1. Results:

| L | n | N (labeled) | R | R·L/n | note |
|---|---|---|---|---|---|
| 2 | 6 | 70 | 1.3146 | 0.438 | |
| 2 | 7 | 465 | 1.5266 | 0.436 | |
| 2 | 8 | 3507 | 1.8184 | 0.455 | |
| 2 | 9 | 30016 | 1.9464 | 0.4325 | nearest zero real, w=-1.946 |
| 3 | 8 | 19355 | 1.1406 | 0.428 | |
| 3 | 6 | 70 | 1.0 | 0.5 | degenerate: zero at y=0 |
| 4 | 7 | 465 | 1.0 | 0.571 | degenerate: zero at y=0 |
| 5 | 8 | 3507 | 1.0 | 0.625 | degenerate: zero at y=0 |

Reproduces r10w2 for L=2 (≈0.44) and L=3 (≈0.43).

## How to read this
If the nearest zero scales as R ~ c·n/L, then R·L/n is roughly constant across rows. It is (≈0.43–0.45 for L=2, 0.428 for L=3), so the data are consistent with order n/L but cannot confirm it. Rows with R=1.0 are excluded from this reading.

## Caveats (honest)
- **Tiny n only.** Labeled enumeration is exponential. L=2: n≤9. L=3: only n=8 (n=10 has ~11M graphs). L=4: n=9 and L=5: n=10 not completed
  (L=4 n=9 has 286,884 labeled graphs; Python WL-hashing was too slow, killed). So **L=4,5 have no usable data** and L=3 has a single point.
- Rows with R=1.0 exactly are an artifact: when n is too small two L-regular graphs must share an edge (P(0)=0), so y=0 is a zero.
  They say nothing about (B*). (This also explains the earlier root-finder failures at L=4,5: those cases sit in this regime.)
- L=2: R·L/n ≈ 0.43–0.45 over n=6..9, essentially flat (not monotone, small-n noise). Consistent with R ~ c·n/L, c≈0.43–0.45,
  but n range 6–9 can't distinguish n/L from other slow growth. L=3 at n=8 (0.428) agrees with L=2 but is one point.
- Does not test the regime L fixed, n→∞, nor L growing with n. Supports (B*) only weakly; a larger-n test needs an
  isomorphism-class generator (e.g. nauty `geng -d L -D L`) plus Monte-Carlo/transfer-matrix overlap counts, not labeled brute force.
