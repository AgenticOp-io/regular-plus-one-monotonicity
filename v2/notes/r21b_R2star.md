# r21b: R2* (k=4) -- NOT PROVED. Reduction to one precise lemma; no new numerics, no scripts.

## Setup (all from r17a / r20a, restated)
Residual pairing on points with degrees d_v = D - h_v (h_v = deg_U(v)), N' = N - 2|U| points, N = nD.
Q(U) = P(simple | U) = P(no loop, no double edge in residual, no residual edge parallel to an edge of U).
Defect set Dfx(U) = loops (vertex v, weight ~ C(d_v,2)/N'), double edges (pairs u,v, ~C(d_u,2)C(d_v,2)*2/N'^2),
and U-parallel edges (uv in U, weight ~ d_u d_v / N').

## What a proof by cluster/cumulant expansion would give (heuristic bookkeeping, hand-derived, unchecked)
log Q(U) = sum_{j>=1} (-1)^j-type joint cumulants of the defect indicators.
1. j=1 (first order): loops depend only on h_v (vertex-local: killed by the 4th difference over a non-star T);
   double edges not in U depend on (h_u,h_v,|U|) only through vertex-local data and N'=N-2|U|;
   U-parallel term x_e d_u d_v / (N-2|U|), expanded in |U|/N, couples e with: edges at u, at v, and (via |U|) any edge.
   Coefficient of |U|*h_u*x_e is ~ 1/N^2, and its 4th difference over a 4-edge T is nonzero but O(D^a/N^2). OK: first order is
   consistent with n^-2 and needs no cancellation. (This corrects r20a, which said first order gives zero at k=4:
   the |U|-dependence of N' gives an n^-2 contribution. Not harmful -- we only need the bound, not the coefficient.)
2. j=2: covariances of pairs of defects sharing a point; each is O(D^a/N^2) and depends on U through h's and N' -> the 4th
   difference is O(D^a/N^2) provided only O(1) such terms depend on T. They are vertex-local in the same way.
3. j>=3 and the tail: each single term is O(N^-3), but there are ~n of them, so one needs LOCALITY: terms whose defects are
   far from supp(T) (graph distance in the residual configuration) must cancel in the 4th difference. That is exactly the
   unproved statement.

## The exact missing lemma (L*)
For fixed D and U with |U| = L = o(n^{1/2}) edges, uniformly,
  log Q(U) = A(U) + B(U) + R(U),
with A, B explicit (first and second cumulant terms, vertex-local + N'-dependence as above) and
  |Delta_{e1}Delta_{e2}Delta_{e3}Delta_{e4} R| <= C(D)/n^3  (or at least o(n^-2) uniformly in 4-edge non-star T within U).
Equivalent count form: g(H)/g(empty) to relative error o(n^-2) *as a difference*, via Q(H) = g(H) prod(D-h_v)!/(N-2L-1)!! (r17a).
Weaker sufficient statement: a McKay-type asymptotic for P(simple | degrees d, forbidden graph H) with error O(D^a/n^2)
that is *smooth* (a function of d and |H| analytic in them up to the error) -- the 4th mixed difference then inherits O(n^-2).

## Why available literature does not give it (not verified; no network/literature access this run)
- McKay-Wormald 1991 (degrees o(n^{1/2}), relative error O(D^3/n) for the simple probability) is too coarse: error is n^-1,
  not n^-2, and gives no regularity in the degree sequence, so differences are not controlled.
- Liebenau-Wormald (2017+) formulas have error n^-c, c<1 unspecified; Isaev-McKay/Gao-type complex-analysis results give
  error terms for degree sequences but I have not checked whether they provide the needed explicit n^-2 expansion in d.
- A switching proof gives *bounds* on ratios g(H)/g(H') with relative error O(L D^a/n) per step (single-edge switch), not
  o(n^-2) for a 4th difference. Standard switchings do not exhibit the cancellation that a 4th difference needs; one would
  have to iterate to second order with explicit correction terms, which is the expansion in L* in disguise.

## What I could rigorously say this run
- Only the reductions above, already in r17a/r20a. The pairing-part locality (r16w1) is the only hand-proved piece.
- Nothing about k=4 with fixed small D (e.g. D=3) beyond the existing exact DP data (r16w1/r18w1: n^2*u roughly flat for P5);
  a proof for fixed D would still need an exact formula for g(H), unavailable.

## Honest status
R2* is open. Best concrete route: prove L* for fixed D by a second-order cluster expansion of the residual defect
process with an explicit locality (decay-of-correlations) bound -- i.e. a Janson/Stein-type bound that cumulants of order >=3
of defect indicators are O(n^-3) *and* factor into a sum over clusters touching T. Starting point: the Q(U) identity above.
Risk: my "first order does contribute n^-2" correction to r20a is hand-derived, unchecked by script.
