# r8w2: (B*) — is it needed for all k>=4? Cauchy/zero-free reformulation

Labels: [P] proved, [N] numerical, [C] conjecture. (B*) is NOT proved; k=4 second-order asymptotics NOT derived. main.tex untouched, nothing committed.
Notation: P(y)=E y^T (polynomial, positive coefficients, P(1)=1, deg<=nL/2), kappa_k = k! [w^k] log P(1+w), mu=ET=L^2/2(1+o(1)).

## 1. Answer to the open sub-question [P]
(B*) is exactly a Cauchy estimate: L^{k+1}/n^{k-1} = nL (L/n)^k, so (B*) <=> |kappa_k|/k! <= (nL)(CL/n)^k, i.e. "log P bounded by ~nL on a disk of radius n/(CL) about y=1".
Claim A [P]: if P has no zero in |y-1|<rho with rho = n/(C0 L), then for all k>=1
  |kappa_k|/k! <= 2 U (2/rho)^k,  U = log P(1+rho) <= (nL/2) log(1+rho).
Proof: f=log P(1+w) analytic on |w|<rho, f(0)=0, Re f <= U there (|P(z)| <= P(|z|) by positive coefficients; need |z| <= 1+|w|, ok). Borel-Caratheodory at r=rho/2 gives |f|<=2U on |w|=rho/2; Cauchy gives the coefficient bound. QED.
Consequence [P]: (B*) holds for ALL k (with an extra log n and a constant C=2C0) from ONE zero-free-disk statement; the tail sum_{k>=4} then needs nothing more. So there is no real split "k=4..K0 plus a crude bound": a crude bound that reaches k>=K0 with the right geometric ratio L/n is the same zero-free statement, and it then gives k=4 too.
Tail check [P]: with Claim A, sum_{k>=K} |w|^k|kappa_k|/k! <~ nL log n (C|w|L/n)^K; for K=4 this is L^5 log n/n^3 -> 0 for L<=n^{1/2}; for K=3 it is L^4 log n/n^2 -> 0 only for L << n^{1/2}/log^{1/2}: k=3 stays exact (r4), k>=4 is what zero-freeness supplies.

## 2. Why no crude bound exists [P]
Without cancellation, the majorant route (absolute values of a_j=m_j/j!=sum_{|S|=j}p_S^2, a_j ~ mu^j/j!) gives |kappa_k|/k! <= (C L^2)^k, radius ~1/L^2 instead of n/L.
Needed: improvement by (L/n... ) = (n L)^{-(k-1)}-type cancellation per order, consistent with kappa_4 ~ L^5/n^3 vs m_4 ~ L^8. So every k>=4 needs the cancellation; a "crude bound beyond K0" cannot be absolute-value-based. The only crude mechanism is analytic (Claim A), which needs zero-freeness at scale n/L, i.e. Poisson-like behaviour of P near y=1 (Poisson: P=e^{mu(y-1)} has no zeros at all).

## 3. Numerics [N]  (script v2/scripts/r8w2_zeros.py, re-run before this report)
Exact law of T over all pairs of iid nu_L (L-sets of disjoint perfect matchings; F1 reduced by symmetry: M1 canonical + other PMs, checked to reproduce the full-pair result; assert E T = n(n-1)/2 (L/(n-1))^2). Nearest zero of P to y=1:
| n,L | N sets | nearest zero | R=dist | n/L | R L/n |
|---|---|---|---|---|---|
| 8,2 | 3150 | -.667+.544i | 1.754 | 4 | .438 |
| 8,3 | 32970 | -.103+.267i | 1.135 | 2.667 | .426 |
| 10,2 | 257040 | -1.004 (real) | 2.004 | 5 | .401 |
n=10 L=3, n=12 L=2 did not finish (n=10,L=3 >10 min; not retried; killed). Result: R*L/n ~0.40-0.44, i.e. zero-free radius ~0.4 n/L, consistent with Claim A's hypothesis (C0~2.5), slowly decreasing in n at L=2 (.438 -> .401, 2 points; L=2 is degenerate, see r7). WEAK: n<=10, no information on the n-dependence for L>=n^{1/3}. The zeros are not Poisson-like (they sit at |y|~1, not infinity), so the hypothesis is nontrivial and could fail with R L/n -> 0 slowly; two n values cannot tell.
No numerical k>=4 data beyond r7's table was produced; no new kappa_4 value.

## 4. k=4 second-order asymptotics
[O] not done. I found nothing new beyond r7 Sec.3; the 11 four-edge classes (C4, P5, paw, ... ) still lack two-sided p_S asymptotics. Claim A suggests a different target than p_S per class: prove zero-freeness of E y^T for |y-1|<n/(CL) directly (Lee-Yang/Barvinok-type interpolation, or via positivity of the pairing-count generating function), which sidesteps class-by-class expansions.

## 5. Next steps
1. Prove or refute zero-freeness at scale n/L in a solvable model (e.g. L=1: T=overlap of two uniform PMs, law explicit via rencontres-type counts; check R vs n) — cheap and a genuine test of the Poisson-like hypothesis for the r=1 case.
2. Larger exact (n,L): needs symmetry-reduced counting of p_S classes (not all-pairs); n=12,L=2 feasible with a C++ port.
3. [C] If zero-freeness fails at scale n/L but holds at n/L^{1+a}, Claim A still gives R2* for L<n^{(1-a')/2...}; compute what is lost before investing.
