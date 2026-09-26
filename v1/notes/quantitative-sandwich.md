# Conjecture Q — quantitative sandwich at the Chernoff floor

## Partial theorem (proved)

**Theorem (rate \(1/17\)).**
BIM’s own B2 budget yields the sandwich for
\[
\varepsilon\ge C\Bigl(\frac{\log n}{d}\Bigr)^{1/17}.
\]
See `bim-error-budget.md` and `paper/main.tex` Theorem quant.
This sits strictly between fixed \(\varepsilon\) (BIM Thm 1.1) and Conjecture Q.

## Necessity (proved)

**Proposition (Chernoff floor).**
Let \(p=(1-\varepsilon)d/n\) with \(d\ge 2\log n\) and \(0<\varepsilon<1/2\).
If \(\varepsilon\le c\sqrt{(\log n)/d}\) for a sufficiently small absolute \(c>0\), then
\[
\mathbb{P}\bigl(\Delta(G(n,p))>d\bigr)\not\to 0.
\]
Hence no coupling can place \(G(n,p)\subseteq G(n,d)\) with probability \(1-o(1)\).

**Proof sketch.**
Degree of a fixed vertex is \(\mathrm{Bin}(n-1,p)\), mean \(\lambda=(1-\varepsilon)d(1-O(1/n))\).
The upper tail \(\mathbb{P}(\mathrm{Bin}\ge d)\) is bounded below by a constant when
\(d-\lambda\le O(\sqrt{\lambda})\), i.e. \(\varepsilon d=O(\sqrt{d})\), i.e.
\(\varepsilon=O(\sqrt{1/d})\). A second-moment / Janson argument on the number of
vertices with degree \(>d\) shows this count is \(\omega(1)\) whp for small \(c\).
(Standard ER degree extremes; cf. Bollobás.)

Thus any quantitative sandwich requires
\[
\varepsilon=\omega\Bigl(\sqrt{\frac{\log n}{d}}\Bigr)
\]
(up to the precise log power in the extreme-value threshold).

## Conjecture Q

**Conjecture Q (near-optimal sandwich).**
There exists an absolute constant \(C_0\) such that the following holds.
Whenever \(d\ge C_0\log n\) and
\[
\varepsilon=\varepsilon(n,d)\ge C_0\sqrt{\frac{\log n}{d}},
\]
there is a coupling \((G_*,G,G^*)\) with
\[
G_*\sim G(n,(1-\varepsilon)d/n),\quad
G\sim G(n,d),\quad
G^*\sim G(n,(1+\varepsilon)d/n),
\]
and \(\mathbb{P}(G_*\subset G\subset G^*)=1-o(1)\).

**Status.** Open. The obstacle inside the BIM process is the factor
\((n\log n/m)^{1/8}\) in \(\eta_m\); removing or weakening it is the attack.

## Conditional consequences of Q

**Theorem Q1 (assuming Q).**
If \(d\ge C_0\log n\) and \(k\ge 3C_0\sqrt{d\log n}\), then there is a coupling of
\(G\sim G(n,d)\) and \(H\sim G(n,d+k)\) with \(\mathbb{P}(G\subset H)=1-o(1)\).

**Theorem Q2 (assuming Q) — sharp defect.**
Under the same hypotheses as Q, there is a coupling of \(G\sim G(n,d)\) and
\(H\sim G(n,d+1)\) with
\[
\mathbb{P}\bigl(\Delta(G\setminus H)\le C\sqrt{d\log n}\bigr)=1-o(1).
\]

(Analogues at rate \(1/17\) are unconditional: Corollary quant-nest in the paper.)

