"""MC estimate of Delta Re log E[e^Phi] via sample cumulants of Phi."""

from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp

from scripts.multicolour_constant import laws
from scripts.next_order_sparse import sigma_and_cumulants


def build(a_val, lam_val, m_idx, max_ell=6):
    a = sp.nsimplify(a_val)
    lam = sp.nsimplify(lam_val)
    states, probs = laws(a, lam)[m_idx]
    states = [tuple(int(x) for x in s) for s in states]
    probs = [sp.nsimplify(p) for p in probs]
    sig, kappa = sigma_and_cumulants(states, probs, max_ell=max_ell)
    m = len(states[0])
    S = np.array([[float(sig.inv()[i, j]) for j in range(m)] for i in range(m)])
    karr = {}
    for ell in range(3, max_ell + 1):
        arr = np.zeros((m,) * ell)
        for t in itertools.product(range(m), repeat=ell):
            arr[t] = float(kappa[t])
        karr[ell] = arr
    return S, karr, m


def phi_samples(S, karr, m, n, trials, seed, max_ell=6):
    rng = np.random.default_rng(seed)
    G = rng.multivariate_normal(np.zeros(m), S / (n - 2), size=(trials, n))
    Gb = G.mean(axis=1, keepdims=True)
    Th = G - Gb * (n / (2 * n - 2))
    # u_jk for all pairs: use broadcasting — memory heavy; loop trials
    out = np.zeros(trials, dtype=np.complex128)
    fac = {ell: (1j) ** ell / math.factorial(ell) for ell in range(3, max_ell + 1)}
    for t in range(trials):
        th = Th[t]
        acc = 0j
        for j in range(n):
            for k in range(j + 1, n):
                u = th[j] + th[k]
                for ell in range(3, max_ell + 1):
                    ka = karr[ell]
                    if ell == 3:
                        val = np.einsum("abc,a,b,c", ka, u, u, u)
                    elif ell == 4:
                        val = np.einsum("abcd,a,b,c,d", ka, u, u, u, u)
                    elif ell == 5:
                        val = np.einsum("abcde,a,b,c,d,e", ka, u, u, u, u, u)
                    else:
                        val = np.einsum("abcdef,a,b,c,d,e,f", ka, u, u, u, u, u, u)
                    acc += fac[ell] * val
        out[t] = acc
    return out


def reh_from_samples(phi, order=4):
    """Re of sum_{r<=order} kappa_r(Phi)/r! via real/imag joint cumulants (low order)."""
    X, Y = phi.real, phi.imag
    # center
    Xc, Yc = X - X.mean(), Y - Y.mean()
    # kappa1
    reh = float(X.mean())
    # kappa2/2 of complex Z=X+iY: Re(kappa2(Z)/2) = (VarX - VarY)/2
    reh += 0.5 * (float(np.mean(Xc**2)) - float(np.mean(Yc**2)))
    if order >= 3:
        # kappa3(Z)/6: Z^3 = (X+iY)^3; Re part of E[Z^3]/6 (centered)
        Zc = Xc + 1j * Yc
        reh += float(np.real(np.mean(Zc**3)) / 6)
    if order >= 4:
        # kappa4(Z)/24 ≈ (E[Z^4] - 3 E[Z^2]^2)/24
        m2 = np.mean(Zc**2)
        m4 = np.mean(Zc**4)
        k4 = m4 - 3 * m2 * m2
        reh += float(np.real(k4) / 24)
    return reh


def main():
    n = 30
    trials = 800
    print(f"n={n} trials={trials}", flush=True)
    for an in [0.25, 0.2, 0.15]:
        rehs = []
        for mi in [0, 1, 2]:
            print(f"  sampling a={an} m={mi+1}...", flush=True)
            S, karr, m = build(an, 0.5, mi, max_ell=6)
            phi = phi_samples(S, karr, m, n, trials, seed=10 + mi + int(an * 100))
            reh = reh_from_samples(phi, order=4)
            rehs.append(reh)
            print(f"    Reh≈{reh:.6f}", flush=True)
        D = rehs[2] + rehs[0] - 2 * rehs[1]
        print(
            f"a={an} Delta={D:.6f} n*Delta={n*D:.4f} n*a*Delta={n*an*D:.4f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
