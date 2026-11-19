# r20a: R2*(k=4) exact statement -- NOT PROVED; structural reduction only

## Proved (elementary, hand-derived, not machine-checked)
Pairing part of log p_U is vertex-local + f(|U|) (r16w1): its 4th difference over a non-star connected T is O(n^-3).
So R2* (k=4, non-star) <=> 4th finite difference of log Q(U)=log P(simple|U) over T is O(D^a/n^2).
Heuristic first-order picture (NOT a proof): log Q(U) ~ -lambda(U), lambda = expected loops+double edges given U.
 - loop terms are vertex-local in h_v=deg_U(v): 4th difference vanishes for non-star T.
 - double-edge term for a host edge uv is ~(D-h_u)(D-h_v)/N: it couples edges at u, at v and uv itself, so it has
   nonzero difference only for |T|<=3 (P3 at order 1/(nD)). Hence for k=4 first order contributes ZERO to non-star T;
   the n^-2 must come from second-order (pairs of defects / lost free points), which I did not expand.
 - This explains why k=3 has n^-1 = n^-(k-2) and suggests k=4 at n^-2, consistent with r16w1 data (n^2 u flat for P5 at D=3).

## Numeric
Nothing new run. Naive check: first-order P3 prediction u_P3 ~ -1/(nD) gives -0.11/n at D=3 vs exact data n*u ~ -0.31 (r16w1)
-> first-order picture is incomplete even at k=3 (factor ~3 off); do not use it to state a constant.

## Not checked / open
- Bound on g(H)/g(empty) to relative O(D^a/n^2) for |H|<=4 (r17a identity): not attempted beyond the reduction above;
  needs two-sided rigorous count of simple D-regular graphs containing H (McKay-type), not available.
- Exponent a in D^a, any L growth, C4 / tri+pend constants (r16w1: n^2 u ~ -2 at D=3, still drifting).
- No counterexample found; no shape where n^-2 fails except stars (degree saturation).
