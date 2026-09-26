# BIM error budget → quantitative sandwich at \((\log n/d)^{1/17}\)

## Source
Behague–Il'kovič–Montgomery, arXiv:2510.20765, especially:
- Theorem 2.4 (switching / near-uniform edge inclusion)
- Section 3.5.5 (event B2), displayed estimate ending at their (essentially)
  \[
  2C_0\mu\,dn + 4C_0\,dn\Bigl(\frac{10n\log n}{\varepsilon dn}\Bigr)^{1/8}
  \le \frac{R}{2},\qquad R=\lfloor\varepsilon dn/8\rfloor.
  \]
- Hierarchy for the upper process:
  \[
  \tfrac1n\ll\tfrac1C\ll\mu\ll\tfrac1{C_0}\ll\varepsilon\ll 1,\qquad d\ge C\log n.
  \]
- Error schedule:
  \[
  \eta_m=C_0\max\Bigl\{\tfrac{\mu}{\log n},\Bigl(\tfrac{n\log n}{m}\Bigr)^{1/8}\Bigr\}.
  \]

## Budget inequalities (must hold)

From \(2C_0\mu\,dn\le R/4\) and \(4C_0 dn(10\log n/(\varepsilon d))^{1/8}\le R/4\):

1. \(C_0\mu = O(\varepsilon)\)
2. \(C_0\bigl(\log n/(\varepsilon d)\bigr)^{1/8} = O(\varepsilon)\)

From the hierarchy: \(C_0=\omega(1/\varepsilon)\) and \(\mu=o(1/C_0)\).

## Optimising ε

Take \(C_0=\Theta(1/\varepsilon)\) (large implied constant) and \(\mu=\Theta(\varepsilon^2)\).
Constraint 1 holds.
Constraint 2 becomes
\[
\frac1\varepsilon\Bigl(\frac{\log n}{\varepsilon d}\Bigr)^{1/8}=O(\varepsilon)
\quad\Longleftrightarrow\quad
\frac{\log n}{\varepsilon d}=O(\varepsilon^{16})
\quad\Longleftrightarrow\quad
\varepsilon=\Omega\Bigl(\Bigl(\frac{\log n}{d}\Bigr)^{1/17}\Bigr).
\]
(The same exponent appears with more careful \(\omega/\ll\) bookkeeping.)

## Hierarchy closes for this ε

Set \(\varepsilon=C_*(\log n/d)^{1/17}\) with \(C_*\) large, \(C_0=10/\varepsilon\), \(\mu=\varepsilon^2/1000\),
and \(C=\Theta(1/\mu)=\Theta(1/\varepsilon^2)\).
The demand \(d\ge C\log n\) reduces to \(d=\Omega(\log n)\) after substituting ε,
for \(C_*\) large enough. Details in `paper/main.tex`.

## What this does / does not claim

**Does:** BIM’s *existing* reduction “Theorem 2.4 ⇒ upper sandwich” (their §3)
already gives a vanishing ε of rate \((\log n/d)^{1/17}\), once the hierarchy is
instantiated. They stated only the fixed-ε theorem; the rate is an accounting corollary
of their B2 estimate.

**Does not:** Re-prove Theorem 2.4. We use it as a black box under its stated hierarchy
(which permits \(\varepsilon=\varepsilon(n)\to 0\)).

**Does not:** Reach the Chernoff floor \(\varepsilon\asymp\sqrt{(\log n)/d}=(\log n/d)^{1/2}\).
The gap is the exponent \(1/17\) vs \(1/2\), caused by the \(\,{}^{1/8}\) in \(\eta_m\).
Improving that power in the switching argument is the remaining path to Conjecture Q.

## Consequences

| Result | Strength |
|---|---|
| Upper sandwich at \(\varepsilon=C(\log n/d)^{1/17}\) | new stated rate |
| Nesting increment \(k\ge 3\varepsilon d=C'\,d^{16/17}(\log n)^{1/17}\) | past \(\sqrt{n}\) for large \(d\) |
| Degree defect \(O\bigl(d^{16/17}(\log n)^{1/17}\bigr)\) | sharpest defect from BIM budget |
| Full Conjecture Q | still open |

## Lower sandwich

Lemma 2.2 uses a fixed \(\eta\ll\varepsilon\) and \(m\ge\varepsilon dn\). The same ε-rate
works for the lower half by the same hierarchy (no \(R^{-1/8}\) accumulation).
Combined: full two-sided sandwich at this rate.

## Next improvement levers

1. Replace \(\eta_m\)’s \(\,{}^{1/8}\) by a smaller power (better switching-path concentration).
2. Split the B2 sum into regimes so the \(R^{-1/8}\) integral is less wasteful.
3. Directly target Chernoff floor with a different coupling (process conjecture).
