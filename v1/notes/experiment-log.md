# Experiment log (continued)

## η-schedule at n = 10^60 (`src/config_probes.py`)

| d ~ n^exp | eta_old < 0.1 | eta_new < 0.1 | Meaning |
|----------:|:-------------:|:-------------:|---|
| 0.20 | yes | yes | both OK (deep inside Gao window) |
| 0.30 | **no** | **yes** | **new error unlocks past ~n^{1/3}** |
| 0.33 | **no** | **yes** | same |
| 0.40+ | no | no | need tighter constants / still shy of √n |

This numerically matches the theory: replacing \(d^3/n\) by \(d^2/n\) in \(\eta\) is exactly
what separates the old ceiling from the \(o(\sqrt{n})\) program.

## Config-model greedy probes

At small n, simple-graph acceptance collapses quickly as d grows (as expected).
Among simple samples at (n,d)=(40,3), greedy complement matching succeeded ~97% of the time.
