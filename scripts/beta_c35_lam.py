"""Exact C35 residue as a function of lambda (symbolic a, fixed lam)."""

from __future__ import annotations

import sympy as sp

from scripts.beta_c35_exact import cov_x_phi5_exact
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def c35_delta_symbolic(lam_val):
    """Return Delta d^{(3,5)}(a) as a sympy expr in a, at fixed lam."""
    a = sp.symbols("a", positive=True)
    lam = sp.nsimplify(lam_val)
    ds = []
    for idx, (states, probs) in enumerate(laws(a, lam)):
        print(f"  m={idx+1}...", flush=True)
        probs = [sp.simplify(p) for p in probs]
        states = [tuple(int(x) for x in s) for s in states]
        sig, kappa = sigma_and_cumulants(states, probs, max_ell=5)
        m = len(states[0])
        if m == 1:
            ds.append(sp.Integer(0))
        else:
            d = cov_x_phi5_exact(sig, kappa, m)
            ds.append(d)
            print(f"    d={d}", flush=True)
    D = sp.simplify(ds[2] + ds[0] - 2 * ds[1])
    return a, D


def main() -> None:
    residues = []
    for ln in [
        sp.Rational(1, 3),
        sp.Rational(2, 5),
        sp.Rational(1, 2),
        sp.Rational(3, 5),
        sp.Rational(2, 3),
    ]:
        print(f"lam={ln}", flush=True)
        a, D = c35_delta_symbolic(ln)
        print(f"  D={D}", flush=True)
        ser = D.series(a, 0, 2)
        print(f"  series={ser}", flush=True)
        res = sp.limit(a * D, a, 0)
        print(f"  residue={res}", flush=True)
        residues.append((ln, res))

    print("residues:", residues, flush=True)
    # Guess form: try fit c*(1-lam)/lam^k or similar
    lam = sp.symbols("lam", positive=True)
    # interpolate residue as rational in lam
    pts = residues
    # try degree-2 over degree-2
    print("vs (1-lam)/(2*lam):", [(ln, r - (1 - ln) / (2 * ln)) for ln, r in pts], flush=True)
    print("vs 5/(3*lam):", [(ln, r - 5 / (3 * ln)) for ln, r in pts], flush=True)
    print("vs 5*(1-lam)/(3*lam):", [(ln, r - 5 * (1 - ln) / (3 * ln)) for ln, r in pts], flush=True)
    print("vs (1-lam)^2/(lam^2):", [(ln, r - (1 - ln) ** 2 / ln**2) for ln, r in pts], flush=True)


if __name__ == "__main__":
    main()
