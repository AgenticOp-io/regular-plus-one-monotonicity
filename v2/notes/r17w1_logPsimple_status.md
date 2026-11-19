# r17w1: log P(simple|U) expansion -- exponent of u_T(path_k) NOT determined

## Proved
Nothing rigorous. Only an algebraic fact (already in r16w1): in the pure pairing model non-star u_T = O(n^-(k-1)).

## Numerically checked (exact, D=3; scripts r17w1_pairing.py, r17w1_disj.py, r16_longpath.py rerun n=12..28)
1. Pairing part: closed-form Ursell of log p_U for P_k, n up to 112: n^{k-1} u is flat/slowly converging
   (k=3: 0.45; k=4: 0.61; k=5: 1.26; k=6: 3.46, all still decreasing slowly). So pairing part ~ n^-(k-1), positive,
   and at n=28 it is 30x (k=4) .. 10^2x (k=6) smaller than the exact u. Hence the exact u_T(path_k) is dominated by
   Ursell(log P(simple|U)) = exact u - pairing u (confirms the r16 attribution).
2. Local exponents of exact u (log ratio n=20->24->28), D=3: P3 0.9, P4 2.0, P5 3.2 (stable 16..28), P6 4.6 (stable 16..28).
   The r16 "n^-(k-2)" reading fits k=3,4 well, k=5 only roughly (3.2 vs 3), and k=6 not at all (4.6 vs 4, with no sign of flattening
   in n^4 u; n^3 u falls steeply). Sequence 1,2,3.2,4.6 does not support a clean linear law. No exponent claimed for k>=5.
3. Two disjoint edges (2e), D=3: u ~ 0.68/n (n u = .691,.688,.685,.683,.681), i.e. n^-(k-1) for k=2, as predicted by
   the pairing/Poisson algebra (inter-edge coupling only through N). Disjoint unions P2+P2, P3+e (k=4,5) change sign near n=16
   and are ~1e-4 at n=28: still pre-asymptotic; no exponent readable.

## Heuristic derivation (hand, NOT checked beyond items above)
log P(simple|U) = cluster expansion over defects B (loop at v, double edge uv, copy of a U-edge uv). U enters via stub counts
r_v = D - d_U(v) (only local) and via N = nD-1-2|U| (global, smooth, k-th difference n^-(k-1)).
- single defects (Poisson term): vertex functions F(r_v)/N, edge-parallel r_u r_v/N (touches the edges at u,v: the 3 edges of P3's
  middle-edge neighbourhood -> u(P3) ~ 1/n, matches n u -> -0.31), double edge u-x summed over free x: F(r_u)ΣF/N^2 ~ 1/n,
  with the quadratic piece (Σ_{v in V(U)} ΔF)^2/N^2 ~ n^-2 coupling two U-vertices (covers <=4 edges of a path:
  u(P4) ~ n^-2, matches data, n^2 u -> -0.82).
- To couple a third U-vertex one needs another 1/N link: guessed counts n^-3 for P5. For P6 the same counting (two edge-parallel
  defects at edges 12 and 45 coupled through N, each n^-1, link 1/n) also gives n^-3, but the data show n^-4.6 locally.
  So either the n^-3 coefficient cancels (cumulant cancellations; the brief's expected 'exact cancellation') or n<=28 is pre-asymptotic.
  I did not do the second-order cumulant (the 1/N coupling coefficient of two far defects, its U-difference) explicitly, so this
  step is unresolved. Also D=3 is degenerate (r_v<=1 at degree-2 vertices kills loops/double edges there; a free vertex
  cannot host two double edges), so a D=3 exponent may not be the large-D / growing-L one.

## Not checked
- Explicit second-order cumulants; whether the 1/N-coupled two-defect term for P6 cancels.
- D>=4 paths (counter too slow at k>=5); n>28; L-growth; any proof of an upper bound on u_T.

## Verdict
Failure of the step: I could not derive the exponent. Not shown to be intrinsic. What is supported: pairing part n^-(k-1); simple-conditioning part dominates
and is slower: k=3: n^-1, k=4: n^-2 (derived heuristically and matching); k>=5 undetermined.
