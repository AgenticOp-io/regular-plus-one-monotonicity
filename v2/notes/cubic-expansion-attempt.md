# Cubic-order expansion of the factor second moment (attempt, 2026-10-16)

Status: heuristic and internally inconsistent. Not a proof. Do not cite.

## Setup

\(\EE[Z_L^2]/(\EE Z_L)^2=\EE_{F_1,F_2}[R(F_1,F_2)]\), with \(F_1,F_2\) independent
uniform \(L\)-factors of \(K_n\) and
\(R=\PP(F_1\cup F_2\subseteq G)/(\PP(F_1\subseteq G)\PP(F_2\subseteq G))\).
Write \(T=|F_1\cap F_2|\) and \(\lambda=D/(n-1)\).

## Naive bookkeeping with McKay 2011 Corollary 5

Second differences over the four hosts \(F_1\cup F_2,F_1,F_2,\emptyset\):

- Quadratic terms give \(-L^2(1-\lambda)/(2\lambda)\).
- The \(T\)-linear terms at order \(LT/n\) give \(2(1-\lambda)LT/(\lambda n)\). The
  Gaussian degree-conditioning heuristic agrees.
- At \(T=0\), the \(X_3\) and \(H\) terms give
  \(-[(1-\lambda^2)/\lambda^2+3(1-\lambda)/\lambda]L^3/n\).

Overlap average, with \(x=\lambda^{-1}e^{2(1-\lambda)L/(\lambda n)}\): the heuristic is
\(\log\EE x^T=\mu(x-1)-L^3(x-1)^2/(2n)+O(L^4/n^2)\), where \(\mu=nL^2/(2(n-1))\).
Its \((x-1)^2\) coefficient matches the exact \(\kappa_{[2]}=-L^3/n\) from v1
Proposition pairwise-mass.

Total cubic coefficient: \(-(1-\lambda)(1+7\lambda)/(2\lambda^2)\) (checked). This is
negative for every \(\lambda\in(0,1)\). That is impossible past \(n^{1/3}\),
because \(\EE[Z^2]\ge(\EE Z)^2\).

## Diagnosis

McKay's displayed formula is exact only up to \(O(n^{-b})\) in a range where
\(|X|=O(n^{1+2\varepsilon})\). Terms such as \(|X|X_2/n^3\) and \(|X|^3/n^4\) are of
order \(L^3/n\) for \(L\)-regular \(X\), since
\((Ln/2)(L^2n)/n^3=L^3/(2n)\) (checked). In McKay's range they are
\(O(n^{-1/2+5\varepsilon})\), so they may be absorbed in his error term. So
McKay's displayed terms cannot fix the cubic coefficient. One also needs:

1. The beta-model entropy of \(K_n-X\) at its own density
   \(\lambda_X=\sum d/\sum g\), not at \(\lambda\).
2. The determinant \(-\tfrac12\log|A|\). Its second difference contributes
   \(+L^2/(2n)-O(LT/n^2)\), which matches v1's leftover \(L^2/(2n)\).
3. The cumulant terms. Their second differences are \(O(L^2/n^2)\) in the
   regular case.
4. The overlap law at a tilt \(x-1=\Theta(1)\). Low factorial cumulants are
   not justified there. The exact route is
   \(\sum_{A\subseteq F_1}(x-1)^{|A|}N(K_n-A,L\mathbf 1-\boldsymbol a)\), with each term
   from Isaev--McKay Theorem 1.2, and this sum has to be resummed.

## Open questions this exposes

- Is the \(L^2/(2n)\) term cancelled by other \(L^2/n\) terms, such as the edge
  term \(-(1-\lambda)T/(\lambda n)\) at the tilted mean, or the \(n/(n-1)\) in \(\mu\)?
  If it is not cancelled, \(\Var Z_L/(\EE Z_L)^2\) does not tend to 0 for
  \(L\gg\sqrt n\), and Conjecture factor-moment would be false as stated.
- The cycle heuristic gives a transfer eigenvalue \(-1/(D-1)\) for
  \(L\)-factor indicators, independent of \(L\). That predicts no cycle
  obstruction. So any surviving \(L^2/n\) term would have to come from a
  non-cycle source.
