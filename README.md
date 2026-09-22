# Regular +1 Monotonicity

Attack on the Gao–Isaev–McKay monotonicity conjecture for random regular graphs:
couple \(G(n,d)\subset G(n,d+1)\) with high probability.

## Goal

**Conjecture (critical case).** For even \(n\) and \(3\le d\le n-3\) with \(dn\) even,
there exists a coupling of \(G\sim G(n,d)\) and \(H\sim G(n,d+1)\) such that
\(\mathbb{P}(G\subset H)=1-o(1)\).

## Status

| Piece | Status |
|---|---|
| Regime map of known results | `notes/regime-map.md` |
| Easy regime (constant-factor degree gap) via Kim–Vu sandwich | **proved in-repo** — `notes/proof-easy-regime.md` |
| Reduction: full monotonicity ⇐ iterated +1 | **proved in-repo** — `notes/proof-reduction.md` |
| +1 via matching extension / TV distance | **in progress** — `notes/proof-plus-one-attack.md` |
| Small-n experiments | `src/experiments.py` |

## References

1. Kim–Vu (2004), Sandwiching random graphs.
2. Gao–Isaev–McKay, sandwich papers + monotonicity conjecture.
3. Behague–Ilʼkovič–Montgomery (2025), full Kim–Vu proof [arXiv:2510.20765].
4. Hollom–Lichev–Mond–Portier–Wang (2025), monotonicity and decompositions [arXiv:2505.22875].

## Working rule

Never claim a regime is new unless it is absent from the regime map.
Prefer defective / approximate statements before exact inclusion.
