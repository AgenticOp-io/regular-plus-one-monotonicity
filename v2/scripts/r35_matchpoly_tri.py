"""r35: for F = union of L disjoint perfect matchings (L-regular), the k-matching counts
m_k(F) with k<=3 depend on F only through (n,L) and the triangle count Tri(F).
Checks m_2 constant and m_3 = a(n,L) + b*Tri exactly (b integer) over random F."""
import itertools, random, sys
def rand_F(n, L, rng):
    E = set()
    while True:
        E = set(); ok = True
        for _ in range(L):
            for _try in range(200):
                p = list(range(n)); rng.shuffle(p)
                M = {tuple(sorted(p[i:i+2])) for i in range(0, n, 2)}
                if not (M & E): E |= M; break
            else: ok = False; break
        if ok: return E
def counts(E):
    E = sorted(E); m2 = m3 = 0
    adj = {}
    for a, b in E: adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    for (e, f) in itertools.combinations(E, 2):
        if not set(e) & set(f): m2 += 1
    for (e, f, g) in itertools.combinations(E, 3):
        if len(set(e) | set(f) | set(g)) == 6: m3 += 1
    tri = sum(1 for a in adj for b in adj[a] if b > a for c in adj[a] & adj[b] if c > b)
    return m2, m3, tri
rng = random.Random(1); n, L = 24, 4
rows = [counts(rand_F(n, L, rng)) for _ in range(60)]
assert len({r[0] for r in rows}) == 1, "m2 should be constant"
pts = sorted({(r[2], r[1]) for r in rows})
(t0, c0) = pts[0]; slopes = {(c - c0) / (t - t0) for t, c in pts[1:] if t != t0}
print("m2 =", rows[0][0], " (Tri,m3) =", pts, " slopes:", slopes)
assert len(slopes) == 1, "m3 not affine in Tri"
print("OK: m3 = a + b*Tri, b =", slopes.pop())
