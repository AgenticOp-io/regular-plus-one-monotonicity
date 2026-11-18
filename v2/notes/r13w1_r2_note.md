# r13w1: closed form for the triangle coefficient r2(D)

Scripts: `v2/scripts/r13w1_et.cpp` (r11w1 exact DP, array/key widened so D<=7), `r13w1_fit.py`, `r13w1_r2_formula.py` (re-runs everything, asserts).
Data: `r13w1_d{4,5,6,7}.txt` (exact E[T]/((D-1)^3/6), n<=100,100,71,50); D=3 from `r11w1_d3.txt` (n<=400).

## Result (NUMERIC-EXACT, not proved)
E[T]=(D-1)^3/6 (1 + r1/n + r2/n^2 + ...), r1=3(D-1)/D (fixed, never fitted; free fit at D=3 gave 2.000000).
Fitted r2 (n^2 residual, deg 4-6 polynomial in 1/n, stable to 1e-5 for D<=5):
 D=3: 3.777778 = 34/9;  D=4: 5.250000 = 21/4;  D=5: 6.240000 = 156/25;  D=6: 6.94444 = 125/18;  D=7: 7.469 (+-.002).
 r2*D^2 = 34, 84, 156, 250: exact quadratic in D (second difference 22). Three points fix it, D=5,6 are checks, D=7 is an independent prediction (7.4694 vs fit 7.4690).

   **r2(D) = (D-1)(11D-16)/D^2 = 11 - 27/D + 16/D^2**   (limit 11, not 12.5; the old 1/D fits 13.9/12.5 were extrapolation bias)

Split: pairing model, exact: n^-2 coeff = (2D^2-27D+58)/D^2; remainder from conditioning on simplicity = 3(3D^2-14)/D^2 = 9 - 42/D^2 (nice: no 1/D term).
Consequence (r10w3 exact reduction): S1_1_1 c0(D) = r2 - 9/2 - 15/D + 67/(2D^2) = (13D^2-84D+99)/(2D^2) -> 13/2 < 8=(j+k+w+1)^2/2, bounded, uniform in D. (D=5: .08, matches r10w3 data .09.)
So for w=1 the conjectured c0->L equality FAILS in the limit (13/2 vs 8) for (1,1,1); only the upper bound c0<=L survives. (Other w>=1 hosts need diamond counts; not redone.)

## What is proved / open
- PROVED (algebra): pairing-model part of r2; formula consistency checks above.
- NOT PROVED: the conditioning remainder 9-42/D^2 (needs P(simple|degree seq) to O(n^-2), i.e. 1/n term of McKay-style expansion as smooth function of the degree sequence). Same gap as r1 (r12w1). Formula is therefore a conjecture, strongly supported: rational form with 3 parameters matched 5 exact values D=3..7.
- OPEN: rigorous r1; r2 uniform in D (needs D=O(1) only for the theorem); two-sided j,k>=2 hosts with w>=1 still need diamond/C4 second-order terms beyond r2 (not attempted); D>=8 exact data (DP blows up).
- Switching route not attempted.
