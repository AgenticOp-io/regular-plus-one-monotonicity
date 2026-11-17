# r9w2: zero-free disk for E y^T in the L=1 case (explicit law)

Labels: [P] proved, [PS] proof sketch (standard saddle-point step not written out), [N] numeric, [O] open. Nothing committed, main.tex untouched.
Script: v2/scripts/r9w2_L1_zeros.py (re-run; asserts the Gaussian identity below at m=6, prints zeros and the limit).

## 1. Exact form [P]
L=1: T = |M1 ∩ M2| for two uniform perfect matchings on n=2m vertices. Fixing M1 and inclusion-exclusion:
  P(1+w) = Σ_i C(m,i) (2m-2i-1)!!/(2m-1)!! · w^i  = 1F1(-m; 1/2-m; w/2) (a Laguerre polynomial with α=-m-1/2).
Using (2k-1)!! = E g^{2k}, g~N(0,1):   P(1+w) = E (g²+w)^m / E g^{2m}.   (assert in script)
So P(1+w) ∝ I(w)=∫_0^∞ (x+w)^m x^{-1/2} e^{-x/2} dx.

## 2. Zeros [N]
Exact roots (mpmath, 120 digits), nearest zero to y=1, R=|w|:
 n=8:.344n  10:.322n  16:.308n  24:.298n  32:.293n  48:.288n  64:.285n  96:.283n  128:.282n  192:.2807n.
R/n decreases monotonically but flattens: Richardson (c+a/m, m=32,48) gives 0.27834. Nearest zero is ≈ real negative with Im ≈ ±1.37 (O(1)). So R·L/n stays bounded below for L=1, R/n → 0.2785 = W(1/e) (below).

## 3. Why: saddle point vs endpoint [PS]
I(w): exponent Φ(x)=m log(x+w) − x/2 − ½log x. Saddle x*=2m−w (Re>0 for |w|<2m); value |e^{Φ(x*)}| ≈ (2m)^m e^{-m} e^{Re w/2}·poly. The endpoint x=0 contributes ≈ |w|^m ·poly. With ζ=w/n (n=2m):
  endpoint/saddle ≈ ( |ζ| e^{1−Re ζ} )^m.
Zeros of I can occur only where saddle and endpoint balance, i.e. near the curve |ζ|e^{1−Re ζ}=1 (Szegő-type curve). Where |ζ|e^{1−Re ζ}<1 the saddle dominates and I≠0 (saddle term is a nonvanishing e^{...}). On |ζ|=r, max of |ζ|e^{1−Reζ} is at ζ=−r: r e^{1+r}. So zero-free for |ζ|<ρ with ρe^{1+ρ}=1, i.e. ρ e^ρ=1/e, ρ=W(1/e)=0.27846. Matches [N] to 4 digits.
Missing for a full proof: uniform error control of the saddle expansion on |ζ|≤ρ−ε (standard steepest descent for a one-saddle integral with an x^{-1/2} endpoint; Kuijlaars–Martínez-Finkelshtein-type asymptotics for Laguerre L_m^{(−m−1/2)} give it). Consequence: [PS] for every ε, P(1+w)≠0 for |w|<(W(1/e)−ε)n and n large ⇒ by r8w2 Claim A, (B*) holds for L=1: |κ_k| ≤ k! n (C/n)^k·... i.e. L^{k+1}/n^{k−1} with L=1.
This is a CORRECTION of the r8w2 worry: zeros are NOT Poisson-like (they sit at |y|~n, scale n), but they ARE at distance Θ(n), exactly the scale (B*) needs. Note r8w2's R·L/n≈0.40 at n≤10 vs limit 0.278 at L=1: the constant drifts down but saturates.

## 4. General L [O] — the precise missing step
P(1+w)=Σ_F w^{|F|} p_F² with p_F=Pr(F ⊆ G), G the L-regular model. L=1: p_F=(n−2|F|−1)!!/(n−1)!! for matchings F, and the Gaussian trick turns Σ C(m,i)w^i(2m−2i−1)!! into one positive-measure moment E(g²+w)^m. For general L there is no such representation: p_F is not a product of per-edge factors and there is no positive "Wick" measure making Σ_F w^{|F|}p_F² an integral of a power. Needed: either (a) a representation P(1+w)=E_μ[(Q+w)^{N}]-type (Lee–Yang/Asano-contraction form) valid up to multiplicative errors 1+O(L/n) per factor, or (b) comparison with an L-fold independent product: E y^T for L independent matchings pairs is a convolution/product of L² L=1-type laws minus collisions — the collision corrections are the unknown, and need only be shown to move zeros by o(n/L).
Heuristic [C]: T ≈ sum of L² nearly-independent copies of the L=1 overlap (each overlap of M_a ∩ M'_b is the L=1 law ⇒ zero-free radius W(1/e)n for each factor ⇒ for the product P_1(y)^{L²} the zero-free radius is still ~0.278 n, NOT ~n/L). Since (B*) asks only n/L, that would be loose by factor L; the real obstruction is the dependence between the L² factors (disjointness of matchings), which is O(L/n)-relative and should perturb zeros by a bounded factor if controlled in an analytic (Rouché) fashion on |w|<n/(CL).
Rouché plan [O]: show log P_L(1+w) = L² log P_1(1+w) + E_L(w) with |E_L(w)| < L² · (0.5)|log P_1| ... fails since log P_1 is small near 0; need |E_L(w)| < |L² log P_1 + ...| not available. The honest missing step: a bound on log P_L analytic on |w|<n/(CL) with Re ≤ nL ·const — equivalent to the whole claim, so cannot be bypassed by comparison unless E_L is bounded absolutely by O(L²·L/n·|w|) (a first-order disjointness correction); computing that correction is precisely the k=2,3 cumulant (already exact, r4) — suggests proving E_L's k-th Taylor coefficient is O(k!(C L/n)^k nL) by induction — open.

## 5. k=4 second-order asymptotics [O]
Not attempted beyond r7; L=1 data (this note) says only that no-zero structure is real, not the 4-edge class constants. Recommended next: use the L=1 closed form to test (B*) numerics: κ_k(L=1) exact from log P(1+w); fit C^k.

## 6. L=1 factorial cumulants [N] (m=64, n=128; κ_k=k![w^k]log P(1+w); column = |κ_k|/k!·n^{k-1})
k=2..8: .00203 .00143 .00116 .00103 .00098 .00097 .00101 — flat ⇒ |κ_k|/k! ≈ 1e-3·n^{-(k-1)}: geometric ratio ~1/n with no k! growth beyond Cauchy, consistent with (B*) (zero radius ~0.28n). [N], one n only.
