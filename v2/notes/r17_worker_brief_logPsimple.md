# r17 worker brief: second-order expansion of log P(simple | U) and exponent of u_T

Read first: v2/notes/r16w1_R2star_status.md (incl. appended notes), v2/scripts/r16_longpath.py, v2/notes/r16_worker_brief_R2star.md.
Write only v2/notes/r17w1_* and v2/scripts/r17w1_*. Do not edit paper/main.tex. Commit when done.

## Established (numerical, nothing proved)
Pairing model: log p_U = sum_v h(d_U(v)) + f(|U|); non-star u_T = O(n^-(k-1)) there.
Simplicity conditioning adds the term log P(simple | U). Exact D=3 data: u_T(path_k) ~ n^-(k-2), k=3..6
(6-edge path still drifting at n=28, exponent uncertain).

## Do
1. Expand log P(simple | U) in the number of loops/double edges (defects), keeping the cancellations
   between defects: a naive defect count (weight ~1/n, touches <=3 path edges) predicts a slower
   decay than the data, so do NOT stop at first-order counting. Use cumulants of the defect
   indicators under the pairing measure conditioned on U, or an inclusion-exclusion with exact
   cancellation. Derive the exponent of u_T for path_k.
2. Check every claimed step numerically (exact small n, D=3, pairing model; reuse r16_longpath.py).
   Try to extend exact counts past n=28 only if a cheap faster counter is easy.
3. If it fails, state exactly which step and whether intrinsic.

Report: proved / numerically checked / not checked, separately. Do not claim an exponent the data doesn't support.
