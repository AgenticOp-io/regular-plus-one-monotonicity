# Lemma L2 draft — patched matching probability error \(O(d^2/n)\)

## Target

**Lemma L2.** Let \(n\) be even, \(d\to\infty\), \(d=o(n^{1/2})\). Let \(Y\) be the number of
perfect matchings in \(G\sim G(n,d)\). Then
\[
\mathbb{E} Y
=
\frac{n!}{(n/2)!\,2^{n/2}}
\Bigl(\frac{e}{n}\Bigr)^{n/2}
\Bigl(\frac{d-1}{d}\Bigr)^{\binom{d-1}{2}n}
\Bigl(\frac{d}{n}\Bigr)^{n/2}
\exp\Bigl(\tfrac14+O\bigl(\tfrac{d^2}{n}\bigr)\Bigr),
\]
and the second-moment ratio satisfies
\[
\frac{\mathbb{E}[Y^2]}{(\mathbb{E}Y)^2}
=
1+\frac{1}{6d^3}+O\Bigl(d^{-4}+\frac{d^2}{n}+\sqrt{\frac{d}{n}}\log^3 n\Bigr).
\]
(Compare Gao arXiv:2104.11850 Theorem 10, where the middle error is \(d^3/n\).)

## Proof plan

1. Write \(Y=\sum_{M\in\mathcal{M}_n}\mathbf{1}_{M\subset G}\) over perfect matchings.
2. For each fixed \(M\), apply Gao arXiv:2012.01492 Remark 8 / Theorem 6 to get
   \[
   \mathbb{P}(M\subset G)
   =
   \bigl(1+O(d^2/n)\bigr)\,p_0(M),
   \]
   with \(p_0\) the same main-term product used by Gao (2104.11850).
3. Sum over \(M\) to get \(\mathbb{E}Y\) with cumulative error \(O(d^2/n)\)
   (not \(O(d^3/n)\)).
4. For \(\mathbb{E}[Y^2]\), expand pairs of matchings \((M,M')\) by intersection type
   (Gao’s classification). In each class, apply Theorem 6 to the edge-exposure product.
5. Track that every place Gao invokes the weaker McKay \(O(d^3/n)\) is replaced by
   \(O(d^2/n)\) or \(O(d^2|H|/n^2)\) with \(|H|\le n\).

## Bookkeeping ledger (to fill while reading Gao §3)

| Gao (2104.11850) location | Uses weaker error? | Patch |
|---|---|---|
| Cor 15 / Thm 14 applications | yes | invoke 2012.01492 Thm 6 |
| Thm 10 display (2)–(3) | yes \(O(d^3/n)\) | replace |
| Thm 19 eqs (22)–(28) Chebyshev inputs | inherits Thm 10 | auto |
| \(Z(G)\) complement matching averages | yes | same patch on \(\overline{G}\) |

## Status

**Not yet fully expanded.** This note is the contract for the calculation.
Once the ledger rows are checked line-by-line against Gao’s PDF, L2 becomes a
proposition with a complete proof.

## Immediate micro-task

Take Gao (2104.11850) proof of Theorem 10, Section 3, and produce a diff comment
file `notes/gao-thm10-diff.md` listing every inequality that cites Corollary 15 /
Theorem 14 / McKay enumeration with the \(d^3/n\) term.
