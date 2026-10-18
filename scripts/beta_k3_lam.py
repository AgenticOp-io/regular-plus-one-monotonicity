"""Exact kappa3 residue vs lambda (symbolic a, fixed lam) — star+path."""

from __future__ import annotations

import sympy as sp

from scripts.beta_k3_fraction import k3_coeff, to_frac
from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def k3_delta_at_points(lam_val, Ns=(8, 10, 12)):
    """Exact Fraction aD at several a; fit residue."""
    lam = sp.nsimplify(lam_val)
    pts = []
    for N in Ns:
        a = sp.Rational(1, N)
        print(f"lam={lam} a=1/{N}", flush=True)
        ds = []
        for states, probs in laws(a, lam):
            probs = [sp.nsimplify(p) for p in probs]
            states = [tuple(int(x) for x in s) for s in states]
            m = len(states[0])
            print(f"  m={m}...", flush=True)
            if m == 1:
                ds.append(to_frac(0))
                continue
            sig, kappa = sigma_and_cumulants(states, probs, max_ell=4)
            ds.append(k3_coeff(sig, kappa, m))
        D = ds[2] + ds[0] - 2 * ds[1]
        aD = to_frac(1) / N * D
        print(f"  aD={aD}", flush=True)
        pts.append((a, sp.Rational(aD.numerator, aD.denominator)))
    A = sp.Matrix([[1, a, a**2] for a, _ in pts])
    b = A.solve(sp.Matrix([y for _, y in pts]))
    return b[0], pts


def main() -> None:
    rows = []
    for ln in [sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(1, 2)]:
        # half already known; include for check. For 1/3 may be slow (nz=27).
        res, pts = k3_delta_at_points(ln)
        print(f"lam={ln} residue~{res} = {sp.N(res, 20)}", flush=True)
        rows.append((ln, res))
        cand = -sp.Rational(131, 108) * (1 - ln) / ln
        print(f"  vs -131(1-lam)/(108*lam) = {cand} err={sp.simplify(res-cand)}", flush=True)

    print("done", rows, flush=True)


if __name__ == "__main__":
    main()
