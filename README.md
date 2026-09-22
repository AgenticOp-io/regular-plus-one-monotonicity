# README

# Regular +1 Monotonicity

Private AgenticOp-io research repo: nest \(G(n,d)\subset G(n,d+1)\).

## Main results

1. **Exact +1** for \(d=o(\sqrt{n}/\log^3 n)\) (assumes Gao arXiv:2012.01492 Thm 6).
2. **Always-nested coupling** with \(\mathrm{d_{TV}}\le 1/2\) for \(d\le c\sqrt{n}\).
3. **Degree-defect** \(\Delta(G\setminus H)=O(\varepsilon d)\) for all \(d\ge C\log n\) via sandwich.

See `notes/strongest-theorems.md` and `paper/main.tex`.

## Layout

```
notes/     proofs and status
src/       experiments
paper/     LaTeX draft
```

## Run

```bash
python src/experiments.py
python src/config_probes.py
```

## Policy

Math deliverables are arXiv-formatted in `paper/main.tex`
(see `.cursor/rules/arxiv-format.mdc`).

Strategic note: the exact-+1 method is complete through \(o(\sqrt{n})\); further
range needs a **new** enabling theorem (`notes/extend-vs-new.md`).
