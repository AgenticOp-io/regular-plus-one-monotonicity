# GIM tails: Chernoff blocked by structure (not by \(\xi^4\))

## Corrected diagnosis

GIM Lemma 4.3 uses failure \(e^{-\Omega(\xi^4\Delta)}\) under \(\Delta\gg\xi^{-4}\log n\).
Plain Chernoff on \(G_0\sim G(n,p)\) upgrades the **degree** control to
\(e^{-\Omega(\xi^2 d)}\), which at \(\xi=\Theta\sqrt{(\log n)/d}\) is \(n^{-\Omega(1)}\).

**That upgrade is real but insufficient.**

GIM Theorem 2.6 also requires the structural hypothesis
\[
n-\Delta\gg\xi\Delta\gg\frac{n}{\log n}.
\]
For regular \(d\), this forces
\[
\xi\gg\frac{n}{d\log n}.
\]
Chernoff needs only \(\xi\ge C\sqrt{(\log n)/d}\). These are compatible iff
\[
\sqrt{\frac{\log n}{d}}\;\ge\;c\frac{n}{d\log n}
\quad\Longleftrightarrow\quad
d\;\ge\;c'\frac{n^2}{(\log n)^3},
\]
which is impossible for \(d\le n-1\).

Equivalently: \(\xi_{\mathrm{Chernoff}}\cdot d=\sqrt{d\log n}\ll n/\log n\) for all
admissible \(d\). The factor-ratio theorem (GIM Thm 2.9 / (A2)) never fires at
Chernoff scale.

## What GIM does give

Best dense rate from Thm 2.6: \(\xi=\omega(1/\log n)\) when \(d=\Theta(n)\),
or more generally \(\xi=\omega(n/(d\log n))\). This is weaker than our BIM
rate \(1/9\) once \(d\ge(\log n)^{O(1)}\cdot n^{9/8}\) is false — for
\(d=\Theta(n)\), \(1/\log n\) vs \(n^{-1/9}\): actually \(n^{-1/9}\ll 1/\log n\),
so **BIM \(1/9\) already beats GIM dense**.

## Upgraded lemma (still valid, narrow use)

**Lemma (Chernoff degree control).**
If \(G_0\sim G(n,p)\) with \(p\le(1-\xi)d/n\), \(\xi\ge C\sqrt{(\log n)/d}\),
\(d\ge C\log n\), then w.h.p.
\(\Delta(G_0)\le d-\xi d/2\) and all degrees are \((1+O(\xi))p(n-1)\).

Useful inside any coupling that already maintains \(G^{(\iota)}\subseteq G_0\), but
**does not unlock Conjecture Q** through GIM Theorem 2.6.
