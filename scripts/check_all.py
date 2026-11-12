"""Run every check this project relies on; exit nonzero if any fails.

  python scripts/check_all.py          # everything except the slow rate sweep
  python scripts/check_all.py --full   # also rate_inequality.py (delta <= 80, ~15 min)

Steps: exact pairing counts, Laplace limit, cycle effects, Wolfram Alpha
identities (v2/scripts/wolfram_identities.txt, appended to
v2/notes/wolfram-checks.md), and the LaTeX build. A missing Wolfram app id is a
failure, not a skip: all math goes through Wolfram Alpha.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FD = ROOT / "v2" / "scripts" / "fixed_degree_factor"
PAPER = ROOT / "v2" / "paper"
failures = []


def run(name, cmd, cwd=ROOT, ok=lambda out: True):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    out = p.stdout + p.stderr
    good = p.returncode == 0 and ok(out)
    print(("PASS " if good else "FAIL ") + name)
    if not good:
        print(out[-1500:])
        failures.append(name)
    return out


run("exact 1-D formula vs exhaustive pairings",
    [sys.executable, str(FD / "exact_one_dim.py")],
    ok=lambda o: "False" not in o and o.count("True") >= 6)
run("Laplace limit sqrt((D-1)/(D-2)) at n=4000",
    [sys.executable, str(FD / "laplace_limit.py")],
    ok=lambda o: all(abs(float(v)) < 2 for v in re.findall(r"diff\*n=(-?[\d.]+)", o)))
run("cycle effects (-1/(D-1))^k",
    [sys.executable, str(FD / "cycle_effects.py")],
    ok=lambda o: all(abs(float(a) - float(b)) < 1e-5
                     for a, b in re.findall(r"\((-?[\d.]+), (-?[\d.]+)\)", o)))
run("McKay exponent identity (Lemma mckay-exponent)",
    [sys.executable, str(FD / "mckay_exponent.py")],
    ok=lambda o: o.strip().endswith("OK"))
if "--full" in sys.argv:
    run("rate inequality I > psi, D <= 80",
        [sys.executable, str(FD / "rate_inequality.py")],
        ok=lambda o: "VIOLATION" not in o and float(re.search(r"\(([-\d.e]+),", o).group(1)) > 0)

for q in (ROOT / "v2" / "scripts" / "wolfram_identities.txt").read_text().splitlines():
    if "--no-wolfram" in sys.argv:
        print("SKIP wolfram (explicit --no-wolfram; record a sympy fallback in the ledger)")
        break
    if q.strip():
        run("wolfram: " + q[:60],
            [sys.executable, str(ROOT / "scripts" / "wolfram_check.py"),
             "--append", "v2/notes/wolfram-checks.md", q],
            ok=lambda o: "[error]" not in o)

for _ in range(3):
    out = run("pdflatex", ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=PAPER)
log = (PAPER / "main.log").read_text(errors="ignore")
if re.search(r"undefined|may have changed", log):
    print("FAIL latex: undefined references")
    failures.append("latex refs")

print("\nALL CHECKS PASSED" if not failures else f"\n{len(failures)} FAILED: {failures}")
sys.exit(1 if failures else 0)
