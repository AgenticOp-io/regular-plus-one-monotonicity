# Defective +1 — first attempt (B1)

## Target

**Conjecture.** For even \(n\) and \(3\le d\le n^{2/3}\), there exist a coupling
\((G,H)\) with \(G\sim G(n,d)\), \(H\sim G(n,d+1)\), and a (random) edge set \(F\) with
\[
\mathbb{E}|F|\le n^{1/3}\log n
\qquad\text{and}\qquad
\mathbb{P}\bigl(G\subset H\cup F\bigr)=1-o(1).
\]

## Construction sketch

Use Gao’s bipartite coupling graph \(X\) between \(\mathcal{G}(n,d)\) and
\(\mathcal{G}(n,d+1)\) as in Theorem 19.

**Sparse regime \(d=o(\sqrt{n}/\mathrm{polylog})\).**  
Take \(F=\emptyset\); the main theorem already gives exact inclusion.

**Medium regime \(\sqrt{n}/\mathrm{polylog}\le d\le n^{2/3}\).**  
1. Still form the auxiliary digraph with arcs \(G\to G'\) whenever \(G\subset G'\).
2. Matching counts \(Y,Z\) no longer concentrate at relative error \(o(1)\).
   Define the **bad** set
   \[
   B
   =
   \bigl\{G'\in\mathcal{G}(n,d+1):
   \bigl|Y(G')/\mathbb{E} Y-1\bigr|\ge \alpha\bigr\}
   \]
   with a larger window, e.g. \(\alpha=n^{-1/6}\).
3. On the good set, run Gao’s acceptance probabilities.
4. On the bad set, or when acceptance fails, **sprinkle** a random set \(F\) of
   at most \(n^{1/3}\) edges from \(G\setminus H\) (the symmetric difference stubs)
   into the container \(H\cup F\).

## Lemma (crude size of bad set) — PARTIAL

By Markov,
\[
\mathbb{P}(G'\in B)
\le
\frac{\mathrm{Var}\,Y}{\alpha^2(\mathbb{E} Y)^2}.
\]
Even without sharp asymptotics for \(\mathrm{Var}\,Y\) when \(d\sim n^{1/2}\),
configuration-model second moments typically give
\[
\frac{\mathrm{Var}\,Y}{(\mathbb{E} Y)^2}
=
O\bigl(d^{-c}+d^2/n\bigr)
\]
for some \(c>0\) (to be proved). With \(\alpha=n^{-1/6}\) and \(d\le n^{2/3}\),
\[
\frac{d^2}{n\alpha^2}
\le
\frac{n^{4/3}}{n\cdot n^{-1/3}}
=
n^{2/3},
\]
which is **too large** — Markov alone does not kill \(B\).

**Fix needed.** Either:
- prove stronger concentration of \(Y\) (e.g. \(\log Y\) concentration), or
- allow \(|F|\) as large as the typical matching deficit,
  \(\sim \alpha\cdot(\text{mean matching size scale})\), or
- switch to a different defective notion (\(\Delta(F)\) bound instead of \(e(F)\)).

## Revised defective goal (more realistic)

**Conjecture B1′.**  
For \(d\le n^{2/3}\), there is a coupling with
\[
\mathbb{P}\bigl(\Delta(G\setminus H)\le n^{\varepsilon}\bigr)=1-o(1)
\]
for every fixed \(\varepsilon>0\) (or \(\le(\log n)^{C}\)).

This matches Kim–Vu’s classical “defect in the upper sandwich” style and would
already transfer all properties resilient to \(n^{\varepsilon}\) edge deletions/additions.

## Next micro-step

Compute or cite a bound on \(\mathrm{Var}\log Y\) / relative mean absolute deviation
of perfect-matching counts for \(d\le n^{2/3}\) in the configuration model.
If \(\mathbb{E}|Y/\mathbb{E}Y-1|=O(d^{-1}+d/\sqrt{n})\), defective +1 with small \(F\) becomes
plausible again.
