"""
worker1_config_split.py -- exact iso-type (non-)flatness of
    a(G0) = E[1/N | G0 subset G(n,p)],   N = #D-regular spanning subgraphs of the host,
which is item (iii) of thm:selection-reduces (the route to conj:config-split).

For each isomorphism type t of D-regular graph on n labelled vertices this computes the
EXACT polynomial
    a_t(p) = sum_k A_k p^k (1-p)^(c-k),   A_k = sum_{S subset comp(G0), |S|=k} 1/N(G0 u S),
with c = C(n,2) - Dn/2, by a subset-sum (zeta) transform over the complement of one
representative G0, in exact rational arithmetic.  Then
    r_t(p) = a_t/abar - 1 = nu_D(t)/mu_D(t) - 1,    TV(p) = (1/2) sum_t mu(t) |r_t|
(abar = mu_D-mean of a;  TV = d_TV(nu_D, mu_D) exactly, see the note).

Usage:  python worker1_config_split.py selfcheck
        python worker1_config_split.py n D [n D ...]
Notes go to v2/notes/worker1_config_split.txt (written by hand from this output).

Replaces the earlier unrun draft, whose 2-factor enumerator was wrong (it produced 715
graphs at n=8 instead of 3507: it only closed cycles in increasing vertex order).
"""
import sys, time, math
from array import array
from fractions import Fraction
from collections import defaultdict
import numpy as np


def all_edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def enum_regular(n, D):
    """All D-regular graphs on n labelled vertices, as edge bitmasks (array of uint64).
    Backtracking: vertex v picks its missing neighbours among later vertices."""
    bit = {e: k for k, e in enumerate(all_edges(n))}
    out = array("Q")
    res = [D] * n
    from itertools import combinations

    def rec(v, mask):
        if v == n:
            out.append(mask)
            return
        r = res[v]
        cand = [u for u in range(v + 1, n) if res[u] > 0]
        if len(cand) < r:
            return
        for nb in combinations(cand, r):
            m = mask
            for u in nb:
                res[u] -= 1
                m |= 1 << bit[(v, u)]
            rec(v + 1, m)
            for u in nb:
                res[u] += 1

    rec(0, 0)
    return np.frombuffer(out, dtype=np.uint64).copy()


def trace_invariants(n, masks):
    """tr A^k, k=3..n, for every graph (exact in float64: entries < 2^53)."""
    E = all_edges(n)
    inv = np.empty((len(masks), n - 2), dtype=np.int64)
    step = 100000
    for s in range(0, len(masks), step):
        m = masks[s:s + step]
        A = np.zeros((len(m), n, n))
        for k, (i, j) in enumerate(E):
            b = ((m >> np.uint64(k)) & np.uint64(1)).astype(np.float64)
            A[:, i, j] = b
            A[:, j, i] = b
        P = A @ A
        for k in range(3, n + 1):
            P = P @ A
            inv[s:s + len(m), k - 3] = np.rint(np.trace(P, axis1=1, axis2=2)).astype(np.int64)
    return inv


def components(n, mask):
    E = all_edges(n)
    adj = [[] for _ in range(n)]
    for k, (i, j) in enumerate(E):
        if mask >> k & 1:
            adj[i].append(j); adj[j].append(i)
    seen = [False] * n
    sizes = []
    for s in range(n):
        if not seen[s]:
            st = [s]; seen[s] = True; c = 0
            while st:
                x = st.pop(); c += 1
                for y in adj[x]:
                    if not seen[y]:
                        seen[y] = True; st.append(y)
            sizes.append(c)
    return tuple(sorted(sizes, reverse=True))


# number of isomorphism classes of d-regular graphs on n vertices (all, incl. disconnected)
KNOWN_CLASSES = {(6, 2): 2, (7, 2): 2, (8, 2): 3, (9, 2): 4, (10, 2): 5, (6, 3): 2,
                 (8, 3): 6, (10, 3): 21, (8, 4): 6, (9, 4): 16}


