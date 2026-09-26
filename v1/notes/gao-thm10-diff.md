# Diff ledger: Gao Thm 10 / Cor 15 vs sharper Thm 6

Source A: Gao, arXiv:2104.11850 (matchings + nesting).  
Source B: Gao, arXiv:2012.01492 (triangles; **Theorem 6**).

## Goal

Every place A uses relative error \(O(d^3/n)\) (via Cor 15 / Thm 14 / McKay)
should become \(O(d^2/n)\) or \(O(d^2|H|/n^2)\) via B.

## Hotspots in A (line refs from ar5iv/pdf extract)

| Location in A | What happens | Patch with B |
|---|---|---|
| **Corollary 15** statement | matching-probability expansion; error inherits Thm 14 | Rebuild proof using B Thm 6; Gao himself says error → \(O(d^2/n)\) (Remark 16(b), §5) |
| **Remark 16(b)** | Explicitly says sharper conditional probs ⇒ better Cor 15 ⇒ better Thms 8, 10, 19 | Our program |
| **Proof of Cor 15** | Applies Thm 14 + Stirling | Swap in B Thm 6 for the edge-product |
| **Thm 10 proof** (~L704) | “Let H be a perfect matching… Cor 15 with k=n/2” | Direct application of B Remark 8: rel. error \(O(d^2|H|/n^2)=O(d^2/n)\) |
| **Thm 10 pairs** (~L736) | Cor 15 for \(|H_1\cap H_2|=k\) | Same, with \(|H|\sim n\) |
| **Thm 19** eqs (22)–(28) | Chebyshev using Var Y from Thm 10 | Automatic once Thm 10 patched |
| **Future research §5** | Confirms \(d^3/n\to d^2/n\) is the intended improvement | — |

## First patch to write in detail

**Proposition (patched single-matching probability).**  
For a fixed perfect matching \(M\) and \(d=o(n^{1/2})\),
\[
\mathbb{P}(M\subset G(n,d))
=
\bigl(1+O(d^2/n)\bigr)
\cdot
\frac{(d)_{1}^{n}}{(dn-1)!!/(dn-n-1)!!}
\cdot(\text{standard configuration main term}),
\]
i.e. the same main term as Gao Thm 10 / Cor 15 with \(\alpha=1\), but error \(O(d^2/n)\).

*Proof sketch.* Apply B Remark 8 with \(H=M\), \(|H|=n/2\). ∎

This single proposition already upgrades the first-moment formula in Thm 10.
Second moment needs the paired-matching case (A ~L736).

## Next writing session

Expand the Proposition into a full proof by copying A’s Cor 15 display for \(\alpha=1\)
and replacing the error term, citing B Theorem 6 / Remark 8 for justification
without re-deriving the main term.
