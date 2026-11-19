# r22c: R2* for FIXED D -- NOT PROVED. Literature check + a concrete route. No new numerics.

## Claim sought
Fixed D>=3, U fixed (|U|=L=O(1)) set of edges, T a 4-edge non-star subset: the 4th difference of log Q(U), Q=P(simple|U), is O(1/n^2).

## Literature (web search, abstracts/snippets only; theorem statements NOT read)
- McKay 1985 / McKay-Wormald 1991: simple-probability and counts, relative error O(D^3/n)-type: n^-1, no smoothness in the degrees -> too coarse for a 4th difference.
- McKay, "Subgraphs of dense random graphs with specified degrees" (CPC 2011, arXiv 1002.3018), and Greenhill-Isaev-McKay "Subgraph counts for dense random graphs with specified degrees" (CPC 2021): dense regime; regular-subgraph corollary error n^(-1/2+eta). Not fixed D.
- Larkin-McKay-Tian (arXiv 2510.24276, 2025): forbidden edges/subgraphs; may contain the McKay "no common edges" asymptotics. Unread -- first thing to check; likely still dense/high-degree range and error not n^-2.
- Found NO source giving #D-regular graphs containing/avoiding fixed H with explicit n^-2 (or full-expansion) error for fixed D.

## Concrete route for fixed D (sketch, not carried out)
The pairing/exact count of simple graphs with degrees d (d_v = D-h_v bounded) and forbidden set H is a coefficient extraction
[prod x_v^{d_v}] of an exponential-type generating function (inclusion-exclusion over loops/multi-edges, Gessel/Read style).
For bounded degree this makes g(H), for each fixed local type of H, a holonomic (P-recursive) sequence in n, hence with a full
asymptotic expansion in 1/n (Bender-Canfield 1978 for H=empty gives P(simple)=exp(-(D^2-1)/4)(1+O(1/n))). If one shows:
 (i) for each isomorphism type of host H on <=8 vertices the ratio g(H)/g(empty) has an expansion a_0+a_1/n+a_2/n^2+O(n^-3), and
 (ii) the expansion coefficients are polynomial in the vertex-disjoint component data (locality),
then the 4th difference over T (which only sees O(1) vertices) is computed from finitely many expansions and the n^-1 term cancels
by the pairing-locality of r16w1/r20a; n^-2 is then the leading surviving order. Step (i) is plausible but requires a
uniform-in-H holonomy/saddle argument I have not done; step (ii) is exactly lemma L* of r21b. So the gap is unchanged.

## Verified-against-data status
r21a data (c(D)=(D-2)/D, D=3..6, n up to 100) is a k=3 check only; it supports the expansion-in-1/n picture (clean fits with
n*c = a + b/n + c2/n^2) but is not evidence for the k=4 bound beyond consistency. No k=4 exact data produced in this run.

## Honest status
R2* for fixed D remains OPEN. Gap: a fixed-D asymptotic expansion of g(H) with error o(n^-2), uniform over bounded H.
Next steps: (1) read Larkin-McKay-Tian theorems for the fixed-D range; (2) try to get g(H) for |H|<=4 edges via the Bender-Canfield
generating function and check n^-2 scaling of the 4th difference with exact DP (extend r21a_cD.py to k=4 T's);
(3) otherwise attack L* by cluster expansion as in r21b.
