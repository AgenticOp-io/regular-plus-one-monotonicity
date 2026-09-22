# Extend vs new theorem — strategic assessment

## Short answer

**Stop extending the present method for exact +1.**  
It is mined out at \(d=o(\sqrt{n}/\mathrm{polylog})\). Further exact range needs a
**new theorem** (or a major addition from outside this coupling/enumeration path).

Polishing the **existing** theorem for arXiv is still worth doing. That is
presentation, not a math extension.

## What the current theorem already is

An execution of Gao’s own Remark 16(b): swap \(O(d^3/n)\to O(d^2/n)\) via
arXiv:2012.01492 Thm 6, replay the Thm 19 coupling.  
Publishable as a short note / addendum-style paper. Not a new conceptual framework.

## What cannot be squeezed further from this path

| Goal | Blocker |
|---|---|
| Exact +1 for \(d=\omega(\sqrt{n})\) | Cumulative matching-prob error \(\Omega(d^2/n)\) |
| Exact +1 for all \(d\) | Same + dense switching barriers |
| Whp nesting at \(d=\Theta(\sqrt{n})\) | Variance term \(d^2/n=\Theta(1)\) kills Chebyshev |

Secondary results (TV ≤ ½, sandwich degree defect) are corollaries, not range extensions.

## What would unlock the next range

These are **new theorems**, not patches:

1. **Quantitative sandwich** — BIM with \(\varepsilon=\varepsilon(n)\to 0\)  
   (ideally \(\varepsilon=\tilde\omega(\sqrt{(\log n)/d})\)).  
   Yields increments of size \(\omega(\sqrt{d\log n})\), not yet +1, but past constant factors.

2. **Process sandwich** (BIM Conjecture 1.3)  
   Strongest form; would essentially optimize defects and thresholds.

3. **Matching-count concentration past \(\sqrt{n}\)**  
   e.g. concentration of \(\log Y\) or permanent methods for dense regular graphs.  
   Would revive Gao’s coupling template in a new window.

4. **Dense +1 by switchings**  
   Direct \(\mathrm{d_{TV}}(G(n,d)\oplus G(n,1),G(n,d+1))=o(1)\) for \(d=\Theta(n)\).

## Recommendation

| Priority | Action |
|---|---|
| Now | Freeze exact-+1 claim; ship arXiv note on \(o(\sqrt{n})\) |
| Next math | Pick **one** new target: quantitative \(\varepsilon(n)\) **or** \(\log Y\) concentration |
| Do not | Keep rewriting η-schedules / Cor 15 errors hoping to beat \(\sqrt{n}\) |

**Bottom line:** format and submit what we have; extend the *program* only by adding a new enabling theorem, not by further tuning this one.
