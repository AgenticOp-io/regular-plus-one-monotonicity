# r24b: first-order constant f1 = 2 for E[q] (4-cycles), pairing-model computation
Status: DERIVED to O(1/n) under one unproved lemma (L1 below); matches numerics (r23a). Not a full proof. No literature search done (MWW statement not checked).

## Setup
Pairing model, N=nD points, G = simple pairing. #4-cycles in K_n = n^(4)/8; placements of a fixed labelled 4-cycle: (D(D-1))^4; P(4 given pairs) = 1/((N-1)(N-3)(N-5)(N-7)). So
 E q = n^(4)/8 (D(D-1))^4 /prod_{j<4}(N-2j-1) * R,  R = P(simple | C4 present)/P(simple).
Prefactor = (D-1)^4/8 * (1-6/n)(1+16/N+O(n^-2)) = (D-1)^4/8 (1 - 6/n + 16/(Dn) + O(n^-2)).  [EXACT]

## R to relative O(1/n)  (a = n C(D,2) = N(D-1)/2)
Given the C4, the rest is a uniform pairing on N-8 points, four vertices with degree D-2. Poisson parameters:
- loops: lam1' - lam1 = [-4(2D-3) + a*8/N^2*N...]/N = -4(D-2)/N   => -Δlam1 = +4(D-2)/N
- double edges: lam2 ~ a^2/((N-1)(N-3)); with a' = a-4(2D-3), denominators (N-9)(N-11): Δlam2 = (D-1)^2/4 * 16/N * (1-(2D-3)/(D-1)) = -4(D-1)(D-2)/N  => -Δlam2 = +4(D-1)(D-2)/N
- new: edge parallel to one of the 4 cycle edges: 4 (D-2)^2/N => -4(D-2)^2/N
Sum = 4(D-2)[1+(D-1)-(D-2)]/N = 8(D-2)/N = (8-16/D)/n.  So R = 1 + (8-16/D)/n + O(n^-2) (given L1).
Hence f1 = -6 + 16/D + 8 - 16/D = **2** for every fixed D>=3, D-independent, as numerics said (1.99 at D=3, 1.97 at D=4).

## Cross-check: triangles (same computation, 3 vertices)
Prefactor (1-3/n)(1+9/(Dn)); R = 1+(6-12/D)/n  =>  e1 = 3-3/D. D=3: 2.00 (numerics 1.99), D=4: 2.25 (numerics ~2.2). Matches, so e1 is also determined: E t = (D-1)^3/6 (1+(3-3/D)/n+O(n^-2)).
(Check D=2 trivial: e1=1.5; not tested.)

## Lemma L1 (the gap)
Needed: for degree sequences d, d' differing from each other at O(1) vertices by bounded amounts (n,D fixed-ish),
 ln P(simple|d') - ln P(simple|d) = -Δ(lam1+lam2 [+ parallel-edge term]) + O(n^-2),
i.e. the part of ln P(simple|d) beyond Poisson lam1+lam2 is (1/n)*Phi(normalized moments of d) + O(n^-2), so a local change moves it by O(n^-2).
Why plausible: Janson/cluster (inclusion-exclusion) expansion of ln P(no loop/double edge): single structures give the lam terms; clusters of j>=2 overlapping structures sharing a vertex v contribute O(n^-2) per vertex; remaining global terms depend on d only through sums S_k=sum d^(k) and N, which change by O(1) i.e. relative O(1/n).
Why not cited: McKay-Wormald 1991 asymptotic formula has relative error O(1/n) for bounded D, which is the same order as what we need, so it does NOT suffice; MWW short-cycle result likewise gives only O(1/n) relative error (from memory, unchecked). Needed: error O(n^-2) for the DIFFERENCE, a local-perturbation statement.
Rigorous routes (not done): (i) cluster expansion with explicit n^-2 remainder; (ii) switching: compare #pairings with the C4 vs without via 2-switchings, track the 1/n terms of the double-counting corrections. Not attempted beyond the Poisson bookkeeping above.

## Consequence
With L1: E q = (D-1)^4/8 (1+2/n+O(n^-2)) => u_C4 = O(n^-2) (r23a D: n*u = f1-2), and the n^-2 remainder in R is exactly what L1 supplies. E t = ...(1+O(1/n)) also follows. So R2*(k=4) is reduced to L1, with the explicit first-order constants checked against DP numerics.
Also noted: all constants above can be verified symbolically (sympy) - algebra done by hand here, re-checked via the two numeric matches only.
