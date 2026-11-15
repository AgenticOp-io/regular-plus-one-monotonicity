"""
r2_worker1_tv.py -- round 2, worker 1: does d_TV(nu_D, mu_D) -> 0, and how fast?
Notes: v2/notes/r2_worker1_tv.txt.

nu_D = law of a uniform D-factor of the host, conditioned on N >= 1;  mu_D = uniform D-regular.
Everything is computed per LABELLED graph, so no isomorphism classification enters a TV value.
Float64 sums of <= 2^21 positive terms (relative error ~1e-12); the identities are asserted.

Part G (host G(n,p), brute force over all 2^C(n,2) hosts, n in {6,7}):
  checks the planting/kernel bound of the notes (Lemma 1 + Theorem 2):
     TV(nu, mu) <= sum_{d*} w(d*) [ E_{d*}|N/E_{d*}N - 1| + TV(mu'_{d*}, mu) ],
  where d* = host degree sequence, w(d*) = P(deg = d*, N>=1)/P(N>=1), E_{d*} = uniform host with
  degrees d*, mu'_{d*}(G0) ∝ #{H : deg H = d*, H ⊇ G0}; the exact identity
     sum_{d*} P_planted(d*) mu'_{d*} = mu;
  and the size of the UNconditioned bound E|N/EN - 1| (Prop 3: it -> 2, the planted host is too dense).
Part R (host uniform h-regular, n=8): the regular-host model of Theorem 4.  Prints TV(nu, mu),
  the split TV(nu, mu') and TV(mu', mu), the bound E|Z/EZ - 1|, and the per-triangle factor of
  nu/mu against the small-subgraph-conditioning prediction 1/(1 - (h-1)^-3).

Usage:  python r2_worker1_tv.py          # both parts, ~1-2 min
"""
import numpy as np
from worker1_config_split import all_edges, enum_regular, trace_invariants


def bits(n):
    E = all_edges(n)
    return E, [np.uint64(1 << k) for k in range(len(E))]


def tv(a, b):
    return 0.5 * float(np.abs(a - b).sum())


def cycle_fit(n, D, F, r_mu, r_mup):
    """Group labelled factors by spectrum (t3, c4 from tr A^3, tr A^4); print per-class nu/mu and
    nu/mu', and the least-squares fit log(nu/mu') = a + b t3 + c c4 (mu-weighted over classes)."""
    inv = trace_invariants(n, F)
    uniq, lab, cnt = np.unique(inv, axis=0, return_inverse=True, return_counts=True)
    lab = lab.ravel()
    rows = []
    for g in range(len(uniq)):
        m = lab == g
        assert np.ptp(r_mu[m]) < 1e-9 and np.ptp(r_mup[m]) < 1e-9   # nu, mu' are S_n-invariant
        t3 = int(uniq[g][0]) // 6
        c4 = (int(uniq[g][1]) - n * D * (2 * D - 1)) // 8
        rows.append((t3, c4, cnt[g], float(r_mu[m][0]), float(r_mup[m][0])))
    rows.sort()
    X = np.array([[1, t, c] for t, c, *_ in rows], float)
    y = np.log([r for *_, r in rows])
    sw = np.sqrt([k for _, _, k, _, _ in rows])
    coef = np.linalg.lstsq(X * sw[:, None], y * sw, rcond=None)[0]
    return rows, np.exp(coef[1]), np.exp(coef[2])


