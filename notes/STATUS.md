# Status board

Last update: after Lemma L2 writeup + main theorem assembly.

## Proven in this repo

| Result | File |
|---|---|
| Easy regime (factor gaps via BIM) | `proof-easy-regime.md` |
| Reduction (+1 ⇒ full mono, even n) | `proof-reduction.md` |
| Lemma L4 (η_new schedule) | `attack-n-half.md` |
| Theorem A (patched Cor 15, error \(O(d^2/n)\)) | `lemma-L2-proof.md` |
| Theorem B (patched EY, EY²) | `lemma-L2-proof.md` |
| Main +1 theorem for \(d=o(\sqrt{n}/\log^3 n)\) | `main-theorem.md` |

## Conditional / cited black boxes

| Item | Source |
|---|---|
| Conditional edge probs Thm 6 | Gao arXiv:2012.01492 |
| Coupling template Thm 19 | Gao arXiv:2104.11850 (error substitution only) |
| Second-moment series algebra | Gao §3.4–3.5 (error substitution only) |

## Still open (beyond this paper’s claim)

- +1 for \(d\ge n^{1/2}\)
- Full Gao–Isaev–McKay conjecture
- Process sandwich (BIM Conjecture 1.3)
- Odd \(n\)

## Next polishing (optional, for arXiv quality)

1. Paste Gao §3.4–3.5 expansions into an appendix with \(d^3/n\mapsto d^2/n\).
2. Write out the \(\bar\phi\)-product → \(\varphi(d,\alpha)\) identification without citing Remark 8.
3. Convert `paper/outline.md` into a full LaTeX article.
