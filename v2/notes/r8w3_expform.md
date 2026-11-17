# r8w3: is the star-host exp-form coefficient c0(D) bounded in D?

**Result:** one-sided hosts: c0 bounded, exactly (j+1)^2/2 + O(1/D) [P]. Two-sided hosts: reduced to the n^-2 triangle-count coefficient; boundedness supported numerically [N]/[C] but NOT decided.

Labels: [P] proved here (symbolic, re-run), [N] numerical, [C] conjecture. main.tex untouched.
Scripts (re-run before writing): `v2/scripts/r8w3_oneside_exact.py` (sympy, ~1-2 min), `v2/scripts/r8w3_extrap.py` (seconds).
Exp-form error as in r7: err = P/(base*exp(-A-B)) - 1, c0 = lim n^2*err.

## 1. One-sided hosts are exactly solvable  [P]
Host = star of j edges at u, target uv. A random D-regular graph is vertex-transitive, so E[#(j+1)-stars at u] = C(D,j+1) gives
P(uv | star) = (D-j)/(n-1-j) EXACTLY (no asymptotics). Inserting this into the Gao exp-form (r7_run.gao) and expanding in 1/n:
the n^0 and n^-1 terms vanish identically, and
- j=1: c0 = 2(D-1)(D-3)/D^2        -> 2
- j=2: c0 = (9D^2-48D+52)/(2D^2)   -> 9/2
- j=3: c0 = 2(4D^2-24D+33)/D^2     -> 8
- j=4: c0 = (25D^2-160D+264)/(2D^2)-> 25/2
i.e. c0(D) = (j+1)^2/2 + O(1/D), a polynomial in 1/D of degree 2. This reproduces the r7 table exactly (S1_0_0: .375,.64,.83,.98,1.09,1.19,1.26 for D=4..10;
S3_0_0 D=5: 1.04 vs 1.05) -- so the r7 fits are validated there and the fit bias at D=10 is small for one-sided hosts.
Consequence [P]: for stars at one endpoint c0 is bounded in D, c0 <= (Delta+1)^2/2 (checked symbolically j<=4; the pattern (j+1)^2/2 is [C] for all j).
The earlier "saturating rational, limit ~2.1" for S1_0_0 was right; it is exactly 2.

## 2. Two-sided hosts reduce to ONE unknown, the triangle probability  [P, by symmetry; not symbolically carried out]
Paths w-u-v-x with distinct endpoints and the common-neighbour pattern u-w-v: by transitivity
P(uw,vw) = D(D-1)/((n-1)(n-2)) exactly, and (#3-paths) = 2e(D-1)^2 - 6*#triangles. So every two-sided star host's exact probability
is an affine function of E[#triangles] = ((D-1)^3/6)(1 + r1(D)/n + r2(D)/n^2 + ...). No other unknown enters. There is no
vertex-transitivity identity for E[#triangles] (not a fixed count), so no closed form: c0(S1_1_1) = r2(D) + explicit rational pieces.
Deciding boundedness of two-sided c0 is therefore equivalent to the n^-2 coefficient of the triangle count of G(n,D) as D grows. Not computed analytically
(needs second-order switching/saddle point; not done).

## 3. Data vs analytic structure  [N]
One-sided data are polynomials in 1/D of degree 2 (exact). Two-sided data D=3..10 (r7_data) fitted by a + b/D + c/D^2 (D>=5, r8w3_extrap.py):
free limit vs conjecture L=(j+k+w+1)^2/2 (w = common leaves), rms of fit:
S1_1_0 free 4.27 (L=4.5); S1_1_1 free 8.01 (L=8), rms .013; S2_1_0 7.45 (8); S2_1_1 12.0 (12.5); S2_2_0 11.2 (12.5); S2_2_1 16.8 (18); S2_2_2 23.3 (24.5).
Pinning the limit at L costs only rms .01-.09 (comparable to fit bias, 0.05-0.35 at D=7..10 per r7). Larger hosts (S3,S4) extrapolate too unstably to test.
- The "a + b ln D" fit of r7 for S1_1_1 (b=4.35) is NOT needed: the same 8 points are fit as well by 8 - 49/D + ... with the pinned limit 8. A degree-2 polynomial in 1/D
  is exactly the form of the one-sided truth, and its slow approach (c0(10) is only 39% of L) mimics log growth over D=5..10. So log growth is not supported;
  the data are consistent with [C] sup_D c0(D) = (j+k+w+1)^2/2 < infinity for star hosts.
- Caveat: this is extrapolation from D<=10 with c0 reaching only 40-60% of the conjectured limit for two-sided hosts. A slowly growing (log or D^eps) term cannot be
  excluded by this data, and I have no analytic proof. Status of boundedness: [C], supported by one-sided [P] and two-sided [N], NOT decided for two-sided hosts.

[C] Conjecture B': for a host H1 touching u,v with Delta_H = max degree, exp-form relative error = c(H1,D)/n^2 + O(D^3/n^3) with
|c| <= (2Delta_H+1)^2 (or (3 Delta_H+1)^2/2 using w<=Delta_H), uniform in D. Far hosts: 1/2.

## 4. What exp-form Thm 6 would need to push the sharp rate past n^{1/5}  [C, bookkeeping from worker3_sharp_boundary Round 2]
Gao20 Thm 6 per-edge relative error O(D^2/n^2) summed over e = mn edges gives D^2 m/n, binding the coefficient 1/(6 delta^3) at delta^5 m = o(n) (n^{1/5}).
Replace it by "Thm 6-exp": P(uv | H1,H2) = base*exp(-A-B)*(1 + O((1+Delta_H^2) L(D)/n^2 + D^3/n^3)), with Delta_H <= 2m for H = F1 u F2.
Summed over mn edges: error m(1+m^2) L(delta)/n. Requirement delta^3 * m^3 L(delta) = o(n) (resolve 1/(6 delta^3)).
- L = O(1) (uniform c0, what the data suggest): m=O(1): delta = o(n^{1/3}); the n^{1/3} is then capped by budget (iv) n^{1/4} in the worker3 table
  => net sharp range delta = o(n^{1/4}) (m=O(1)).  Not n^{1/3} unless (iv) is also improved.
- L = delta^a: delta^{3+a} = o(n) at m=O(1). Target n^{1/4} needs only a < 1; a=2 (= Thm 6 as stated) gives n^{1/5}. So log D, or D^{1-eps}, growth of c0 would still reach n^{1/4}; only c0 ~ D^{>=1} kills the gain.
So to claim n^{1/4} one needs: (a) the exp-form Thm 6 with Delta_H^2 L(D)/n^2 error, L(D) = O(D^{1-eps}) -- the missing proof ingredient is the local second-order switching
at u,v (r6 item 5), including the cross terms between N(u) and N(v) (common neighbours), which is exactly the triangle n^-2 coefficient of section 2;
(b) the n^-3 remainder D^3/n^3 per edge (total delta^6 m/n^2, harmless below n^{1/3}); (c) Delta_H^2 ~ m^2 bounded or small vs delta^3 (m^3 delta^3 = o(n)); (d) budget (iv).
Far-part hosts (c0 = 1/2, D-free, r6) need no new ingredient.

## Not done
No analytic derivation of c0 for two-sided hosts; no D>10; the far parts of large H1 together with u,v stars; no proof of (j+1)^2/2 for all j.
