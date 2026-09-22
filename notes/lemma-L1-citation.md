# Lemma L1 — sharper conditional edge probabilities (citation)

## Source

Pu Gao, *Triangles and subgraph probabilities in random regular graphs*,
arXiv:2012.01492. **Theorem 6** (and Remarks 7–8).

## What we need

Gao (2104.11850) Remark 16(b) + §5: replacing McKay-style relative error \(O(d/n)\)
(feeding \(O(d^3/n)\) into matching probabilities) by the sharper Theorem 6 estimate
is the intended route to extend nesting from \(d=o(n^{1/3})\) toward \(d=o(n^{1/2})\).

## Theorem 6 (statement we will use)

For a degree sequence \(\mathbf{d}\) with \(M=\sum d_i\) even, \(\Delta^2=o(M)\), and
disjoint graphs \(H_1,H_2\) under the paper’s degree hypotheses,
\[
\mathbb{P}\bigl(uv\in\mathcal{G}(n,\mathbf{d})\mid H_1^+,H_2^-\bigr)
=
\Bigl(1+O\bigl(\tfrac{\Delta^5 n}{M^3}\bigr)\Bigr)
\cdot(\text{explicit main term involving }\widetilde{\mathbf{d}},\bar\phi).
\]
For \(d\)-regular graphs, \(M=dn\), \(\Delta=d\), the relative error is
\[
O\Bigl(\frac{d^5 n}{(dn)^3}\Bigr)=O\Bigl(\frac{d^2}{n^2}\Bigr).
\]

## Remark 8 (perfect-matching probabilities)

McKay’s classical bound gives
\[
\mathbb{P}(H\subset G(n,d))
\quad\text{with relative error}\quad O(d^3/n).
\]
Theorem 6 upgrades this to relative error
\[
O\bigl(d^2|H|/n^2\bigr).
\]
For \(H\) a perfect matching (\(|H|=n/2\)) this is \(O(d^2/n)\), which is \(o(1)\) precisely
when \(d=o(n^{1/2})\) — matching our target window.

## Status in this project

- **L1 = Theorem 6:** treated as an external black box (cite, do not re-prove).
- **L2:** rebuild Gao (2104.11850) Corollary 15 / matching-count inputs using Remark 8.
- That calculation is the next writeup: `notes/lemma-L2-draft.md`.
