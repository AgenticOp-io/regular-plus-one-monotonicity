# Past \(1/3\): corrected architecture

## Hard barriers (proved accounting)

| Engine | Binding constraint | Ceiling |
|---|---|---|
| BIM upper B2 + switching | \(\eta=O(\varepsilon)\) and \(\eta=\Omega(\sqrt{\log n/(\varepsilon d)})\) | \(\varepsilon=\Omega((\log n/d)^{1/3})\) |
| BIM lower + residual degree conc. | \(\eta\ll\varepsilon\) and \(\eta=\Omega(\sqrt{\log n/(\varepsilon d)})\) | \(\varepsilon=\Omega((\log n/d)^{1/3})\) |
| GIM Thm 2.6 structure | \(\xi\Delta\gg n/\log n\) | \(\xi=\omega(n/(d\log n))\); **incompatible with Chernoff for all \(d<n\)** |
| GIM degree tails alone | \(e^{-\Omega(\xi^4\Delta)}\) (loose) or \(\xi^2d\) (Chernoff) | upgrading tails does **not** remove the structural block |

So Conjecture Q needs BIM process Conjecture 1.3, or a coupling outside deletion/addition+B2.

## Dead ends recorded

- **GIM Freedman / \(\xi^2d\) tails:** structural hypothesis \(\xi d\gg n/\log n\) forces \(\xi\gg n/(d\log n)\). Chernoff \(\sqrt{(\log n)/d}\) never meets this (\(d\gg n^2/\mathrm{polylog}\) impossible).
- **B2 residual as “defect”:** with switching-optimal \(\eta\), residual average degree \(\asymp\sqrt{d\log n/\varepsilon}\). At Chernoff this is \(\asymp d^{3/4}\mathrm{polylog}\), **worse** than perfect \(1/3\)-sandwich defect \(d^{2/3}\).

## Live architectures

### A. Process conjecture ⇒ Chernoff (proved implication)
BIM Conjecture 1.3 + ordinary ER degree Chernoff ⇒ Conjecture Q.
(Written as Theorem in `paper/main.tex`.)

### B. Window reduction (proved reduction)
For \(d\ge n^{\sigma}\), Conjecture Q ⇔ final-window coupling from
\(\varepsilon=(log n/d)^{1/3}\) down to Chernoff \(\sqrt{(\log n)/d}\).
The hard surplus-degree range is only
\[
\sqrt{d\log n}\;\le\;\delta\;\le\;d^{2/3}(\log n)^{1/3}.
\]
(Written as Theorem in `paper/main.tex`.)

### C. Attack the final window
Under the BIM coupling at rate \(1/3\), study the residual
\(R=G^*_0\setminus G\) (degree \(\asymp d^{2/3}\)) and thin it to surplus
\(\asymp\sqrt{d\log n}\) without exposing edges of \(G\).

## Recommended next build
Prove a **one-sided final-window lemma**: given \(G\subset G^*_0\sim G(n,(1+\varepsilon_0)d/n)\) from the \(1/3\)-sandwich, construct \(H\sim G(n,(1+\varepsilon_C)d/n)\) with \(G\subset H\) by dependent thinning of \(G^*_0\setminus G\).
