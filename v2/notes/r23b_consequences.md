# r23b: consequences of r22b (symmetry gives exact g(H)/g(0) for some H)  -- partly PROVED, headline gap unchanged

Notation as r22b: Q(H)=g(H)*prod_v (D-h_v)!/(N-2L-1)!!, g(H)/g(0)=P(H subset G), G uniform simple D-regular on [n], m=nD/2, N=nD.

## PROVED (exact, by S_n-invariance + counting identity; hand algebra, sympy-checked)
Principle: if the number X_H(G) of copies of H in G is the same for every D-regular G, and S_n is transitive on copies of H in K_n,
then P(H subset G)=X_H/#copies(K_n) exactly. Works for: edge, every star K_{1,k} (X=n C(D,k)), and **disjoint edge pair 2K2**:
X = C(m,2) - n C(D,2)  (two edges are adjacent in exactly one way; a simple graph has n C(D,2) adjacent pairs), #copies = C(n,2)C(n-2,2)/2.
(1) Stars (r22b generalised): Q(K_{1,k})/Q(0) = prod_{i=1}^k (nD-2i+1) / (D (n-i)).  [k=1,2 match r22b/r17a]
(2) **Disjoint pair, exact:** c_n(2K2):=log[Q(2K2)Q(0)/Q(e)^2]
      = log of the following (sympy-simplified):
      (n-1)(Dn-3)(Dn-4D+2) / (D (n-3)(n-2)(Dn-1)).   (valid D>=2, n>=D+1, nD even)
    The 1/n term cancels exactly. Expansion: c_n(2K2) = -2(D-1)(D-3)/(D^2 n^2) + O(D^a/n^3).
    At D=3 the n^-2 term also vanishes => O(n^-3), explaining r17a's observed ~n^-3.5 decay.
    Check vs r17a DP (D=3): n=8,10,12,14 -> -.005814, -.002466, -.001271, -.000739; r17a table: -.00581, -.00247, -.00127, -.00074. EXACT match.
    So the "disjoint pairs interact only at n^-3" observation is now a theorem for pairs (n^-2 uniformly, n^-3 at D=3).

## Which r20 conditional items does this make unconditional?  Answer: NONE of the two listed, honestly.
- (B*) for k>=4: needs non-star connected/4-edge T; symmetry gives only X_H constant for stars and 2K2. NOT closed.
- Triangle coefficient r2(D): needs E[#triangles] (g(K3)); #triangles is not constant over D-regular graphs. NOT closed.
- One-sided j-stars / S1_1_0 (r10w3): these were already proved; r22b gives a second, exact route for the star part
  (formula (1)), but I did not verify the map between r10w3's exp-form c0 and Q(star) so I claim no new c0 statement.
- Adjacent pair coefficient c(D)=(D-2)/D: closed by r22b (the r20 "Heuristic" bullet and its doubt are resolved).
- Disjoint pair: new, closed by (2).

## Where symmetry stops: everything else reduces to ONE unknown, the triangle count
Counting adjacent/disjoint structures in a D-regular simple graph (T=#triangles):
  #P4 (3-edge paths) = m(D-1)^2 - 3T;  K2+P3 and 3K2 and C4-free combinations likewise = (explicit polynomial in n,D) + c*T (+ #C4, #P5 for larger).
So for all hosts with <=3 edges, g(H)/g(0) = (exact rational function) + (const)*E[T]/(copies), and E[T] is exactly the r2(D) unknown.
Hence the smallest gap for k=3 hosts: **E[T] to relative o(n^-2)** (i.e. r2(D)); for k=4 hosts additionally E[#C4], E[#P5-type] i.e. lemma L*.
Exact E[T] is NOT derivable by symmetry (T varies with G). This is the single smallest remaining gap, and I did not close it.

## Not done
- No attack on E[T] beyond identifying it as the hub; no numerics beyond the sympy check above; no literature check.
- (2) was verified against r17a data at D=3 only (4 points), plus the symbolic derivation.
- Candidate next step: express E[T] via the switching/Poisson relation  E[T]=(D-1)^3/6 * (1 + r1/n + r2/n^2) with r1 forced = 3(D-1)/D? (r10w3 notes r1 not independently proved); test whether the exact 2K2 and P3 formulas, plugged into the triangle-free identities for #P4 etc., force r1 (a consistency relation among Q(K3), Q(P4)).
