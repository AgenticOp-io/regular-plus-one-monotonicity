# r6: exact computation of the exp-form (Conjecture B) ratio -- PLAN (stub, updated below)

Status labels used: **proved** / **numerical** / **conjecture**.  main.tex untouched.

## Plan
1. Faster/more general exact engine `v2/scripts/r6_exact.py`: same degree-class DP N(c) as r5w3 but (a) any host
   (edge list, u, v), (b) many hosts per process sharing the memo, (c) multiprocessing over (D, host, n), (d) floats-free (exact ints).
2. Refit n^2*err_exp and n^2*err_prod on larger n / D, adversarial hosts (irregular, dense stars, mixed degrees, |H1|~8-10).
3. Extract the explicit n^-2 coefficient c(H1,u,v) of the exp form from the data; guess closed form in host statistics.
4. Second-order switching proof attempt for that coefficient.

## Results (all **numerical** unless marked)
Engine: `v2/scripts/r6_exact.py D n.. [-- hosts]` (exact big-int degree-class DP of r5w3, 24 host families, 8 processes);
fit: `v2/scripts/r6_fit.py` (least squares n^2*err = c0 + c1/n + c2/n^2). Raw data `notes/r6_data/d{3,4,5,6}.txt`.
Reach: D=3 n<=100 (9 s), D=4 n<=50 (45 s), D=5 n<=36 (3 min), D=6 n<=28 (~10 min). This is only modestly beyond r5 (n<=28):
r5's "too slow" was pessimistic, but the class-count state space grows like n^D, so D>=7 or n>~100 needs a genuinely new method
(NOT done: no generating-function/symmetric-function recursion was built; I did not try).

1. **Far hosts: c0 = 1/2 exactly** (numerical). For hosts whose vertices are all non-adjacent to u,v (empty, match3/6, triangle,
   K4, K_{2,3}, 6-path, far hubs of degree 2..D) the exp-form error is n^-2 * (0.50 +- 0.03) for D=3..6, independent of D and of
   the host (D=3, n<=100: 0.498-0.502 for tri/K4/K23/hub/path6; larger hosts converge slowly because of |H|^2/n corrections, e.g.
   match6 0.477). The product form on the same hosts: c0 = D^2-D+1 (7, 13, 21, 31 -- fits 7.00, 13.0, 21.0, 31.1).
2. **Hosts touching u or v: c0 depends on the local degrees, bounded and non-D^2** (numerical). Edge at u: D=3..6 -> 0, .375, .64, .83
   (increasing slowly, ~1 limit?). Star of j edges at u: D=6, j=1..5 -> .83, 1.23, 1.86, 2.94, 4.69 (grows with j=Delta, like
   (j+1)^2/8..; product form 35.6..61.2 grows like D^2 + stuff). Common neighbour of u,v: -2.0, -.91, .09, .91 (D=3..6): c0 is
   NEGATIVE for small D and drifts upward with D -- so c0 is a nonconstant rational function of D at u,v-incident hosts, not
   D-free as in the far case. Larger D needed to know whether it saturates: this is the one place where "D-uniform O(1+Delta^2)"
   is not settled by the data (D<=6 only; fits at D=6 have n<=28 so c0 uncertain by ~0.1).
3. **No counterexample found** to error O((1+Delta)/n^2 + D^3/n^3) on 24 hosts incl. irregular/mixed ('mix': 2 stars + triangle
   + edge at v + disjoint edge: c0 = -2.65, -1.22, -.17 at D=3,4,5), double stars, K4, K_{2,3}, 6-edge matchings and paths. The
   largest |c0| seen is 5.5 (star_both3, D=4) = star at both ends exhausting residual degree; as Delta -> D these cases have
   d~_u -> 1, where Gao's own expansion degenerates. Hosts with |H1|~m and Delta>>1 were NOT reached.
4. Conjectured structure (**conjecture**): c0(H1,u,v,D) = 1/2 + sum of local terms supported on N_H(u) u N_H(v), rational in the
   residual degrees d~_u, d~_v, D. Not extracted in closed form: D<=6 gives too few points per family to pin a rational
   function (e.g. edge at u: 0, 3/8, ~.64, ~.83 fits 1 - 2/(D-1)... only roughly). Need D=7..10 (new engine).
5. Proof (second-order switching): **not done.** What the data say it must contain: the far-host 1/2 equals the empty-host value
   (r4: exactly 1/(2n^2)+1/(3n^3)), so a proof can proceed by showing the far part of H1 contributes only through A,B (W-sum),
   and the remaining work is a local computation at u and v. No rigorous step added.

STATUS: Conjecture B stays a **conjecture**; evidence now 24 hosts, D=3..6, n up to 100 (D=3). Budget table unchanged.
NEXT: (i) D>=7 and n~100 via a truly faster counter (e.g. truncated saddle-point/Isaev-McKay count, or C++ with scaled doubles);
(ii) pin c0 at u,v-incident hosts as a rational function of D; (iii) the local second-order switching at u and v.
