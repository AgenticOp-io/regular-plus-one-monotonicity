# r22b: EXACT closed form for the adjacent-pair coefficient  (PROVED, no asymptotic enumeration needed)

Setup (r17a): Q(H)=P(pairing simple | H in pairing)=g(H)*prod_v (D-h_v)!/(N-2L-1)!!, N=nD, g(H)=#simple D-regular labelled graphs containing H.
c_n(D) := log[ Q(P3) Q(0) / Q(e)^2 ]  (= Delta(P3)-2Delta(e), Delta(H)=log Q(H)/Q(0)).  Assume D>=2, nD even, n>=D+1 (so regular graphs exist, G nonempty).

## Key step: g(H)/g(0) = P(H subset G), G uniform simple D-regular graph. For e and P3 this is exact by symmetry.
The symmetric group S_n acts on the set of D-regular graphs, so the law of G is invariant under relabelling.
- e=uv: E[#edges]=nD/2 over C(n,2) pairs, all equally likely => P(uv in G)=D/(n-1).
- P3 = {uv,vw}: E[#cherries (centre, unordered pair of neighbours)] = n*C(D,2) exactly (every graph has this many), over n*C(n-1,2) possible cherries, all equally likely by S_n-invariance (S_n is transitive on cherries) => P(uv,vw in G)=C(D,2)/C(n-1,2)=D(D-1)/((n-1)(n-2)).
(Same works for every star K_{1,k}: P=C(D,k)/C(n-1,k). It does NOT give disjoint pairs, triangles, P4: those need genuine enumeration.)

## Exact Q ratios (prefactor: vertex factors (D-h)!/D!, and (N-1)!!/(N-2L-1)!!)
- e: Q(e)/Q(0) = D/(n-1) * (1/D^2) * (N-1) = (N-1)/(D(n-1))   [matches r17a: (nD-1)/(nD-D)]
- P3: vertex factors: centre (D-2)!/D!=1/(D(D-1)), two leaves 1/D each; (N-1)(N-3). So
  Q(P3)/Q(0) = D(D-1)/((n-1)(n-2)) * 1/(D^3(D-1)) * (N-1)(N-3) = (N-1)(N-3)/(D^2 (n-1)(n-2)).
Hence  Q(P3)Q(0)/Q(e)^2 = (N-3)(n-1) / ((N-1)(n-2)),  i.e.

  **c_n(D) = log[ (nD-3)(n-1) / ((nD-1)(n-2)) ] = log(1 - 2/(nD-1)) + log(1 + 1/(n-2))**   (EXACT, all n,D with D>=2)

(The log(D/(D-1)) from the vertex factors cancels the log((D-1)/D) from g.)

## Consequence
n c_n(D) = (D-2)/D + O(1/n), error uniform in D (|error| <= C/n, C absolute: expand both logs, -2n/(nD-1) = -2/D + O(1/(nD^2)), n/(n-2)-type term = 1 + O(1/n)).
In particular c(D)=(D-2)/D rigorously, for every fixed D and for D up to n^{1-eps} (even D=o(n)), no McKay-type asymptotics, no cluster expansion needed.
Corrections: c_n = (D-2)/(nD) + O(1/n^2) with explicit second term from log expansion.

## Numerical check (matches r21a to all printed digits)
D=3,n=20: 1083/1062 -> log=.019581, n*c=.3916 (r21a .3916). D=3,n=100: 29403/29302 -> n*c=.3441 (r21a .3441).
Not re-run for D=4..6 (same formula, same one-line check).

## Corrects/closes
- r20b's heuristic (D-2)/D: now a theorem (for the exact quantity c_n). r21a's "b~1.07" fit is just the 1/n term of the closed form.
- r21a/r20a sign confusion: moot, c_n is defined above as log of the explicit ratio, positive for D>=3.

## Not done / caveats
- Only the exact adjacent-pair (P3) coefficient. Disjoint pairs, triangle, P4, L>=4 still need real enumeration (g(H) not given by symmetry). However: star hosts K_{1,k} of any size are now exactly computable via the same two lines, which may serve the R2* star-host case (r7_star_hosts).
- I did not use the web/McKay literature: it was unnecessary.
- Assumes regular graphs exist (nD even, n>D). Check of the algebra done by hand and against two r21a data points only.
