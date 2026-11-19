# r10w2: zero-free disk for E y^T, general L (script only, no results yet)

Labels: [O] open. Nothing run/recorded; main.tex untouched.
Script: v2/scripts/r10w2_zeros.py  (usage: `r10w2_zeros.py L n`).

## What it does
P(y)=E y^T, T=|E(G1)∩E(G2)|, G1,G2 iid uniform L-regular on n vertices. Enumerates all L-regular graphs on n vertices (bitmask over edges),
histograms T against every G1 (L=2: one representative per component-size class, weighted by class count; else all pairs, small n only),
shifts y=1+w, and finds the root of P nearest y=1 with mpmath (80 dps). Prints |w|, R/n, R*L/n -- compare L=1 baseline R/n -> W(1/e)=0.2785 (r9w2).

## Caveats [O]
- L=2 class invariant is sorted component sizes; this is NOT the iso class (a component of size k>=4 could be a non-cycle only if not 2-regular, so for 2-regular graphs sizes = cycle type -- fine). Not checked against brute force.
- Enumerator has dead pruning lines (`pass`, `and False`); correctness of N unverified (should match known counts, e.g. L=2 n=6: 70).
- Pair enumeration is O(N^2); only tiny n feasible. Float64 histogram fed to 80-digit roots, so precision is limited by the double hist.
- No output captured yet: whether R*L/n stays bounded below for L>=2 is open.
