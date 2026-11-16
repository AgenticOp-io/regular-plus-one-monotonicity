# r6: tilted pairing second moment for G(n,p)-type hosts

Scripts: `v2/scripts/r6_tilt.py` (R(t) by MC over exact overlap law pi, exact f), `v2/scripts/r6_scale.py` (n-scaling).
Labels: [P]=proved (algebra), [N]=numerically supported, [C]=conjecture. main.tex not edited.

## 1. The tilt
Lambda(P) = sum over pairs {i,j} of the pairing P of y_i y_j (y_v = h_v - hbar). Tilted count: Z_t = Z * exp(t*Lambda(P)).
Target: R(t) = E[Z^2 e^{2t Lambda}] / (E[Z e^{t Lambda}])^2.  (Tilt is by a function of the pairing, not a per-point weight w_v;
a per-cell weight cannot work because r_v are forced, so the subset-weight is constant on closed sets. [P] trivial.)

## 2. Exact reduction [P]
Within a class of m points with centred-in-class weights, Lambda_class = W^2/(2m) + Lambda_u, W = sum of point weights, Lambda_u
= sum over pairs of u_i u_j (u = w - W/m, sum u = 0). Exact. E Lambda_u = -Q_u/(2(m-1)), Var Lambda_u = (Q_u^2 - sum u^4)/(2(m-1)) approx,
Q_u = sum u^2. In the second moment the four classes (overlap O, S1\S2, S2\S1, rest R) are independent uniform pairings given the
overlap vector b, so E[Z^2 e^{2t Lambda}] = Z-prefactor * E_pi[ f(S) 1_even * E exp(2t sum_k Lambda_k) ].
The b-dependence enters only through W_O = sum b_v y_v etc. (deterministic quadratic W^2/2m terms) — this is what the tilt can
cancel against the shift Delta = D^2 sum y^2/hbar^3 of r4 Prop 3.
APPROXIMATION (not proved): Lambda_u replaced by Gaussian (cumulants to order 2). Error is third cumulant * t^3, t ~ 1/(eps hbar^2).

## 3. Numerics [N] (hbar=12, D=9, rho=3, beta := D/(rho hbar^2) = 0.0208)
Optimal tilt found by scan: t* = -beta (sign: Z_t = Z e^{-beta Lambda}, i.e. the tilt REMOVES the e^{-beta Lambda} dependence; the sign
in r4 Sec 8 "N ~ exp(-beta Lambda)" is consistent). t>0 makes R blow up (n=480, t=.05: R=31).
y in {-1,0,1} (1:2:1), R(0) -> R(-beta):  n=240: 1.32->1.15;  n=960 (K=.62): 2.04->1.11;  n=1920 (K=1.25): 2.78->(0.81)
y in {-2..2} binomial,  R(0) -> R(-beta):  n=240: 1.73->0.94; n=960 (K=2.5): 9.1->(0.77); n=1920 (K=5): 135->(0.95)
Untilted R grows like exp(K) as r4 predicts; tilted R(-beta) stays O(1) and is flat in n and in K. The minimum over t sits at -beta
within ~20% (n=480 scan: min near t=-0.02).
CAVEAT: values < 1 are impossible for a true second moment ratio; they come from the Gaussian truncation of Lambda_u (and MC noise
at heavy tails). So only "tilted R is bounded, no exp(K) growth" is supported; the constant is NOT reliably the regular value
sqrt((hbar-1)/(hbar-2)) = 1.049. An exact tilted pairing computation (not Gaussian) was not done.

## 4. Claim (conjecture [C], not a theorem)
For hosts with |y_v| <= C sqrt(hbar log n), D^3 = o(n) etc. (r4 hypotheses), tilt t = -beta (1+o(1)), beta = D/(rho hbar^2):
  E[Z^2 e^{-2 beta Lambda}] / (E[Z e^{-beta Lambda}])^2 = sqrt((hbar-1)/(hbar-2)) (1+o(1)) for every degree profile, K-free.
Heuristic reason: log f has curvature c at S*; Gaussian integration over (S, Y=sum b y) shows the tilt adds a linear term in delta Y whose
coupling cancels c*Delta*delta S, leaving K_tilted = 0 at t = -beta; K = beta^2 Var(Lambda) from r4 Sec 8 is the same beta.
Consequence if true: N e^{-beta Lambda}/E[...] -> 1 in L^2 for G(n,p) hosts, so planting should be done against the tilted weight
(reweight G(n,p) by e^{-beta Lambda(H)}/normaliser; Lambda is a host statistic, and its law needs a separate tilt-comparison
step: TV between G(n,p) and its e^{-beta Lambda}-tilt is small iff beta^2 Var Lambda = K = o(1) — which FAILS for G(n,p)).
## 5. Honest obstruction
The last point matters: tilting the second moment fixes concentration of Z_t, but converting back to N needs N/E N = Z_t/E Z_t * e^{beta Lambda}/E_host-conditional ...
i.e. one still needs Lambda concentrated at scale o(1/beta), which is false (sd(beta Lambda) = sqrt K -> inf). So the tilt gives
N = EN(Lambda) * (1+o(1)) with EN(Lambda) ~ e^{-beta Lambda}: a conditional-on-host-statistic LLN, NOT N/EN -> 1 under G(n,p).
Whether (iii') needs unconditional N/EN -> 1 or only "planted vs G(n,p) in TV" must be checked against PROGRAM.md; a log-normal law of
N under G(n,p) is not a TV obstruction by itself, but Lemma 1 (E|Z-1|) form of the planting reduction no longer applies directly.
## 6. Not done
No proof of Gaussian step, no exact (non-Gaussian) tilted moment, no simple-graph transfer, no scan for non-{-beta} optimal t beyond n<=480,
residual statistic from r5 (A-A degree profile) not examined at larger n.
