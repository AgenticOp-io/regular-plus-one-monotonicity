# Strongest theorems past \(o(\sqrt{n})\) — clean statements

Cross-reference: detailed proofs in `medium-regime-theorems.md`.

---

## A. Exact nesting (already proved)

**Theorem.** Assume Gao arXiv:2012.01492 Thm 6. If \(d\to\infty\) and
\(d=o(n^{1/2}/\log^3 n)\), then
\[
\exists\text{ coupling: }\mathbb{P}\bigl(G(n,d)\subset G(n,d+1)\bigr)=1-o(1).
\]

---

## B. Always-nested, law-approximate (new)

**Theorem.** Let \(n\) even and \(3\le d\le n/2-1\) (so every complement of a \(d\)-regular
graph has degree \(\ge n/2\), hence has a perfect matching by Dirac). Then there is a
coupling \((G,H)\) with:

1. \(G\subset H\) with probability 1;
2. \(H\sim\mu_d\oplus\mu_1\) exactly (hence \(H\) is exactly \((d+1)\)-regular);
3. \(\mathrm{d_{TV}}(H,\;\mu_{d+1})\le \mathrm{d_{TV}}(\mu_d\oplus\mu_1,\mu_{d+1})\).

Coupling \(H\) onward to an exact \(\mu_{d+1}\) copy \(H'\) by optimal coupling, one obtains
\(G\subset H'\) on the event \(\{H=H'\}\), which has probability
\(1-\mathrm{d_{TV}}(\mu_d\oplus\mu_1,\mu_{d+1})\).

**Corollary.** If \(\mathrm{d_{TV}}(\mu_d\oplus\mu_1,\mu_{d+1})\le\delta\), then there is a
coupling with \(H\sim\mu_{d+1}\) and
\[
\mathbb{P}(G\subset H)\ge 1-\delta,
\]
where \(G\) has law within TV distance \(\delta\) of \(\mu_d\).

---

## C. TV bound from moments (new packaging)

**Theorem.** If \(\mathbb{P}(|Y-\mathbb{E}Y|\ge\alpha\mathbb{E}Y)\le\delta\) with \(\alpha<1/2\), then
\[
\mathrm{d_{TV}}(\mu_d\oplus\mu_1,\mu_{d+1})\le 10(\alpha+\delta).
\]

**Corollary (small-\(c\) square-root window).**  
Assume the patched variance formula for \(d\le c\sqrt{n}\). Choosing \(\alpha\) fixed small
and \(c\) small enough that \(d^2/n\le\alpha^2/100\), Chebyshev gives \(\delta\le 1/100\),
hence
\[
\mathrm{d_{TV}}(\mu_d\oplus\mu_1,\mu_{d+1})\le 1/2
\]
for large \(n\). Combined with B:
\[
\mathbb{P}(G\subset H)\ge 1/2
\quad\text{with }H\sim\mu_{d+1},\ \mathrm{d_{TV}}(\mathrm{law}G,\mu_d)\le 1/2.
\]

---

## D. Sandwich defect (new packaging of BIM)

**Theorem.** For each fixed \(\varepsilon\in(0,1)\) and \(d\ge C(\varepsilon)\log n\),
there is a coupling and a graph \(F\) with
\[
\mathbb{P}(G\subset H\cup F)=1-o(1),
\qquad
\mathbb{P}\bigl(\Delta(F)\le 3\varepsilon d\bigr)=1-o(1).
\]

---

## E. What we cannot reach with present tools

Exact whp +1 for \(d=\omega(\sqrt{n})\): blocked by cumulative conditional-probability
error \(\Omega(d^2/n)\).

---

## Recommended interpretation

The project’s publishable claims, in order of strength:

1. Exact +1 to \(o(\sqrt{n}/\mathrm{polylog})\) — **main theorem**.
2. Always-nested coupling with TV\(\le 1/2\) for \(d\le c\sqrt{n}\) — **secondary**.
3. Degree-defect \(O(\varepsilon d)\) for all \(d\ge C\log n\) via sandwich — **easy corollary**.
