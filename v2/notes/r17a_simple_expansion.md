# r17a: P(simple | host H) second-order expansion — STATUS: numeric only (nothing proved, nothing cited)

## Exact identity (proved, elementary)
Fix H = L edges as point-level pairs. With h_v = deg_H(v), N=nD:
Q(H) := P(pairing simple | H in pairing) = g(H) * prod_v (D-h_v)! / (N-2L-1)!!, g(H)=#simple D-regular graphs containing H.
L=1 exact: Q(e)/Q(0) = (nD-1)/(nD-D), so Delta(e) = log of that = (D-1)/(nD) + O(n^-2) (checked vs DP, n=8: 23/21).
So all of Delta(H)=log Q(H)-log Q(0) reduces to g(H)/Z, i.e. the same exact-count gap as r1/R2*/r2(D).

## Literature (not verified, no access in this run; do not rely)
Candidates: McKay 1985 (Ars Combin. 19A, 15-25, symmetric 0-1 matrices with excluded entries); McKay-Wormald 1991
(Europ. J. Combin. 11/ degrees o(n^1/2), error O(D^3/n) — too weak for O(1/D) and O(L^2/n) terms);
Gao / Isaev-McKay (complex-martingale) for hosts. Hypotheses/exact statements NOT checked.

## Numeric (v2/scripts/r17a_simple_host.py, exact DP, D=3, n=8,10,12,14; reuses r16w1_cluster.count)
Connected part c(S)=Delta(S)-|S|*Delta(e):
n:        8       10      12      14
P3      .0632   .0463   .0365   .0300   (n*c: .505 .463 .438 .420 -> ~0.31/n extrapolated, i.e. O(1/n), NOT O(n^-2))
2e     -.00581 -.00247 -.00127 -.00074   (disjoint pair: decays ~n^-3.5, far below L^2/n)
3e     -.0368  -.0140  -.0068  -.0038   (decays ~n^-3.5)
tri     .0108   .0101   .0070   .0052
P4      .0927   .0627   .0470   .0374
Reading: disjoint hosts interact at ~n^-3 (relative), adjacent edges at 1/n via the shared vertex (lost free points).
So the L^2/n term is really (#adjacent pairs)/n, not L^2/n; disjoint-pair term negligible at these n.
Not done: closed form for adjacent coefficient, D>3 (DP too slow; n=16 run killed), L>=4, uniformity in L<=n^{1/2-eps}.
Blocker unchanged: no proved two-sided second-order g(H)/Z.
