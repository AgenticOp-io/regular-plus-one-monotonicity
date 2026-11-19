# r20 brief A: R2* with the statement fixed exactly
Read first: r16w1_R2star_status.md, r17a_simple_expansion.md, r17b_R2star_status.md (r17b stalled on ambiguity; this removes it).
Write only v2/notes/r20a_* and v2/scripts/r20a_*. Do not edit paper/main.tex.

## Exact statement (use this one, do not reinterpret)
G uniform D-regular simple graph on n vertices (D fixed first; then D=L growing, L<n^{1/2}).
For an edge set U on [n]: p_U = P(U subset G). Ursell u_T = sum_{U<=T} (-1)^{|T|-|U|} log p_U.
R2*(k=4): for every connected 4-edge T (P5, C4, triangle+pendant, K1,3+edge, ...; stars treated separately):
  |u_T| <= C * D^a / n^{2}  (find a, C; fixed-D data show n^-2 for k=4).
Equivalent route: log p_U = pairing part (exact, r16w1) + log P(simple | U). So R2* <=> the 4th finite difference of
log P(simple | U) over T is O(D^a/n^2). Prove it, or find T/regime where it fails.
## Do
1. Use r17a identity Q(H)=g(H)*prod(D-h_v)!/(N-2L-1)!! and prove/bound g(H)/g(empty) to relative O(D^a/n^2) for |H|<=4.
2. Numerics: exact D=3,4 (v2/scripts/r16w1_ursell.py) to confirm any claimed formula before stating it.
3. Report proved / numeric / not checked separately. Commit on your branch.
