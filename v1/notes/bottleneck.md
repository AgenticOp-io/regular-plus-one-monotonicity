# Bottleneck analysis (corrected Stage-1 target)

## Critical correction

**Gao (arXiv:2104.11850), Theorem 8** already proves exact +1 monotonicity:
\[
d\to\infty,\quad d=o(n^{1/3})
\quad\Longrightarrow\quad
\exists\text{ coupling }G(n,d)\subset G(n,d+1)\text{ a.a.s.}
\]
HLMPW’s \(n^{1/10}\) ceiling is only for their **TV-iteration / matching-decomposition** package
(Corollary 3.2), not for bare +1 inclusion.

So our earlier Stage-1 goal “beat \(n^{1/10}\)” was aiming at the wrong wall.

## True frontier for +1

| Regime | Status | Source |
|---|---|---|
| \(d=O(1)\) special cases | done (overlay methods) | HLMPW |
| \(\omega(1)=d=o(n^{1/3})\) | **done** | Gao Thm 8 |
| \(d=o(n^{1/2})\) | **flagged as likely, not written** | Gao Remark 16(b) + §5 |
| \(n^{1/2}\lesssim d\ll n\) | open | — |
| \(d=\Theta(n)\) | open (different tools) | — |
| constant-factor gaps, \(d\ge C\log n\) | done | BIM sandwich transit |

## Quantitative obstruction in Gao’s proof

Gao Theorem 19: if \(\alpha=o(1)\) and
\[
\eta(\alpha)
=
2\alpha
+ \frac{1}{d^3\alpha^2}
+ C\frac{d^3}{n\alpha^2}
+ C\frac{\sqrt{d/n}\,\log^3 n}{\alpha^2}
= o(1),
\]
then there is a coupling with
\[
\mathbb{P}(G_d\subset G_{d+1})\ge 1-5\eta.
\]
The term \(d^3/(n\alpha^2)\) with \(\alpha\to 0\) forces \(d=o(n^{1/3})\).

That \(d^3/n\) error enters through **Corollary 15** (enumeration / conditional edge
probabilities). Gao Remark 16(b):

> A stronger version … estimates conditional edge probabilities up to relative error
> \(d^2/n^2\) instead of \(d/n\). … This will result in an improvement in the range of \(d\)
> in … Theorems 8, 10, and 19. … for a simpler proof we [did not].

Gao §5 Future research repeats: improve \(d^3/n\to d^2/n\) via [Gao, arXiv:2012.01492, Thm 6].

## Breakthrough target (revised)

**Theorem (proposed).**  
Suppose \(d\to\infty\) and \(d=o(n^{1/2})\). Then there is a coupling with
\[
\mathbb{P}\bigl(G(n,d)\subset G(n,d+1)\bigr)=1-o(1).
\]

**Method.** Re-run Gao’s Theorem 19 proof with the sharper conditional probabilities from
arXiv:2012.01492, replacing every \(O(d^3/n)\) by \(O(d^2/n)\) (or better), then choose
\[
\alpha = n^{-1/4}d^{1/2}\quad\text{(or an optimized schedule)}
\]
so that \(\eta(\alpha)=o(1)\) throughout \(d=o(n^{1/2})\).

### Heuristic: why \(n^{1/2}\) appears

If the dominant error is \(d^2/(n\alpha^2)\) and we take \(\alpha=d^{-c}\) or
\(\alpha=(d^2/n)^{1/4}\), the constraint \(d^2/(n\alpha^2)\to 0\) with \(\alpha\to 0\)
permits \(d=o(n^{1/2})\). Past \(\sqrt{n}\), even the improved enumeration error is too large
for Chebyshev-level matching concentration alone — need new ideas (BIM switchings,
spectral, process coupling).

## Secondary targets (still valuable)

1. **HLMPW Cor 3.2 past \(n^{1/10}\)** toward \(n^{1/7-\varepsilon}\): needs higher matching moments;
   enables iterated \(\oplus\) decompositions, not just +1.
2. **Defective +1 for \(d\le n^{2/3}\):** \(\Delta(H\setminus G)\le n^{o(1)}\) or \(O(\mathrm{polylog}\,n)\).
3. **Odd \(n\):** +2 via near-perfect matchings / 2-factors.
