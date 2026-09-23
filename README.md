# README

# Regular +1 Monotonicity

Private AgenticOp-io research repo: nest \(G(n,d)\subset G(n,d+1)\).

## Main results

1. **Exact +1** for \(d=o(\sqrt{n})\) (assumes Gao arXiv:2012.01492 Thm 6).
2. **Always-nested coupling** with \(\mathrm{d_{TV}}\le 1/2\) for \(d\le c\sqrt{n}\).
3. **Degree-defect** \(\Delta(G\setminus H)=O(\varepsilon d)\) for all \(d\ge C\log n\) via sandwich.

See `notes/strongest-theorems.md` and `paper/main.tex`.

## Layout

```
notes/     proofs and status
src/       experiments
paper/     LaTeX draft
archive/   research chat history (chat-history.md) and encrypted transcript
```

## Run

```bash
python src/experiments.py
python src/config_probes.py
```

## Policy

Math deliverables are arXiv-formatted in `paper/main.tex`
(see `.cursor/rules/arxiv-format.mdc`).
Before a proof is finalized, each new identity is checked with
`python scripts/wolfram_check.py` (see `.cursor/rules/verify-math.mdc`).
The Wolfram app id stays in `.wolfram-appid` and is not committed.

Strategic note: the exact-+1 method is complete through \(o(\sqrt{n})\); further
range needs a **new** enabling theorem (`notes/extend-vs-new.md`).
