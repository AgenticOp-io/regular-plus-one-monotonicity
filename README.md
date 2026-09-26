# Regular +1 monotonicity

Private AgenticOp-io research repo. Two manuscripts live in this tree.

| Tree | Status | Manuscript |
| --- | --- | --- |
| `v1/` | sent 1.0.0 | exact \(+1\) at every growing degree |
| `v2/` | **active bar** 2.0.0-dev | Chernoff sandwich, peel ID, long factors |

Work program: `v2/notes/PROGRAM.md`. Do not edit v1 except Gao errata.

Do not write v2 theorems into `v1/paper/main.tex`. Do not retitle a v2
conjecture unless `v2/paper/main.tex` has a proof.

## Layout

```
v1/paper/     v1.0 LaTeX (deliverable sent for comment)
v1/notes/     v1.0 workshop
v2/paper/     v2.0 LaTeX (open problems until a proof lands)
v2/notes/     v2.0 workshop
scripts/      Wolfram checker and approach screen (shared)
archive/      chat history
```

## Build

```bash
pdflatex v1/paper/main.tex
pdflatex v2/paper/main.tex
```

MiKTeX on this machine: run `pdflatex` twice from the chosen `paper/` directory.

## Policy

New closed-form identities go through `python scripts/wolfram_check.py`.
For v2 work append to `v2/notes/wolfram-checks.md`.
The Wolfram app id stays in `.wolfram-appid` and is not committed.

The standalone directory `../regular-plus-one-sequel` was the first sequel
copy. Active 2.0 work is `v2/` in this repo.
