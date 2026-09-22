# Toward +1 monotonicity up to \(d=o(\sqrt{n})\)

## Abstract

We outline a program to extend Gao’s nesting theorem
\(G(n,d)\subset G(n,d+1)\) from \(d=o(n^{1/3})\) to \(d=o(n^{1/2})\),
by substituting Gao’s sharper conditional edge probabilities
(arXiv:2012.01492, Thm 6) into the coupling of arXiv:2104.11850, Thm 19.

## 1. Introduction

The Gao–Isaev–McKay monotonicity conjecture asks for couplings
\(G(n,d_1)\subset G(n,d_2)\) whenever \(d_1\le d_2\) (with two exceptions).
The critical case is \(d_2=d_1+1\). Gao proved this for
\(d\to\infty\) and \(d=o(n^{1/3})\), and noted that \(o(n^{1/2})\) should follow
from sharper subgraph probabilities. We make that program explicit.

## 2. Easy regime (complete)

Constant-factor gaps via Behague–Ilʼkovič–Montgomery sandwich: see
`notes/proof-easy-regime.md`.

## 3. Reduction (complete)

Iterated +1 ⇒ full monotonicity for even \(n\): see `notes/proof-reduction.md`.

## 4. Main conditional theorem

Assume the patched second-moment estimate (Lemma L2) with error \(O(d^2/n)\).
Then for \(d\to\infty\) and \(d=o(n^{1/2}/\log^2 n)\),
\[
\mathbb{P}(G(n,d)\subset G(n,d+1))=1-o(1).
\]
Proof: `notes/attack-n-half.md` (Lemmas L4 + L5).

## 5. Remaining calculation

Lemma L2 — rebuild Gao Thm 10 with arXiv:2012.01492 Thm 6.
Ledger: `notes/lemma-L2-draft.md`.

## 6. Experiments

Small-\(n\) TV: `src/experiments.py`.  
\(\eta\)-schedules: `src/config_probes.py`.

## References

- Kim–Vu 2004
- Gao arXiv:2012.01492
- Gao arXiv:2104.11850
- Behague–Ilʼkovič–Montgomery arXiv:2510.20765
- Hollom–Lichev–Mond–Portier–Wang arXiv:2505.22875
