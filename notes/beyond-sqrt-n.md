# Beyond \(\sqrt{n}\): barrier and attack sketch

## Why \(\sqrt{n}\) is a wall for the current method

1. **Matching-probability error.**  
   Even with Theorem 6, Remark 8 gives relative error \(O(d^2|H|/n^2)\) for
   \(\mathbb{P}(H\subseteq G)\). For a perfect matching, \(|H|=n/2\), so the error is
   \(O(d^2/n)\), which is \(o(1)\) iff \(d=o(\sqrt{n})\).

2. **Chebyshev + \(\eta\).**  
   The term \(d^2/(n\alpha^2)\) in \(\eta_{\mathrm{new}}\) cannot be killed for
   \(d=\omega(\sqrt{n})\) while keeping \(\alpha\to 0\).

3. **Config-model simplicity.**  
   Contiguity of \(G(n,d)\) to the simple configuration model fails in stronger forms
   as \(d\) grows; switchings become heavier.

So a new idea is required for \(d\ge n^{1/2}\).

## Candidate approaches

### B1 — Defective +1 (near-term publishable)

Prove: for \(d\le n^{1-\delta}\), there is a coupling and a graph \(F\) with
\[
e(F)\le n^{o(1)}
\quad\text{or}\quad
\Delta(F)\le(\log n)^{O(1)}
\]
such that \(\mathbb{P}(G(n,d)\subset G(n,d+1)\cup F)=1-o(1)\).

Kim–Vu historically used defects; a polylog defect through the medium-dense window
would still transfer many monotone properties.

### B2 — BIM sandwich transit with shrinking \(\varepsilon(n)\)

BIM gives factor gaps of size \(\varepsilon d\). If one can take
\(\varepsilon(n)=o(1)\) with \(\varepsilon d\to\infty\) (e.g. \(\varepsilon=(\log n)/d\) when
\(d\gg\log n\)), then
\[
d_2=d_1+\omega(\log n)
\]
becomes available. Not quite +1, but +polylog. Ties to BIM Conjecture 1.3
(process sandwich) for optimal \(\varepsilon\).

### B3 — Switchings in the dense regime

For \(d=\Theta(n)\), use switchings / McKay–Wormald enumeration of dense regular graphs
directly to couple \(G_d\) and \(G_{d+1}\). HLMPW already has
\(\min\{d_1,d_2-d_1\}=\omega(n/\log n)\). Goal: reduce the increment to \(1\).

### B4 — Matching in the complement via permanents / Ryser

Estimate \(Z(G)=\mathrm{per}(J-I-A_G)\) concentration for dense \(A_G\) by modern
permanent techniques (e.g. Barvinok, Schrijver bounds + Lipschitz). If
\(Z/\mathbb{E}Z=1+o(1)\) whp for \(d\le(1-\delta)n\), replay the bipartite coupling
template without needing \(O(d^2/n)\to 0\) from sparse enumeration.

### B5 — Intermediate models (config ↔ matching-unions)

arXiv:2510.21472 couples configuration models and unions of matchings through the
sandwich. Possibly lift +1 along that chain in dense regimes.

## Recommended order

1. **B1 defective +1** for \(n^{1/2}\le d\le n^{2/3}\) — most likely short paper.
2. **B2** quantitative sandwich \(\varepsilon(n)\) — aligns with BIM Conjecture 1.3.
3. **B4** permanent concentration — higher risk/reward for dense +1.

## Immediate lemma for B1

**Conjecture (defective).**  
For \(d\le n^{2/3}\), there is a coupling and a set \(F\) of at most \(n^{1/3}\) edges with
\[
\mathbb{P}\bigl(G(n,d)\subset G(n,d+1)\cup F\bigr)=1-o(1).
\]

Strategy: run Gao’s coupling until the acceptance probabilities deteriorate past
\(\sqrt{n}\); dump the disputed stubs into \(F\).