def gnp_part(n, D, p):
    E, B = bits(n)
    c = len(E)
    H = np.arange(1 << c, dtype=np.uint64)
    F = enum_regular(n, D)
    deg = np.zeros((n, len(H)), dtype=np.int64)
    for k, (i, j) in enumerate(E):
        b = ((H >> np.uint64(k)) & np.uint64(1)).astype(np.int64)
        deg[i] += b; deg[j] += b
    e = deg.sum(0) // 2
    wt = p ** e * (1 - p) ** (c - e)
    key = np.zeros(len(H), dtype=np.int64)
    for v in range(n):
        key = key * n + deg[v]
    _, lab = np.unique(key, return_inverse=True)
    lab = lab.ravel(); G = lab.max() + 1

    N = np.zeros(len(H))
    for f in F:
        N += (H & f) == f
    pos = N > 0
    PN = wt[pos].sum()
    invN = np.where(pos, 1 / np.maximum(N, 1), 0.0)
    nu = np.empty(len(F))
    cnt = np.empty((len(F), G))              # cnt[f, d*] = #{H with degrees d*, H ⊇ f}
    for a, f in enumerate(F):
        m = (H & f) == f
        nu[a] = (wt[m] * invN[m]).sum() / PN
        cnt[a] = np.bincount(lab[m], minlength=G)
    mu = np.full(len(F), 1 / len(F))
    assert abs(nu.sum() - 1) < 1e-12

    # unconditioned planting bound
    EN = (wt * N).sum()
    unc = (wt * np.abs(N / EN - 1)).sum()
    # degree-conditioned bound (hosts with the same d* have the same weight)
    size = np.bincount(lab, minlength=G).astype(float)
    meanN = np.bincount(lab, weights=N, minlength=G) / size
    Zdev = np.bincount(lab, weights=np.abs(N / np.maximum(meanN[lab], 1e-300) - 1) * (meanN[lab] > 0),
                       minlength=G) / size
    Zdev[meanN == 0] = 0                       # w(d*) = 0 there anyway
    w = np.bincount(lab, weights=wt * pos, minlength=G) / PN
    colsum = cnt.sum(0)
    mup = cnt / np.where(colsum > 0, colsum, 1)
    tvmup = 0.5 * np.abs(mup - mu[:, None]).sum(0)
    termA = float((w * Zdev).sum()); termB = float((w * tvmup).sum())
    lhs = tv(nu, mu)
    assert lhs <= termA + termB + 1e-12
    # exact identity: planted degree law mixes mu' back to mu
    Ppl = np.bincount(lab, weights=wt * N, minlength=G) / EN
    assert np.allclose(mup @ Ppl, mu, atol=1e-13)
    print(f"G(n,p) n={n} D={D} p={p:.4f}: TV(nu,mu)={lhs:.6f}  bound={termA + termB:.6f}"
          f" [A: E|Z-1|={termA:.6f}, B: TV(mu',mu)={termB:.6f}]  unconditioned E|N/EN-1|={unc:.4f}"
          f"  P(N>=1)={PN:.4f}")


def reg_part(n, h, D):
    F = enum_regular(n, D)
    H = enum_regular(n, h)
    N = np.zeros(len(H))
    for f in F:
        N += (H & f) == f
    assert N.min() > 0 or D == 0
    invN = 1 / N
    nu = np.empty(len(F)); W = np.empty(len(F))
    for a, f in enumerate(F):
        m = (H & f) == f
        nu[a] = invN[m].sum() / len(H)
        W[a] = m.sum()
    mu = np.full(len(F), 1 / len(F))
    mup = W / W.sum()
    assert abs(nu.sum() - 1) < 1e-12
    bound = float(np.abs(N / N.mean() - 1).mean())
    t_num, t_a, t_b = tv(nu, mu), tv(nu, mup), tv(mup, mu)
    assert t_a <= bound + 1e-12
    rows, th3, th4 = cycle_fit(n, D, F, nu / mu, nu / mup)
    x = 1 / (h - 1)
    print(f"reg-host n={n} h={h} D={D}: #H={len(H)} #F={len(F)}  TV(nu,mu)={t_num:.6f}"
          f"  TV(nu,mu')={t_a:.6f} <= E|Z-1|={bound:.6f}  TV(mu',mu)={t_b:.6f}")
    print(f"      fit nu/mu' ~ th3^t3 th4^c4: th3={th3:.4f} (SSC {1 / (1 - x ** 3):.4f}),"
          f" th4={th4:.4f} (SSC {1 / (1 + x ** 4):.4f})")
    for t, c, k, r1, r2 in rows:
        print(f"      t3={t:2d} c4={c:2d} #={k:6d}  nu/mu={r1:.6f}  nu/mu'={r2:.6f}")


if __name__ == "__main__":
    for n, D, p in [(6, 2, 0.5), (6, 2, 1 / 3), (6, 3, 0.5), (6, 3, 0.75), (7, 2, 0.5), (7, 2, 2 / (0.75 * 6))]:
        gnp_part(n, D, p)
    for h, D in [(3, 2), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3), (5, 4), (6, 4)]:
        reg_part(8, h, D)
