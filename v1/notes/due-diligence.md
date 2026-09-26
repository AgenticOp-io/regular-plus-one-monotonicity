# Due diligence — originality and the √n barrier

Searched arXiv / published literature (2026-09-22). Key sources:
[Gao21] arXiv:2104.11850, [Gao20] arXiv:2012.01492,
[HLMPW25] arXiv:2505.22875, [BIM25] arXiv:2510.20765,
[GIM] sandwich papers, arXiv:2510.21472.

## 1. Is squeeze past √n possible?

### Up to \(o(\sqrt{n})\) (from \(o(n^{1/3})\))
**Yes — and Gao already said so.**

From [Gao21] introduction / Remark 16:
> “Indeed, it is possible to prove that Theorem 8 holds for all \(d\to\infty\) and
> \(d=o(n^{1/2})\). However, for the sake of a simpler proof, we did not pursue that.”

And Remark 16(b): sharper conditional probs from [Gao20] Thm 6 give Cor 15 with
error \(O(d^2/n)\) instead of \(O(d^3/n)\), improving Thms 8, 10, 19.

So the **statement** of our main theorem was publicly anticipated by Gao.
Our contribution is writing the calculation he deferred — not discovering a new range.

### Past \(\omega(\sqrt{n})\) with this method
**No.**

[Gao20] Remark 8: matching probabilities via Thm 6 have relative error
\(O(d^2|H|/n^2)=O(d^2/n)\) for a perfect matching.
That is \(o(1)\) iff \(d=o(\sqrt{n})\).
Cumulative product-of-conditionals arguments hit the same wall
(our Proposition on the enumeration barrier).

Exact whp +1 for \(d=\omega(\sqrt{n})\) is still open in general
(full Gao–Isaev–McKay monotonicity conjecture). Known pieces use other tools
(HLMPW for sparse/medium; sandwich for large factor gaps; dense increments
\(\omega(n/\log n)\)).

**Verdict:** squeeze *to* \(\sqrt{n}\) is possible (and foreshadowed); squeeze *past*
with the present method is not.

---

## 2. Plagiarism / priority risk

### Would this be plagiarism?
**Not if citations are honest** — and they already are (we attribute Thm 6, Cor 15,
Thm 19, BIM, HLMPW).

Plagiarism = presenting others’ words/ideas as your own without credit.
We credit Gao for the method and the suggested improvement.

### Real risks (more serious than “plagiarism”)

| Risk | Assessment |
|---|---|
| **Overclaiming novelty** | HIGH if we market the main theorem as a breakthrough discovery. Gao announced the range. Frame as: *completion of the proof outlined in [Gao21] Remark 16(b)*. |
| **“Not a paper” referee report** | MEDIUM–HIGH. A short note filling Remark 16 can be publishable, but some venues will say it is too incremental. |
| **Copied proof text** | LOW if we do not paste Gao verbatim. Adaptation with error substitution + citation is normal. |
| **Secondary theorems already known** | Sandwich degree-defect (Thm defect) is an immediate corollary of [BIM25] — do **not** claim originality. TV≤½ at \(d=O(\sqrt{n})\) is a soft packaging of Gao/HLMPW ideas — weak novelty. |
| **Someone already wrote o(√n) nesting** | No arXiv hit found (2026-09-22) beyond Gao’s announcement that it is possible. Search for nesting/perfect-matchings returns essentially only [Gao21]. HLMPW cites Gao for +1 in the \(o(n^{1/3})\) / TV \(n^{1/10}\) regimes, not \(o(\sqrt{n})\). |

### What is safely ours vs not

| Claim | Status |
|---|---|
| Exact +1 for \(d=o(\sqrt{n}/\mathrm{polylog})\) | **Gao’s suggested range**; full writeup not found on arXiv. Publishable as a note *attributed to completing Remark 16(b)*. |
| Patched Cor 15 with \(O(d^2/n)\) | Explicitly described by Gao Remark 16(b); not independently novel. |
| η-schedule / Lemma L4 | Minor technical packaging; not a new idea. |
| Sandwich \(\Delta\)-defect | **Not novel** — cite BIM only. |
| Exact +1 past \(\sqrt{n}\) | Open; not in our paper. |

### Recommended framing for arXiv

Abstract/intro should say something like:

> Gao observed that his \(+1\) nesting theorem extends from \(d=o(n^{1/3})\) to
> \(d=o(n^{1/2})\) using the sharper edge probabilities of [Gao20], but left the
> details for a simpler exposition. We supply those details…

Do **not** say “we prove a long-open strengthening” without that attribution.

---

## Bottom line

1. **Past √n:** not with this toolbox; need a new theorem.
2. **Plagiarism:** unlikely if cited; **priority/novelty** is the real issue — the main result was already signposted by Gao. Submit only as an attributed completion note, or pivot to a genuinely new target.
