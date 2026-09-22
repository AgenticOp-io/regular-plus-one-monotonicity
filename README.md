# README

# Regular +1 Monotonicity

Private research repo (AgenticOp-io): extend
\(G(n,d)\subset G(n,d+1)\) from Gao’s \(d=o(n^{1/3})\) to \(d=o(\sqrt{n})\).

## Current status

| Item | State |
|---|---|
| Easy regime (factor gaps via BIM) | **proved** — `notes/proof-easy-regime.md` |
| Reduction (+1 ⇒ full mono) | **proved** — `notes/proof-reduction.md` |
| Bottleneck diagnosis | done — `notes/bottleneck.md` |
| Lemma L1 (cite Thm 6) | recorded — `notes/lemma-L1-citation.md` |
| Lemma L2 / Thms A–B (patch Cor 15 & moments) | **proved** — `notes/lemma-L2-proof.md` |
| Lemma L4 (η schedule) | **proved** — `notes/attack-n-half.md` |
| Main +1 theorem for \(d=o(\sqrt{n}/\log^3 n)\) | **proved (cond. on Thm 6)** — `notes/main-theorem.md` |
| +1 for all \(d\) / full conjecture | open |

See `notes/STATUS.md` for the live board.

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

Attack **defective +1** for \(n^{1/2}\le d\le n^{2/3}\) (`notes/beyond-sqrt-n.md`).
Optional: compile `paper/main.tex` and submit a note.
