# r16 brief: repair of lem:avoid-G-host (residual step 2)

Read first: v2/notes/r15w1_avoid_G_host.md (lemma is FALSE as stated: pairing-level log second-moment
ratio ~ n s2^4/(2 m^2 delta) on the window hyp:s3-avoid-G needs), v2/notes/r15w2_condition_A_B.md.
Write only v2/notes/r16w2_* and v2/scripts/r16w2_*. Do not edit paper/main.tex. Commit nothing outside those.

## Goal
Find a TRUE replacement for avoid-G-host that still feeds hyp:s3-avoid-G, or prove none exists.
Suggested repair (unproven): condition the pairing model on the assortativity sum sum y_i y_j over edges.
1. State the conditioned lemma exactly. Check whether conditioning removes the n s2^4/(2m^2 delta) blow-up.
2. Verify numerically (delta=40, m=6, t=3, n=200..1600 as in r15w1) that the conditioned log-ratio stays bounded.
3. Re-derive McKay's estimate used in r15w1 independently, flag if the quoted form differs.
4. If conditioning fails, give the sharpest true statement and what hyp:s3-avoid-G would need instead.
Report: proved / numerically checked / not checked, separately.