def classify(n, Dlow, masks):
    """Group Dlow-regular graphs by spectrum (traces).  Returns list of
    (rep_mask, class_size, descriptor).  Guarded by known class counts and by
    class_size | n!  (orbit sizes must divide n!)."""
    inv = trace_invariants(n, masks)
    uniq, first, counts = np.unique(inv, axis=0, return_index=True, return_counts=True)
    assert KNOWN_CLASSES.get((n, Dlow)) == len(uniq), (n, Dlow, len(uniq))
    out = []
    for u, f, c in zip(uniq, first, counts):
        assert math.factorial(n) % int(c) == 0
        t3 = int(u[0]) // 6
        c4 = (int(u[1]) - n * Dlow * (2 * Dlow - 1)) // 8
        out.append((int(masks[f]), int(c), dict(t3=t3, c4=c4, comps=components(n, int(masks[f])))))
    out.sort(key=lambda x: (x[2]["t3"], x[2]["c4"], x[2]["comps"]))
    return out


def zeta(h, c):
    """In-place subset-sum transform over c bits: h[S] <- sum_{T subset S} h[T]."""
    for i in range(c):
        v = h.reshape(-1, 2, 1 << i)
        v[:, 1, :] += v[:, 0, :]
    return h


def popcount(c):
    pc = np.zeros(1 << c, dtype=np.int64)
    for i in range(c):
        pc.reshape(-1, 2, 1 << i)[:, 1, :] += 1
    return pc


