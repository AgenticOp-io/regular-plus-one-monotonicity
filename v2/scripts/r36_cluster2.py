"""r36: exact E[x^{|M cap F|} 1{M cap U=0}] (hafnian DP) vs 2nd-order cluster formula
ln Z ~ q1 W1 + (q2-q1^2) W1^2/2 - q2 (Q2/2 + P2), weights w=x-1 on F minus U, -1 on U (incl F cap U).
F = L disjoint PMs, U = j' further disjoint PMs; M uniform PM of K_n."""
import random, math, sys
def rpm(n, rng, forb):
    for _ in range(10000):
        p = list(range(n)); rng.shuffle(p)
        M = {tuple(sorted(p[i:i+2])) for i in range(0, n, 2)}
        if not (M & forb): return M
def haf_ratio(n, w):  # E over uniform PM of prod_{e in M} a_e, a=1+w ; DP over bitmask
    a = [[1.0 + w.get((min(i, j), max(i, j)), 0.0) for j in range(n)] for i in range(n)]
    f = {}
    full = (1 << n) - 1
    def rec(mask):
        if mask == full: return 1.0
        if mask in f: return f[mask]
        i = 0
        while mask >> i & 1: i += 1
        s = 0.0
        for j in range(i + 1, n):
            if not mask >> j & 1 and a[i][j]: s += a[i][j] * rec(mask | 1 << i | 1 << j)
        f[mask] = s; return s
    return rec(0) / math.prod(range(1, n, 2))
def second_order(n, w):
    E = list(w.items()); q1 = 1 / (n - 1); q2 = 1 / ((n - 1) * (n - 3))
    W1 = sum(v for _, v in E); Q2 = sum(v * v for _, v in E)
    s = {}
    for (a, b), v in E: s[a] = s.get(a, 0) + v; s[b] = s.get(b, 0) + v
    sq = {}
    for (a, b), v in E: sq[a] = sq.get(a, 0) + v * v; sq[b] = sq.get(b, 0) + v * v
    P2 = sum((s[v] ** 2 - sq[v]) / 2 for v in s)
    return q1 * W1 + (q2 - q1 ** 2) * W1 ** 2 / 2 - q2 * (Q2 / 2 + P2), q1 * W1
if __name__ == "__main__":
    rng = random.Random(3); x = 2.0
    print("n L jp   exact_lnZ   1st-order err   2nd-order err")
    for n, L, jp in [(12, 2, 2), (14, 2, 2), (16, 2, 3), (16, 3, 3), (18, 3, 3), (20, 3, 3)]:
        F = set(); U = set()
        for _ in range(L): F |= rpm(n, rng, F)
        for _ in range(jp): U |= rpm(n, rng, U)
        w = {e: x - 1 for e in F}
        for e in U: w[e] = -1.0
        ex = math.log(haf_ratio(n, w)); s2, s1 = second_order(n, w)
        print(n, L, jp, round(ex, 5), round(ex - s1, 5), round(ex - s2, 5), "overlap", len(F & U))
