# r16w1: R2* 4-edge p_S expansion -- NOTHING PROVED; numerical scaling check only

## Proved
Nothing new. No two-sided second-order expansion of p_S for 4-edge S was obtained, in either direction.
The missing inequality is the same as in r15w3: P(S in G) for G uniform L-regular to relative error o(n^-2) (resp.
(L/n)^a with a>=3 uniformly in L<n^{1/2}). It needs the matching-avoidance count of an L-regular host to second order;
the pairing-model part is algebra, the conditioning on "simple" is the unproved part. I could not isolate a single
inequality that fails, so I cannot claim it is intrinsic; I only know the switching/avoidance route stops at n^{1/3}.

## Numerically checked (exact, fixed D only; v2/scripts/r16w1_ursell.py, output r16w1_ursell_out.txt)
Exact p_S = P(S subset G), G uniform D-regular on n vertices (D=3: n=12..28; D=4: n=14..22), via r5w3_exact.contains.
Ursell (connected log-cumulant) u_T = sum_{U<=T} (-1)^{|T|-|U|} log p_U.
- Disjoint-edge shapes (M4) have u_T -> 0 fast (|n^3 u| shrinks 0.86, 0.32, 0.06, then changes sign at n=28): consistent with
  independence up to small corrections. Not a clean rate.
- Connected, non-saturated shapes at fixed D scale like n^{-(k-2)}, not n^{-(k-1)}:
  P2 (k=2): u -> const (-0.37, D=3); P3 (k=3): n*u -> -0.31 ; tri: n*u -> ~-1.06 ; P5 (k=4): n^2 u -> -0.82 (flat n=16..28, D=3).
  C4, tri+pend (k=4): n^2 u ~ -2.1, -1.7, still drifting slowly (D=3); D=4 P5 still drifting (-0.36..-0.45).
- Saturated stars (K1,3 at D=3, K1,4 at D=4: all slots of a vertex) have u not small at all (L-degenerate, as expected).
So with p_e = L/(n-1) held as the normalisation, the literal reading "connected correction of order (c/n)^{|C|-1}" for
the log-Ursell u_T of a connected k-edge cluster is NOT what fixed-D data show: they show n^{-(k-2)} (one power weaker).
Whether this contradicts (B*) is NOT determined: kappa_k sums over vertex placements (extra n factors per vertex) and
the r6 reduction fixes the normalisation; I did not re-derive that map. Please check it before basing a proof on
"(c/n)^{|C|-1}" per Ursell term. Also fixed D says nothing about L growth.

## Not checked
- Any L-dependence (L ~ n^{1/3}..n^{1/2}); exact enumeration cannot reach it. No MC run.
- The map between u_T decay and the kappa_k bound (see above).
- Exponents beyond n=28 (D=3) / n=22 (D=4); fits are by eye, not extrapolated.
- McKay-type subgraph-probability asymptotics from the literature were not looked up or verified here.

## Follow-up (hand derivation, not machine-checked): pairing-model Ursell terms
Pairing model: p_U = prod_v (D)_{d_U(v)} / prod_{i<|U|}(nD-1-2i) (before conditioning on simple).
log p_U = sum_v h(d_U(v)) + f(|U|). Ursell u_T = k-th finite difference over edges of T.
- f(|U|): k-th difference of f = (k-1)-th difference of g(i)=-log(nD-1-2i) = O(n^{-(k-1)}).
- vertex terms: k-th difference of h(count at v) vanishes unless ALL k edges of T meet v (star). So for non-star T, k>=3: u_T = O(n^{-(k-1)}), exactly the brief's reading.
So the extra power seen at fixed D (n^{-(k-2)}) is NOT from the pairing algebra; it must come from conditioning on "simple"
(P(simple | U) depends on U through local defects). Placement counts (n^{k+1} trees) are separate from this and don't alter per-shape u_T.
Open: expand log P(simple | U) to the order needed; this is the same unproved step as r15w3. Still no L-growth check.

## r16 follow-up: long paths, exact (D=3, n=12..28) — `v2/scripts/r16_longpath.py`
Tested my naive first-order-defect guess (connected clusters of <=2m+1 edges at order n^-m, i.e. u ~ n^-ceil((k-1)/2)): **wrong**, it predicts too slow a decay.
Exact data for path P_k (k edges), D=3: n^{k-2}·u_T is roughly flat (slowly drifting down in magnitude):
- k=5: n^3 u = -3.36, -3.37, -3.23, -3.12, -3.03 (n=12,16,20,24,28)
- k=6: n^4 u = -17.6, -17.3, -15.1, -13.4, -12.2
(k=3,4 earlier: n^{k-2} u flat ~ -0.2 / -0.43 at D=4.) So u_T ~ n^{-(k-2)} for k=3..6, one power weaker than the (c/n)^{k-1} reading, and NOT n^-ceil((k-1)/2).
Not explained analytically: simplicity conditioning gives the extra power, but the expansion of log P(simple|U) hasn't been done. Drift in k=6 suggests the asymptotic regime isn't reached by n=28 (constant may be shrinking, i.e. true exponent could be steeper). Nothing proved; (B*) exponent `a` still undetermined. Next: second-order expansion of log P(simple|U), or exact data at n>28 (needs a faster counter than r5w3_exact).