def A_coeffs(n, g0, fmasks, low_bits=25):
    """A_k = sum_{|S|=k} 1/N(G0 u S), exact, for S over the complement of G0.
    fmasks: masks of ALL D-regular graphs.  Blocks over the top bits if c > low_bits."""
    nE = n * (n - 1) // 2
    comp = [k for k in range(nE) if not (g0 >> k) & 1]
    c = len(comp)
    idx = np.zeros(len(fmasks), dtype=np.int64)       # F \ G0 in complement coordinates
    for i, k in enumerate(comp):
        idx |= ((fmasks >> np.uint64(k)) & np.uint64(1)).astype(np.int64) << i
    lo = min(c, low_bits)
    hi = c - lo
    low = idx & ((1 << lo) - 1)
    top = idx >> lo
    pc = popcount(lo)
    big = len(fmasks) + 1
    acc = defaultdict(int)                             # (k, N) -> multiplicity
    for T in range(1 << hi):
        sel = low if hi == 0 else low[(top & ~T) == 0]
        h = zeta(np.bincount(sel, minlength=1 << lo).astype(np.int64), lo)
        assert h[0] >= 1 and h.min() >= 1              # G0 itself is always counted
        if big * (lo + 1) <= 5 * 10 ** 7:               # small N range: count without sorting
            cnt = np.bincount(pc * big + h)
            key = np.nonzero(cnt)[0]
            cnt = cnt[key]
        else:
            key, cnt = np.unique(pc * big + h, return_counts=True)
        kT = bin(T).count("1")
        for ky, ct in zip(key.tolist(), cnt.tolist()):
            acc[(ky // big + kT, ky % big)] += ct
    A = [Fraction(0)] * (c + 1)
    for (k, N), ct in acc.items():
        A[k] += Fraction(ct, N)
    assert sum(ct for ct in acc.values()) == 1 << c
    return A


def a_of_p(A, p):
    c = len(A) - 1
    return sum(A[k] * p ** k * (1 - p) ** (c - k) for k in range(c + 1))


def run_case(n, D, ps=None):
    """Returns (types, sizes, Acoeffs).  Types are described via the LOW-degree graph
    (G0 itself if D <= (n-1)/2, else its complement)."""
    t0 = time.time()
    nE = n * (n - 1) // 2
    Dlow = min(D, n - 1 - D)
    low = enum_regular(n, Dlow)
    cls = classify(n, Dlow, low)
    full = np.uint64((1 << nE) - 1)
    fmasks = low if Dlow == D else low ^ full
    flip = (lambda m: m) if Dlow == D else (lambda m: m ^ ((1 << nE) - 1))
    tot = len(low)
    print(f"\n=== n={n} D={D}  |Omega_D|={tot}  types={len(cls)}  "
          f"(types described by the {'graph' if Dlow == D else 'COMPLEMENT (degree %d)' % Dlow})"
          f"  c={nE - D * n // 2} complement edges  [{time.time() - t0:.0f}s]", flush=True)
    from multiprocessing import Pool
    with Pool(min(len(cls), 6)) as pool:                # one type per worker
        As = pool.starmap(A_coeffs, [(n, flip(rep), fmasks) for rep, _, _ in cls])
    for rep, size, desc in cls:
        print(f"  type comps={desc['comps']} t3={desc['t3']} c4={desc['c4']} size={size} "
              f"|Aut|={math.factorial(n) // size}  done [{time.time() - t0:.0f}s]", flush=True)
    if ps is None:
        ps = [("p=1/4", Fraction(1, 4)), ("p=1/2", Fraction(1, 2)), ("p=3/4", Fraction(3, 4))]
        for num, den in ((1, 2), (3, 4), (9, 10)):
            p = Fraction(D * den, (n - 1) * num)        # mean host degree = D / rho
            if p < 1:
                ps.append((f"rho={num}/{den} (p={p})", p))
    for label, p in ps:
        a = [a_of_p(A, p) for A in As]
        abar = sum(Fraction(size, tot) * x for (_, size, _), x in zip(cls, a))
        r = [x / abar - 1 for x in a]
        tv = sum(Fraction(size, tot) * abs(x) for (_, size, _), x in zip(cls, r)) / 2
        pex = tot * p ** (D * n // 2) * abar           # = P(N>=1), prop:target-cn
        print(f"  [{label}]  P(N>=1)={float(pex):.6f}  abar={float(abar):.8e}  "
              f"TV(nu,mu)={float(tv):.6f}  max|r|={float(max(abs(x) for x in r)):.6f}  "
              f"max/min={float(max(a) / min(a)):.6f}")
        for (_, size, desc), x, rr in zip(cls, a, r):
            print(f"      comps={str(desc['comps']):14s} t3={desc['t3']:2d} c4={desc['c4']:2d} "
                  f"mu={size / tot:.5f}  a={float(x):.8e}  r=a/abar-1={float(rr):+.6f}")
    sys.stdout.flush()
    return cls, As


def selfcheck():
    """n=6, D=2 against (a) the values recorded in v2/notes/small-n-inv.md and
    (b) brute force over all 2^15 hosts for P(N>=1) = |Omega| p^6 abar."""
    cls, As = run_case(6, 2, ps=[("p=1/2", Fraction(1, 2))])
    by = {c[2]["comps"]: a_of_p(A, Fraction(1, 2)) for c, A in zip(cls, As)}
    assert abs(float(by[(6,)]) - 0.29623897) < 1e-8 and abs(float(by[(3, 3)]) - 0.25733183) < 1e-8
    fm = [int(x) for x in enum_regular(6, 2)]
    assert len(fm) == 70 and len(enum_regular(8, 2)) == 3507 and len(enum_regular(8, 3)) == 19355
    alive = sum(1 for H in range(1 << 15) if any(f & H == f for f in fm))
    abar = Fraction(60, 70) * by[(6,)] + Fraction(10, 70) * by[(3, 3)]
    assert Fraction(alive, 1 << 15) == 70 * Fraction(1, 2) ** 6 * abar
    # Normalized (iii'): d nu_D / d mu_D = a/abar and TV = (1/2) E_mu|a/abar - 1|, checked
    # against nu_D computed straight from its definition over all 2^15 hosts, two values of p.
    typ = [components(6, f) for f in fm]
    for p in (Fraction(1, 2), Fraction(1, 3)):
        nu = defaultdict(Fraction)
        for H in range(1 << 15):
            inside = [t for f, t in zip(fm, typ) if f & H == f]
            if inside:
                w = p ** bin(H).count("1") * (1 - p) ** (15 - bin(H).count("1")) / len(inside)
                for t in inside:
                    nu[t] += w
        Z = sum(nu.values())                                 # = P(N>=1)
        a = {c[2]["comps"]: a_of_p(A, p) for c, A in zip(cls, As)}
        mu = {c[2]["comps"]: Fraction(c[1], 70) for c in cls}
        ab = sum(mu[t] * a[t] for t in mu)
        assert all(nu[t] / Z == mu[t] * a[t] / ab for t in mu)
        tv = sum(abs(nu[t] / Z - mu[t]) for t in mu) / 2
        assert tv == sum(mu[t] * abs(a[t] / ab - 1) for t in mu) / 2
    print("selfcheck OK: n=6 values match small-n-inv.md; P(N>=1) identity exact;"
          " nu/mu = a/abar and TV identity exact at p=1/2,1/3; |Omega| = 70, 3507, 19355.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "selfcheck":
        selfcheck()
    else:
        for i in range(0, len(args), 2):
            run_case(int(args[i]), int(args[i + 1]))
