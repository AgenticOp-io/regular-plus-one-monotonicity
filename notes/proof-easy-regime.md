# Easy regime: constant-factor degree gaps via the sandwich theorem

This note records a **complete proof** of a regime already implied by
Behague–Ilʼkovič–Montgomery (BIM), Theorem 1.1. It is our baseline and the template
for how ER transit yields regular monotonicity.

## Theorem (Easy monotonicity)

Let \(\varepsilon\in(0,1)\) and let \(C=C(\varepsilon)\) be as in BIM Theorem 1.1.
Suppose \(d_1\ge C\log n\), \(d_2\ge \dfrac{1+\varepsilon}{1-\varepsilon}\,d_1\), and \(d_1 n\), \(d_2 n\) are even.
Then there is a coupling with
\[
\mathbb{P}\bigl(G(n,d_1)\subset G(n,d_2)\bigr)=1-o(1).
\]

## Proof

Apply BIM Theorem 1.1 twice.

1. There is a coupling so that, with probability \(1-o(1)\),
   \[
   G(n,d_1)\;\subset\;G\!\Bigl(n,(1+\varepsilon)\frac{d_1}{n}\Bigr).
   \]
2. There is a coupling so that, with probability \(1-o(1)\),
   \[
   G\!\Bigl(n,(1-\varepsilon)\frac{d_2}{n}\Bigr)\;\subset\;G(n,d_2).
   \]

By the hypothesis \(d_2\ge \frac{1+\varepsilon}{1-\varepsilon}d_1\),
\[
(1+\varepsilon)\frac{d_1}{n}\;\le\;(1-\varepsilon)\frac{d_2}{n}.
\]
Under the standard monotone coupling of binomial random graphs
(same uniforms \(U_e\sim\mathrm{Unif}[0,1]\), keep edge \(e\) in \(G(n,p)\) iff \(U_e<p\)),
\[
G\!\Bigl(n,(1+\varepsilon)\frac{d_1}{n}\Bigr)
\;\subset\;
G\!\Bigl(n,(1-\varepsilon)\frac{d_2}{n}\Bigr)
\]
almost surely.

Glue the three couplings on one probability space (e.g. via a product space and
the usual transfer). On the intersection of the two BIM high-probability events,
\[
G(n,d_1)
\;\subset\;
G\!\Bigl(n,(1+\varepsilon)\tfrac{d_1}{n}\Bigr)
\;\subset\;
G\!\Bigl(n,(1-\varepsilon)\tfrac{d_2}{n}\Bigr)
\;\subset\;
G(n,d_2).
\]
Hence \(\mathbb{P}(G(n,d_1)\subset G(n,d_2))=1-o(1)\).

## Remark (why this is not +1)

The degree gap must be a **constant factor**. In particular this never yields
\(d_2=d_1+1\) for \(d_1\to\infty\), since
\[
\frac{d_1+1}{d_1}=1+o(1) < \frac{1+\varepsilon}{1-\varepsilon}
\]
for large \(d_1\). Closing that gap is the whole project.

## Club-sandwich corollary

Iterating the theorem along a geometric ladder
\(d_{i+1}\ge \rho d_i\) with \(\rho=(1+\varepsilon)/(1-\varepsilon)\)
gives a coupled chain of length \(\Theta(\log n)\). This is maximal for sandwich-transit
methods; longer chains need \(+1\) (or \(o(d)\) increments).
