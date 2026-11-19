# r16w1: R2* / (B*) — status (NOT proved)

## Proved
Nothing new. No two-sided second-order expansion of p_S for 4-edge S was obtained, so the
smallest provable `a` in p_S = prod p_e (1 + conn. corrections + O((L/n)^a)) is still: only the
switching-level bound (k<=3, n^{1/3} barrier). The missing inequality is unchanged from r15w3:
a lower bound (n^-2 relative) on #matchings of a regular host avoiding a prescribed 4-edge
pattern, i.e. the same conditioning gap as r1/r2(D); I could not show it is intrinsic either.

## Numerically checked (v2/scripts/r16w1_cluster.py, exact counts; data in r16w1_data_L3/L4.txt)
u(S) = sum_{A<=S} (-1)^{|S|-|A|} log p_A, p_A = P(A subset F), F uniform L-regular on n vertices,
exact via vertex-by-vertex DP on degree sequences (4-edge joint log-cumulant per shape).
- L=3, n=8,10,12 and L=4, n=10,12 only (n=14, L=4 timed out). Results: disconnected shapes
  (4-matching, P3+2, P4+e) are ~1e-3..1e-4 and shrink with n; connected P5/fork ~1e-3;
  C4 and triangle+pendant are largest (L=3: C4 -3.3e-2 -> -2.0e-2 for n=10->12, local exponent ~ -2.6;
  L=4: -1.9e-2 -> -1.2e-2, exponent ~ -2.4).
- star4 at L=4 is -0.165 and flat in n: degree-saturation artefact (a vertex of degree 4=L), not asymptotic.
Consistent with decay near n^-2..n^-3 but these n are far too small to fix the exponent or any L-dependence.

## Not checked
- L-scaling (needs L growing with n; exact DP infeasible beyond n~12). Whether |kappa_4| <= C L^5/n^3.
- Any n>=14, pairing-model second-order host counts, summability over k>=4.
