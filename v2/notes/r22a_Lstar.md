# r22a: Lemma L* -- NOT PROVED. What is and is not established.

No new theorem this run. No numerics run, no literature/web search performed (so (3) of the brief is NOT done;
claims about Isaev-McKay / Liebenau-Wormald / McKay's subgraph paper below are from memory, unverified).

## Rigorous (elementary, exact)
Notation as r21b: residual pairing on N'=N-2L points, degrees d_v=D-h_v. Let F be the finite family of defects
(loops at v; double edges {u,v}; U-parallel edges e in U). Defects are *events on disjoint-or-overlapping point sets*.
Exact inclusion-exclusion: Q(U) = sum_{S subset F compatible} (-1)^{|S|} * w(S) * (N'-2m(S)-1)!!/(N'-1)!!,
where m(S) = number of pairs forced and w(S) = number of ways to realise S (product of binomials in d_v). So:
 (a) Q(U) is an *explicit finite-degree-in-defects* alternating sum; truncating at order J has error <= (expected #defect-sets of
     size J+1) = O((D^2... )^{J+1}/ (J+1)!) only when expected defect count lambda=O(D^2) is bounded -- true for fixed D
     (Bonferroni, rigorous), but the error is O(1) not O(n^-3): it gives NO locality. 
 (b) log Q = sum of joint cumulants is the same statement; it is formal until a convergence/decay estimate is proved.
Nothing in (a),(b) yields the n^-2 bound on the 4th difference; they only restate L*.

## Why each proposed route stops
(1) Cluster expansion / Kotecky-Preiss: needs a polymer gas with a *product* reference measure. The pairing measure is a uniform
    perfect matching (global hard constraint: points used once). Standard trick = Poissonisation / conditioning on degrees
    (Stein-Chen for matchings, Janson-type): gives total-variation errors O(D^a/n) for the *number* of defects, not
    cumulant bounds of order n^-3 with locality. Producing those is a research-paper-sized computation; I did not do it.
(2) Switching: single switchings give g(H)/g(H') = (1+O(L D^a/n)) ratios. A 4th difference needs relative accuracy n^-2 with
    smoothness in H; switchings give bounds, not expansions. Iterating to second order with explicit corrections = L* again.
(3) Literature: McKay-Wormald'91 error O(D^3/n) (too coarse, no smoothness). Whether a published n^-2 expansion
    in (d, H) exists: UNVERIFIED. Best candidates to check by hand: McKay "Subgraphs of dense random graphs with specified
    degrees" (dense, wrong regime), Isaev-McKay "Complex martingales and asymptotic enumeration" (error terms n^-c),
    Liebenau-Wormald "Asymptotic enumeration of graphs by degree sequence" (sparse; gives O(1/n)-type error for sparse).

## Decomposition worth keeping (correct, simple, but only a reduction)
Q(U) = E_res[ 1{residual simple} * prod_{e in U} 1{uv_e not in residual} ].
Dependence on U enters only via (i) d_v=D-h_v, (ii) N'=N-2L, (iii) which pairs uv_e are forbidden. The 4th difference over
non-star T={e1..e4} kills any factor depending on <=3 of the e's or any vertex-local function; what survives
couples >=2 edges of T through a shared vertex, a shared N', or a shared defect cluster. L* is exactly that the third kind,
summed over all n positions of clusters, is o(n^-2): needs cluster locality (decay) -- unproved.

## Suggested next steps (concrete)
1. Numerically estimate D^4_T log Q exactly for D=3, n up to DP limit using r5w3_exact.contains, for T in the few non-star
   shapes (path P5, matching 4K2, etc.), fit n^2*value; if it is flat (as r16w1/r18w1 suggest) L* is consistent but still unproved.
2. Prove L* in a cheaper setting first: *bipartite or Poisson model* (independent edge multiplicities), where defects are
   independent given degrees and log Q is an exact sum -> locality is trivial. Then transfer via a
   conditioning argument; the transfer error is the real obstacle.
3. Check literature (item 3) with web access.

## Honest status
L* open. R2* remains conditional. Nothing here should be cited as a proof step.
