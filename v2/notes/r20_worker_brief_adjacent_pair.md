# r20 brief B: adjacent-pair coefficient for general D
Read first: r17a_simple_expansion.md (disjoint pairs ~n^-3, adjacent pairs ~1/n via shared vertex; closed form not found; D>3 DP too slow).
Write only v2/notes/r20b_* and v2/scripts/r20b_*. Do not edit paper/main.tex.
## Goal
Let e,f share one vertex. Find the exact coefficient c(D) in
  log P(simple | e,f present) - log P(simple | e) - log P(simple | f) + log P(simple) = c(D)/n + O(D^b/n^2),
as an explicit function of D (and verify it at D=3,4,5,6). Cheap route: exact expansion of P(simple) via loops/double-edges
count (Poisson-type, McKay-Wormald) with the two edges' vertices' remaining D-1 or D-2 stubs; avoid the full DP.
Report proved / numeric / not checked. Commit on your branch.
