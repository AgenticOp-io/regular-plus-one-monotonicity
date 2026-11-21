# r31: double-switching attempt on missing lemma 2: NOT PROVED
Status: no proof. This note gives the setup, the error accounting, and the exact step that fails. Nothing here is a theorem.

## Lemma attempted
Pairing model, degrees d_i <= D, M = sum d_i ~ Dn. For a fixed cycle edge (i,j), let m = number of pairs parallel to it (other pairs joining points of i and j). Want, uniformly for 3 <= D <= n^c, that the ratio P(m=1)/P(m=0) (and the induced Bonferroni term E binom(Z,2)) is known to absolute error O((D+k^2)/n^2), instead of the O(D^4/n^2) from single switchings.

## Accounting (heuristic, paper only, not verified numerically)
- Main term lambda = (d_i-1)(d_j-1)/(2M) ~ D/n (for d ~ D, M ~ Dn). The exact first-order constant is not the issue.
- Single switching (remove the double pair, cross with two fresh pairs): forward count ~ M^2, backward count ~ d_i d_j. Forbidden-configuration losses (new loop/parallel at the 4 touched vertices) are relative O(D^2/n). Absolute error in the ratio: lambda * D^2/n ~ D^3/n^2. Target is D/n^2, i.e. relative error 1/(nD)... so single switching is short by a factor D^2.
- Double switching (MWW04 / McKay 1002.3018 style) removes the relative D^2/n terms by comparing two sets of forbidden configurations. Leftover: overlaps of two forbidden events, relative (D^2/n)^2, and three-vertex overlaps ~D^3/n^2. These give absolute errors below D/n^2 iff roughly D^4 <= n. So IF the cancellation step below closed, the range would be about D <= c n^{1/4}. Unverified.

## Step that fails
The cancellation of the relative-D^2/n terms needs the exact first-order values of
  P(no loop/parallel at the touched vertices after the switch | rest of the structure),
i.e. ratios P_{d'}(simple)/P_d(simple) for degree sequences d' differing from d at 4 vertices. That is exactly L1' of r29 (the differentiable-in-d McKay-Wormald exponent with error O(D/n)). Double switching relates two such quantities to each other; it does not evaluate them. The argument is circular: lemma 2 needs L1' at precision O(D/n^2) per unit degree change, and L1' is the missing input. Fixed D (r25) avoids this only because constants may depend on D.

Second obstruction: the backward count needs the number of valid auxiliary pairs avoiding all ~D^2 collision sites per vertex, and the *difference* between the two sides is needed to relative precision 1/(nD), while the first-order inclusion bound controls it only to D^2/n. Closing needs inclusion-exclusion to second order with explicit overlap terms. Not done.

## Conclusion
Lemma 2 is NOT proved for any growing D. Conditional on L1', the accounting suggests D <= c n^{1/4}; this is a heuristic, not a claim. Single switchings give only D^3/n^2.
