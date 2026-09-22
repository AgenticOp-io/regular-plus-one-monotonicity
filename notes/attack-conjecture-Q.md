# Attack log — Conjecture Q (updated)

## Beaten so far

| Rate | How |
|---|---|
| \(1/17\) | first B2 extraction with \(C_0=\Theta(1/\varepsilon)\) |
| **\(1/9\)** | **absolute \(C_0\)** in switching; proved |
| \(1/3\) | Hypothesis P (path counts at switching-optimal \(\eta\)); conditional + process-tight |

## Hard ceiling of BIM process

B2 needs \(\eta=O(\varepsilon)\) at \(R\sim\varepsilon dn\).
Switching needs \(\eta=\Omega(\sqrt{\log n/(\varepsilon d)})\).
⇒ \(\varepsilon=\Omega((\log n/d)^{1/3})\).

**Chernoff \(1/2\) is impossible in this architecture.** Must change the coupling
(process Conjecture 1.3, or defective log-degree upper sandwich, or GIM-style
embedding with sharper \(\xi^3 d\) tails).

## Next to beat \(1/3\)

### A. Prove Hypothesis P (get unconditional \(1/3\))
Re-run BIM §§5–7 with \(\eta=C\sqrt{\log n/\delta}\).
Likely for \(\delta\ge(\log n)^{C}\); check union bounds.

### B. Break the architecture (get toward \(1/2\))
1. **Defective polylog upper sandwich:** allow \(\Delta(G\setminus G^*)\le(\log n)^{O(1)}\)
   instead of perfect containment; Kim–Vu had this for \(d=o(n^{1/3})\).
2. **Process conjecture** BIM 1.3.
3. **Sharper embedding tails** than \(e^{-\Omega(\xi^3 d)}\) in GIM.

### C. Immediate micro-step for P
Extract from BIM Lemma 5.3 / Thm 6.1 the actual relative error in path counts
as a function of \(\delta\), and compare to \(\sqrt{\log n/\delta}\).
