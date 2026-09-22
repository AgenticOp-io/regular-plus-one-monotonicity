# Contiguity blocked; next rate from BIM path exponents

## Hybrid contiguity — dead

Comparing hybrid \(H=G\cup R_q\) to nested ER on \(G^*_0\) at retention
\(r=(1+\varepsilon)/(1+\varepsilon_0)\) gives \(\chi^2=\Theta(dn)\) between the two
inhomogeneous Bernoulli measures. Contiguity fails; do not chase TV of hybrid to ER.

## Where the \(1/8\) comes from (BIM)

| Object | Relative error | Source |
|---|---|---|
| Degrees in \(F\setminus K\) | \(\sqrt{\log n/\delta}\) | Lemma 5.3 G1 (Chernoff-optimal) |
| Paths from a vertex (upper) | \((\log n/\delta)^{1/4}\) | Lemma 5.1 with \(\lambda=(\cdots)^{1/4}\) |
| Paths \(x\)–\(y\) (lower) | \((\log n/\delta)^{1/4}\) | Theorem 6.1 |
| Paths \(x\)–\(y\) (upper) | \((\log n/\delta)^{1/8}\) | Lemma 7.1 via \(\lambda=(\eta/C_0)^2\) |

Lemma 7.1 forces \(\lambda=O(\eta^2)\) through the truncation-set size \(|B|\) bound.
That square-root degradation turns the natural \(1/4\) into the schedule’s \(1/8\).

## Rate dictionary

If two-sided path error is \(O((\log n/\delta)^{\alpha})\), B2 with absolute \(C_0\) gives
\[
\Bigl(\frac{\log n}{\varepsilon d}\Bigr)^{\alpha}=O(\varepsilon)
\quad\Rightarrow\quad
\varepsilon=\Omega\Bigl(\Bigl(\frac{\log n}{d}\Bigr)^{1/(1+1/\alpha)?}\Bigr)
\]
wait: \((\log n/(\varepsilon d))^{\alpha}=O(\varepsilon)\) ⇒ \(\log n/(\varepsilon d)=O(\varepsilon^{1/\alpha})\)
⇒ \(\varepsilon^{1+1/\alpha}=\Omega(\log n/d)\) ⇒
\[
\varepsilon=\Omega\Bigl(\Bigl(\frac{\log n}{d}\Bigr)^{1/(1+1/\alpha)}\Bigr)
=\Omega\Bigl(\Bigl(\frac{\log n}{d}\Bigr)^{\alpha/(\alpha+1)}\Bigr).
\]

| \(\alpha\) | Rate \(\alpha/(\alpha+1)\) | Status |
|---|---|---|
| \(1/8\) | \(1/9\) | proved (current Thm quant) |
| \(1/4\) | \(1/5\) | **conditional on fixing Lemma 7.1** |
| \(1/2\) | \(1/3\) | Hypothesis P (process-optimal) |

## Target Theorem (rate \(1/5\))

**Hypothesis U.** For \(\delta\ge C\log n\), two-vertex \((F\setminus K,K)\)-alternating path
upper counts hold at relative error \(O((\log n/\delta)^{1/4})\)
(same scale as Theorem 6.1 lower bounds / Lemma 5.1).

**Then:** quantitative sandwich at \(\varepsilon=C(\log n/d)^{1/5}\) for all \(d\ge C\log n\).

## How to prove Hypothesis U

Avoid Lemma 7.1’s \(\lambda=\eta^2\) truncation. Options:
1. Couple the two-vertex upper bound to the one-vertex upper bound (Lemma 5.1) plus
   a lower-bound correction from Theorem 6.1 at \(\lambda=\eta\).
2. Apply Kim–Vu polynomial concentration directly to the two-vertex path polynomial
   at the \(1/4\) scale (as BIM §8 does for \(\delta\ge n^{\sigma}\)).
3. Freedman martingale along the path exploration with variance proxy \(\delta^{\ell}d^{\ell}/n\).
