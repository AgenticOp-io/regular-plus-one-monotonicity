# Non-truncation two-vertex upper

## Solid upgrades

1. **One-vertex upper at Chernoff scale** (`lem:one-vertex-chernoff`):
   G1 is already √(log n/δ); G2 has error 2/δ ≤ λ/log n at this λ.
   BIM's (log n/δ)^{1/4} in Lemma 5.1 was only for uniformity with Thm 6.1.

2. **L² computation** (`rem:second-moment`): for ℓ≥10ℓ₀ one has μ≥n⁹ and
   Var(Y)=O(λ μ²) at λ=√(log n/δ). Relative SD = Θ(√λ)=(log n/δ)^{1/4}.
   Matches Thm U; does **not** reach Hypothesis P.

## Barrier (precise)

| Method | Two-vertex upper error |
|---|---|
| Truncation (Lemma 7.1) | Ω(√λ)=(log n/δ)^{1/4} |
| Second moment / Chebyshev | Θ(√λ)=(log n/δ)^{1/4} |
| Kim–Vu, bounded degree | needs ℓ₀=O(1) i.e. δd≥n^Ω(1) (already have) |

To get error λ=√(log n/δ) need sub-Gaussian / Freedman / high-moment control
with a sharp Lipschitz or predictable-variance proxy (crude edge-exposure
Lipschitz loses a factor n/δ and is useless).

## Still open

Hypothesis P upper half ≡ global rate 1/3 via `thm:quant-third-global`.
