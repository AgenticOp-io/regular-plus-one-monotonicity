# README

# Regular +1 Monotonicity

Private research repo (AgenticOp-io): extend
\(G(n,d)\subset G(n,d+1)\) from Gao’s \(d=o(n^{1/3})\) to \(d=o(\sqrt{n})\).

## Current status

| Item | State |
|---|---|
| Easy regime (factor gaps via BIM) | proved — `notes/proof-easy-regime.md` |
| Reduction (+1 ⇒ full mono) | proved — `notes/proof-reduction.md` |
| Bottleneck diagnosis | done — `notes/bottleneck.md` |
| Attack plan to \(o(\sqrt{n})\) | **active** — `notes/attack-n-half.md` |
| Lemma L1 (cite Thm 6) | recorded — `notes/lemma-L1-citation.md` |
| Lemma L2 (patch Gao Thm 10) | draft — `notes/lemma-L2-draft.md` |
| Lemma L4 (η schedule) | proved (conditional on η form) |
| Full +1 for \(d=o(\sqrt{n})\) | **open** (needs L2) |

## Layout

```
notes/     mathematical writeups
src/       small-n and schedule experiments
paper/     paper outline
```

## Run experiments

```bash
python src/experiments.py
python src/config_probes.py
```

## Next concrete step

Line-by-line diff of Gao arXiv:2104.11850 Theorem 10 against
arXiv:2012.01492 Theorem 6 → finish Lemma L2.
