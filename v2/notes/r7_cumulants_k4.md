# r7: numerical check of (B*) at k>=4; status of the 4-edge second-order program

Labels: [P] proved, [N] numerical, [C] conjecture/heuristic, [O] open. main.tex not edited.
(B*): |kappa_k| <= C^k k! L^{k+1}/n^{k-1}, kappa_k = FACTORIAL cumulants of T=|F1 cap F2|,
log E[y^T] = sum w^k kappa_k/k!, m_k = E(T)_k = k! sum_{|S|=k} p_S^2.

## 1. What was run [N]
`v2/scripts/r7_kappa_exact.py n L K` : exact enumeration of all unordered L-sets of disjoint perfect matchings of K_n,
exact p_S per isomorphism class of k-edge S (networkx), exact Fractions for m_k -> kappa_k. Nothing sampled.
Reached: n=8, L=2..5 (k<=5 for L=2,3; k<=4 for L=4,5); n=10, L=2,3 (k<=4). n=10, L=4 did not finish (10 min timeout, not retried).
Table: kappa_k / (k! L^{k+1}/n^{k-1}) (the constant C^k that (B*) would need):

| n,L  | k=2   | k=3   | k=4    | k=5   |
|------|-------|-------|--------|-------|
| 8,2  | -.327 | .205  | .113   | -.865 |
| 8,3  | -.414 | .440  | -.510  | .542  |
| 8,4  | -.425 | .472  | -.621  |       |
| 8,5  | -.405 | .415  | -.491  |       |
| 10,2 | -.309 | .183  | .034   |       |
| 10,3 | -.397 | .406  | -.434  |       |

Raw kappa_4: n=8: .169, -5.80, -29.8, -71.9 (L=2..5); n=10: .0264, -2.53 (L=2,3). Sign of kappa_k alternates with k for L>=3.

## 2. What this does and does not show
- [N] No violation: for every case run the normalised ratio is O(1) (|.|<=~0.9, k=4: <=0.62), roughly constant in L at fixed n (L=3,4,5 at n=8),
  and for L=3, n=8->10 it moves .51->.43 at k=4 (and .44->.41 at k=3, .41->.40 at k=2), i.e. consistent with the L^{k+1}/n^{k-1} scale.
- This is WEAK evidence. n<=10 is far from the regime (L>=n^{1/3} with n large); two values of n cannot fix an exponent in n.
  L=2 is degenerate (kappa_4 drops 6.4x from n=8 to 10, faster than n^-3, a finite-size effect, not a counterexample or support).
  The ratios at k=5, L=2, n=8 (-.87) show the constant C^k need not be small. k>=5 essentially unchecked.
- [N] Sanity: kappa_1=E T=n(n-1)/2 (L/(n-1))^2 matches (e.g. 2.2857, 5.1429 at n=8).
- Larger n is not reachable by this brute force (sets of disjoint matchings grow ~ n!!^L). A reachable extension would be exact p_S for
  the 11 four-edge classes via the r5w3/r6 degree-class DP, which handles only regular/few-degree structure, not general S: not done.

## 3. Second-order asymptotics for 4-edge subgraphs [O] (not done; what is clear)
Four-edge classes without isolated vertices: K1,4, P5, C4, paw (triangle+pendant), fork (K1,3 with one subdivided edge), K1,3+K2, P4+K2,
P3+P3, P3+2K2, triangle+K2, 4K2 (11 total). Regularity of nu fixes p_S exactly for stars and for P3-components only partially
(r4 Sec.0: p_{P3}=C(L,2)/C(n-1,2)); triangle t3 has only the Theorem-A upper bound; C4, P4, P5, paw etc. have NO known two-sided asymptotics.
kappa_4 is a cancellation: m_4 ~ (L^2/2)^4 vs kappa_4 ~ L^5/n^3, so each p_S is needed with relative error o(L^-?) ~ n^-3 in its
connected part. No such expansion exists in the repo and I did not derive one. I found no argument that it fails either; (B*) remains [O].
The data above are the only new k>=4 information, and they are [N] at n<=10.

## 4. Next steps (concrete)
1. Get kappa_4 exactly at n=12 (L=2 via 2-regular-graph weights, L=3 needs a smarter count) to see the n-exponent for fixed L.
2. Compute p_S per 4-edge class at n=8,10 (reuse script internals) and fit the n^-1, n^-2 relative corrections to guess the cluster terms phi_C.
3. Only then attempt a McKay-type second-order proof for the classes whose phi_C is nonzero.
