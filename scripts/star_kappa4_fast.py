"""Fast numeric star contribution to kappa_4(X)/24 second difference."""
from __future__ import annotations

import itertools
import time

import numpy as np
import sympy as sp

from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants, _matchings


def star_coeff(a_val, lam_val, m_idx: int) -> float:
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    states, probs = laws(a, lam)[m_idx]
    sig, kappa = sigma_and_cumulants(
        states, [sp.nsimplify(p) for p in probs], max_ell=3
    )
    S = np.asarray(sig.inv().tolist(), dtype=np.float64)
    m = S.shape[0]
    k3 = np.zeros((m, m, m), dtype=np.float64)
    for t in itertools.product(range(m), repeat=3):
        k3[t] = float(kappa[t])

    # Precompute all nonzero k3 flat entries
    ts = [t for t in itertools.product(range(m), repeat=3) if k3[t] != 0.0]
    kt = np.array([k3[t] for t in ts])
    nt = len(ts)
    # colour indices array (nt, 3)
    cols = np.array(ts, dtype=np.int8)

    g0, g = 2.0, 1.0
    pairings12 = list(_matchings(12))
    pairings6 = list(_matchings(6))

    # Build cov colour lookup: for each pairing, contribution is product of S[c_i,c_j]*g
    # Iterate t-quadruples
    E4 = 0.0
    for i1 in range(nt):
        for i2 in range(nt):
            for i3 in range(nt):
                for i4 in range(nt):
                    base = kt[i1] * kt[i2] * kt[i3] * kt[i4]
                    idxs = np.concatenate([cols[i1], cols[i2], cols[i3], cols[i4]])
                    wsum = 0.0
                    for pairing in pairings12:
                        pt = 1.0
                        for ia, ib in pairing:
                            ra, rb = ia // 3, ib // 3
                            pt *= (g0 if ra == rb else g) * S[idxs[ia], idxs[ib]]
                        wsum += pt
                    E4 += base * wsum

    E2 = 0.0
    for i1 in range(nt):
        for i2 in range(nt):
            base = kt[i1] * kt[i2]
            idxs = np.concatenate([cols[i1], cols[i2]])
            wsum = 0.0
            for pairing in pairings6:
                pt = 1.0
                for ia, ib in pairing:
                    ra, rb = ia // 3, ib // 3
                    pt *= (g0 if ra == rb else g) * S[idxs[ia], idxs[ib]]
                wsum += pt
            E2 += base * wsum

    return (E4 - 3.0 * E2 * E2) / 31104.0


def main():
    lam = 0.5
    for av in [0.25, 0.2, 0.15, 0.1]:
        t0 = time.time()
        c2 = star_coeff(av, lam, 1)
        t1 = time.time()
        print(f"a={av} m2={c2:.8f} ({t1-t0:.1f}s)", flush=True)
        c3 = star_coeff(av, lam, 2)
        t2 = time.time()
        print(f"a={av} m3={c3:.8f} ({t2-t1:.1f}s) D={c3-2*c2:.8f}", flush=True)


if __name__ == "__main__":
    main()
