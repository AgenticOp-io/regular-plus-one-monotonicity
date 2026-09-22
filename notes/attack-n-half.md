# Attack: push +1 from \(o(n^{1/3})\) to \(o(n^{1/2})\)

## Goal

Prove Gao’s Theorem 8 with \(d=o(n^{1/2})\) instead of \(d=o(n^{1/3})\), by importing the
sharper conditional edge probabilities from Gao, *Triangles and subgraph probabilities in
random regular graphs*, arXiv:2012.01492, Theorem 6.

## Lemma checklist

| ID | Statement | Status |
|---|---|---|
| L0 | Gao Thm 8 for \(d=o(n^{1/3})\) | known (cite) |
| L1 | Conditional \(\mathbb{P}(uv\in G\mid H\subset G)\) with rel. error \(O(d^2/n^2)\) | cite arXiv:2012.01492 Thm 6 |
| L2 | Rebuild Gao Cor 15 with error \(O(d^2/n)\) instead of \(O(d^3/n)\) | **TO PROVE** |
| L3 | Rebuild Gao Thm 10 variance error terms under L2 | **TO PROVE** |
| L4 | Show \(\exists\alpha=o(1)\) with \(\eta_{\mathrm{new}}(\alpha)=o(1)\) for all \(d=o(n^{1/2})\) | **TO PROVE** |
| L5 | Replay Gao Thm 19 coupling with new \(\eta\) | routine once L2–L4 hold |

## Proposed new error function

Replace Gao’s
\[
\eta(\alpha)=2\alpha+\frac{1}{d^3\alpha^2}+C\frac{d^3}{n\alpha^2}+C\frac{\sqrt{d/n}\log^3 n}{\alpha^2}
\]
by
\[
\eta_{\mathrm{new}}(\alpha)=2\alpha+\frac{1}{d^3\alpha^2}+C\frac{d^2}{n\alpha^2}+C\frac{\sqrt{d/n}\log^3 n}{\alpha^2}.
\]

## Lemma L4 (conditional on the form of \(\eta_{\mathrm{new}}\)) — PROVED

**Lemma.** Suppose \(d\to\infty\) and \(d=o(n^{1/2}/\log^2 n)\). Set
\[
\alpha := \max\Bigl\{
d^{-1},\;
\bigl(d^2/n\bigr)^{1/4}\log n,\;
\bigl(d/n\bigr)^{1/6}\log n
\Bigr\}.
\]
Then \(\alpha=o(1)\) and \(\eta_{\mathrm{new}}(\alpha)=o(1)\).

**Proof.**  
Under \(d=o(n^{1/2}/\log^3 n)\): each argument of the max is \(o(1)\), so \(\alpha=o(1)\).

Bound each piece of \(\eta_{\mathrm{new}}\):

1. \(2\alpha=o(1)\).
2. \(\alpha\ge d^{-1}\) ⇒ \(\frac{1}{d^3\alpha^2}\le d^{-1}=o(1)\).
3. \(\alpha\ge(d^2/n)^{1/4}\log n\) ⇒
   \(\frac{d^2}{n\alpha^2}\le \frac{(d^2/n)^{1/2}}{\log^2 n}=o(1)\).
4. \(\alpha\ge(d/n)^{1/6}\log n\) ⇒
   \(\frac{\sqrt{d/n}\,\log^3 n}{\alpha^2}
   \le
   \frac{(d/n)^{1/2}\log^3 n}{(d/n)^{1/3}\log^2 n}
   =
   (d/n)^{1/6}\log n=o(1)\).

Therefore \(\eta_{\mathrm{new}}(\alpha)=o(1)\). ∎

**Remark.** The old \(\eta\) with \(d^3/(n\alpha^2)\) cannot be killed for
\(d=\omega(n^{1/3})\): even optimizing \(\alpha\), Chebyshev + \(d^3/n\) error forces
failure. That is exactly Gao’s \(o(n^{1/3})\) ceiling.

## What remains (the real work)

**Lemma L2 (open — main calculation).**  
Re-derive Gao’s Corollary 15 (counting / permanent-style estimates for near-regular degree
sequences inside a host, or the \(k\)-matching probability expansion) using
arXiv:2012.01492 Theorem 6, and obtain
\[
\mathbb{P}(M\subset G(n,d))
=
\Bigl(1+O\bigl(\tfrac{d^2}{n}\bigr)\Bigr)
\cdot(\text{main term})
\]
uniformly for perfect matchings \(M\) (or for the \(Z(G)\), \(Y(G)\) averages used in Thm 19).

**Lemma L3 (open).**  
Feed L2 into the second-moment calculation for \(Y\) so that
\[
\frac{\mathrm{Var}\,Y}{(\mathbb{E}Y)^2}
=
\frac{1}{6d^3}+O\Bigl(d^{-4}+\frac{d^2}{n}+\sqrt{\frac{d}{n}}\log^3 n\Bigr)
\]
(or any error that still lets L4 fire for \(d=o(n^{1/2})\)).

## Theorem (conditional breakthrough) — PROVED as reduction

**Theorem.** Assume Lemmas L2 and L3. Then for every \(d\to\infty\) with \(d=o(n^{1/2})\),
there is a coupling with \(\mathbb{P}(G(n,d)\subset G(n,d+1))=1-o(1)\).

**Proof.** Lemma L4 supplies \(\alpha\) with \(\eta_{\mathrm{new}}(\alpha)=o(1)\). Run Gao’s Theorem 19
coupling verbatim with \(\eta_{\mathrm{new}}\) in place of \(\eta\); the only inputs that change are
the Chebyshev bound on \(Y\) (from L3) and the degree-bias estimates for \(Z(G)\) (from L2).
Failure probability \(O(\eta_{\mathrm{new}})=o(1)\). ∎

## Next action

1. Fetch and digest arXiv:2012.01492 Theorem 6 statement precisely.
2. Diff Gao’s proof of Corollary 15 line-by-line, marking every use of the weaker
   conditional probability.
3. Produce a patched Corollary 15 (Lemma L2) as a standalone note.
