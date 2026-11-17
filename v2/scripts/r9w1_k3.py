"""r9w1: exact 3rd cumulant of S=sum_v (D+rho_v)^2 (host degrees), rho = degrees of X ~ G(H,p), H = complement of D-regular G0.
S = const + w1*|E_X| + 2*P2(X), w1 = 2+4D.  kappa3 = sum_j w1^j 2^(3-j) K_j(p), K_j polynomial in p (exact, integer coeffs).
Term enumeration (connected triples of monomials) + brute-force check over all 2^m subgraphs."""
import itertools, sys
from fractions import Fraction
from collections import defaultdict

def comp_edges(n, E0):
    E0 = {frozenset(e) for e in E0}
    return [e for e in itertools.combinations(range(n), 2) if frozenset(e) not in E0]

def terms(n, H):
    idx = {e: i for i, e in enumerate(H)}
    inc = defaultdict(list)
    for e in H:
        inc[e[0]].append(idx[e]); inc[e[1]].append(idx[e])
    T = [(1 << i, 1) for i in range(len(H))]            # (edge bitmask, type 1=edge term)
    for v in range(n):
        for a, b in itertools.combinations(inc[v], 2):
            T.append(((1 << a) | (1 << b), 0))          # cherry, type 0
    return T

def poly_add(P, k, c): P[k] = P.get(k, 0) + c

def kappa3_poly(n, E0):
    """returns {j: {exp: coeff}} with kappa3 = sum_j w1^j 2^(3-j) * sum coeff p^exp (exact)."""
    H = comp_edges(n, E0); T = terms(n, H); N = len(T)
    pc = lambda x: bin(x).count("1")
    nb = [[] for _ in range(N)]                          # overlap graph
    for i in range(N):
        for j in range(N):
            if i != j and T[i][0] & T[j][0]: nb[i].append(j)
    seen = set(); out = {j: {} for j in range(4)}
    def add(i, j, k):
        key = tuple(sorted((i, j, k)))
        if key in seen: return
        seen.add(key)
        a, b, c = (T[x][0] for x in key); jt = sum(T[x][1] for x in key)
        # mult: ordered triples that are distinct-index sets, plus repeated-index triples handled separately
        mult = 6
        s = lambda m: pc(m)
        # joint cumulant k(A,B,C)= E[ABC]-E[AB]E[C]-E[AC]E[B]-E[BC]E[A]+2E[A]E[B]E[C], E[x_S]=p^|S|
        P = out[jt]
        poly_add(P, s(a|b|c), mult); poly_add(P, s(a|b)+s(c), -mult); poly_add(P, s(a|c)+s(b), -mult)
        poly_add(P, s(b|c)+s(a), -mult); poly_add(P, s(a)+s(b)+s(c), 2*mult)
    def addrep(i, j):   # triples with a repeated index: (i,i,j) ordered count 3 for i!=j ; (i,i,i) count 1
        a, b = T[i][0], T[j][0]; jt = 2*T[i][1] + T[j][1]; P = out[jt]; s = pc
        # k(A,A,B) with A idempotent: A*A=A. E[AAB]=p^|a|b|, E[AA]E[B]=p^|a|+|b|, 2*E[AB]E[A]... use general formula with a,a,b
        for m, (x, y, z) in [(3, (a, a, b))]:
            poly_add(P, s(x|y|z), m); poly_add(P, s(x|y)+s(z), -m); poly_add(P, s(x|z)+s(y), -m)
            poly_add(P, s(y|z)+s(x), -m); poly_add(P, s(x)+s(y)+s(z), 2*m)
    # all-distinct connected triples
    for i in range(N):
        for j in nb[i]:
            for k in set(nb[i]) | set(nb[j]):
                if k != i and k != j: add(i, j, k)
    # (i,i,j): ordered count 3 each for ordered pair (i,j), i!=j overlapping; (i,i,i): single
    for i in range(N):
        for j in nb[i]: addrep(i, j)
        a = T[i][0]; jt = 3*T[i][1]; P = out[jt]; s = pc
        poly_add(P, s(a), 1); poly_add(P, s(a)+s(a), -3); poly_add(P, 3*s(a), 2)
    # (i,i,j) with i,j non-overlapping give cumulant 0: skip (checked in brute)
    return out

def eval_poly(out, w1, p):
    return sum(Fraction(w1)**j * 2**(3-j) * sum(c*Fraction(p)**e for e, c in P.items()) for j, P in out.items())

def brute_k3(n, E0, w1, p):
    H = comp_edges(n, E0); m = len(H); p = Fraction(p)
    tot = defaultdict(Fraction)
    for mask in range(1 << m):
        r = [0]*n; k = 0
        for i, (a, b) in enumerate(H):
            if mask >> i & 1: r[a] += 1; r[b] += 1; k += 1
        P2 = sum(x*(x-1)//2 for x in r)
        tot[w1*k + 2*P2] += p**k*(1-p)**(m-k)
    mu = sum(v*q for v, q in tot.items())
    return sum((v-mu)**3*q for v, q in tot.items())

def counts(n, E0):
    A = [[0]*n for _ in range(n)]
    for a, b in E0: A[a][b] = A[b][a] = 1
    t = sum(1 for a, b, c in itertools.combinations(range(n), 3) if A[a][b] and A[b][c] and A[a][c])
    c4 = 0
    for q in itertools.combinations(range(n), 4):
        for o in [(0,1,2,3),(0,1,3,2),(0,2,1,3)]:
            v = [q[i] for i in o]
            if all(A[v[i]][v[(i+1) % 4]] for i in range(4)): c4 += 1
    return t, c4

if __name__ == "__main__":
    cyc = lambda off, k: [(off+i, off+(i+1) % k) for i in range(k)]
    kk = lambda off, k: [(off+a, off+b) for a in range(k) for b in range(a+1, k)]
    cases = [("C6", 6, cyc(0,6), 1), ("2xK3", 6, cyc(0,3)+cyc(3,3), 1)]
    q3 = [(a, b) for a in range(8) for b in range(a+1, 8) if bin(a ^ b).count("1") == 1]
    cases += [("Q3", 8, q3, 3), ("2xK4", 8, kk(0,4)+kk(4,4), 3)]
    # n=10: G0 = complement of 2-regular H (H cycle types) -> G0 6-regular, brute 2^10
    for name, parts in [("H=C10", [10]), ("H=C5+C5", [5,5]), ("H=C3+C7", [3,7]), ("H=C4+C6", [4,6]), ("H=C3+C3+C4", [3,3,4])]:
        Hs = []; off = 0
        for k in parts: Hs += cyc(off, k); off += k
        G0 = comp_edges(10, Hs); cases.append((name, 10, G0, 6))
    for name, n, E0, D in cases:
        out = kappa3_poly(n, E0)
        for p in [Fraction(3, 10), Fraction(1, 2)]:
            w1 = 2 + 4*D
            a, b = eval_poly(out, w1, p), brute_k3(n, E0, w1, p)
            assert a == b, (name, p, a, b)
        print(name, "t0,c4(G0)=", counts(n, E0), "k3(p=.3,host S) =", float(eval_poly(out, 2+4*D, Fraction(3,10))), "EXACT==BRUTE")
    print("OK")
