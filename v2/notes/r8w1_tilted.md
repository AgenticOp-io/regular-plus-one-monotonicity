# r8w1: can the Gaussian/tilted step (iii') be done from TV closeness alone?

Script: `v2/scripts/r8w1_tilted.py` (run twice, asserts pass). Labels: [P]roved, [N]umerical, [C]onjecture.
Answer: **no — TV closeness alone is insufficient (precise counterexample, [P]); the right condition is a weighted (exp-moment) closeness, which reduces to G0-dependence of cumulants of the host statistic.**

## 1. Setting [P, as in r6_iii_requirement]
Y(G0) = E[e^{-f(S)} | G0] / avg over G0, with log N = f(S), S a host statistic, f(S) ~ -beta*Lambda. Write L = beta*sd(Lambda), K = L^2 (-> inf, r4/r6).
Let P_G0 = law of S given G0, Pbar = its mu_D-average. d_TV(P_G0, Pbar) -> 0 is what "TV closeness" gives.

## 2. Obstruction [P]
Weight w = e^{-sqrt(K) Z}, Z standardised. If P_G0 = N(delta, s^2) and Pbar = N(0,1) then exactly
 Y = exp(-sqrt(K) delta + K (s^2-1)/2).
 - Mean shift delta = K^{-1/4}: TV ~ 0.4 delta -> 0, but Y = exp(-K^{1/4}) -> 0.
 - Scale s = 1 + K^{-1/2}: TV -> 0, but Y ~ exp(sqrt(K)) -> inf.
[N] confirmed by quadrature (A rows in script: K=256: TV=0.099, Y=1.8e-2 for the shift; TV=0.029, Y=1.5e7 for the scale; formula matches to 1e-6).
Reason: the weight puts its mass at ~sqrt(K) sd in the tail, where TV is blind. So TV(P_G0, Pbar)->0 does NOT imply Y->1 when K->inf.
Sufficient (Gaussian case) [P]: delta = o(K^{-1/2}) and s^2-1 = o(1/K). Without Gaussianity, the needed statement is
the cumulant generating function difference |log E_G0 e^{-tS} - log E_bar e^{-tS}| -> 0 at t = L (exp-moment closeness), not TV.
This refines r6_iii Sec 2/3: "G0 enters only via higher cumulants" is the right idea, but the bound needed is K*(relative effect) -> 0 per cumulant order, with the K factor kept.

## 3. Exact G0-dependence of S = sum r_v^2 (r_v = host degree) [P + N]
Given regular G0, the random part is G(n,p) on the complement H (also regular). T = sum r_v^2 = sum r_v + 2*#2-paths.
 - Mean of T: depends only on |E(H)| and degrees [P].
 - Variance of T: covariances between 2-paths are nonzero only if they share an edge; the union shapes are paths/stars of <=3 edges in H, whose counts, for H regular, are degree-only. Hence **Var T is G0-independent** [P] (the 3-edge path count involves a triangle correction only through a path-of-length-3 pair, which is not a sharing-one-edge pair of 2-paths). Checked exactly [N]: n=6 (C6 vs 2xK3) and n=8 (Q3 vs 2xK4) give identical mean and variance (to 1e-9).
 - Third cumulant depends on triangles of G0 [N]: C6 vs 2xK3 p=.3: k3 = 286.917 vs 286.028; p=.5: 492 vs 490.5. Q3 vs 2xK4 (p=.3): 1166.91 vs 1163.36. Fourth cumulant also differs (2578 vs 2558) at p=.3.
 So delta = 0 and s=1 exactly at the mean/variance level; the leading G0-dependence of log Y is at cumulant 3: log Y ~ -(c^3/6) Delta k3(T) + (c^4/24) Delta k4(T) ... with c = beta/(2(M-1)).
 Delta k3 is proportional to the triangle-count deviation of G0 (t0 - E t0 ~ D^{3/2}) [C: proportionality shown only by the 4 small cases; no coefficient derived].

## 4. What is and is not decided
- Proved: TV closeness alone cannot give Y -> 1 once K -> inf (Sec 2). Any proof of (iii') for G(n,p) hosts must control exp-moments / cumulants with the K factor.
- Proved + exact small-n: the two leading cumulants of S are G0-independent for regular G0 (Sec 3), supporting r6_iii's heuristic.
- NOT done [C]: size of c^3 Delta k3 at scale (K ~ n); i.e. whether beta^3 * (D^{3/2} * triangle weight)/sigma-scale -> 0. Needs the explicit third-cumulant coefficient per triangle (a closed form from the 3 edge-sharing 2-paths around a triangle plus all 3/4-edge chains whose counts involve t0) and K's n-scaling (r6 numerics: K ~ n at hbar=12, D=9).
- NOT done: f != linear in S (S is only the degree functional; residual r5 statistic), non-Gaussian tail beyond cumulant 4, simple-graph transfer.
- main.tex untouched; nothing committed.
