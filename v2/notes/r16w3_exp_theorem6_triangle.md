# r16w3: triangle coefficient r2(D) (exp-form Theorem 6)

E[#triangles in G(n,D)] = (D-1)^3/6 * (1 + r1/n + r2/n^2 + ...), r1 = 3(D-1)/D.

## Closed form (NUMERIC-EXACT, not proved)
r2(D) = (D-1)(11D-16)/D^2 = 11 - 27/D + 16/D^2  (from r13w1; see r15w3).
Re-run 2026-11-19 with v2/scripts/r13w1_r2_formula.py: fit/pred D=3..7 =
3.77778/3.77778, 5.25/5.25, 6.24/6.24, 6.94441/6.94444, 7.46898/7.46939 (D=7 out of sample).

## Bound
r2(D) < 11 for all D>=3 (increasing in D on D>=3: derivative 27/D^2-32/D^3>0 iff D>32/27), r2 -> 11.
Hence c0(S1_1_1)=(13D^2-84D+99)/(2D^2) < 13/2 ... (r15w3 states <8; either way bounded) -- conditional on r1, r2.

## Obstruction
Split r2 = pairing part (2D^2-27D+58)/D^2 [PROVED algebra, configuration model]
        + conditioning remainder 3(3D^2-14)/D^2 = 9-42/D^2 [NOT proved].
Yes, a conditioning term (as in R2*) is the obstruction: need P(simple | triangle-host present) to relative
O(n^-2), i.e. McKay-type second-order expansion; same gap as r1=3(D-1)/D.

## Status
- Proved: pairing-model part only.
- Numerically checked: closed form vs exact DP for D=3..7 (3 free params, 5 points; D=7 and D=6 are genuine checks).
- Not checked: D>=8 (DP data n<<D^2 unreliable), independent derivation of the remainder, any n^-3 term.
No new script (r13w1_r2_formula.py reused unchanged).
