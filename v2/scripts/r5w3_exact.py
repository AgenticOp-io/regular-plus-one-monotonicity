# Exact P(uv in G | H1 in G) for random D-regular G on n vertices (degree-sequence DP + inclusion-exclusion),
# vs Gao Thm6 principal term in product form (1-A)(1-B) and exp form exp(-A-B).
import itertools, sys
from functools import lru_cache
from math import comb, exp

def make(D):
    @lru_cache(None)
    def N(c):  # c[j-1]=#vertices with residual degree j; number of labelled graphs
        if not any(c): return 1
        k=max(j for j in range(1,D+1) if c[j-1]); c=list(c); c[k-1]-=1
        tot=0
        def rec(j,left,cur,w):
            nonlocal tot
            if j==0:
                if left==0: tot+=w*N(tuple(cur))
                return
            for a in range(min(left,c[j-1])+1):
                new=list(cur); new[j-1]-=a
                if j>=2: new[j-2]+=a
                rec(j-1,left-a,new,w*comb(c[j-1],a))
        rec(D,k,c,1)
        return tot
    return N

def Nseq(N,D,deg):
    if any(x<0 for x in deg): return 0
    c=[0]*D
    for x in deg:
        if x>D: return 0
        if x: c[x-1]+=1
    return N(tuple(c))

def contains(N,n,D,S):
    # #D-regular graphs containing S = #graphs of degree dt=D-deg_S avoiding S;
    # f(d,S) = sum_{T<=S} (-1)^|T| f(d-deg_T, T)  (graphs containing T = graphs of residual degree avoiding T)
    S=tuple(sorted(S)); d=[D]*n
    for a,b in S: d[a]-=1; d[b]-=1
    memo={}
    def f(d,S):
        if any(x<0 for x in d): return 0
        if not S: return Nseq(N,D,d)
        key=(d,S)
        if key in memo: return memo[key]
        tot=0
        for r in range(len(S)+1):
            for T in itertools.combinations(S,r):
                e=list(d)
                for a,b in T: e[a]-=1; e[b]-=1
                tot+=(-1)**r*f(tuple(e),T)
        memo[key]=tot
        return tot
    return f(tuple(d),S)

def gao(n,D,H,u,v):
    dt=[D]*n
    for a,b in H: dt[a]-=1; dt[b]-=1
    Hs={frozenset(e) for e in H}
    nb=lambda x:[y for y in range(n) if frozenset((x,y)) in Hs]
    M=sum(dt); M2=sum(x*(x-1) for x in dt)
    W=0
    for a,b in H:
        for x,y in ((a,b),(b,a)):
            if len({x,y}&{u,v})==0 and frozenset((x,u)) not in Hs and frozenset((y,v)) not in Hs:
                W+=dt[x]*dt[y]
    A=M2**2/M**3+M2/M**2+W/M**2
    phi=-2*(dt[u]+dt[v])+2-sum(dt[x] for x in nb(u))-sum(dt[y] for y in nb(v))-(dt[u]+dt[v]-2)*M2/M+dt[u]*dt[v]
    B=phi/M
    return dt[u]*dt[v]/M,A,B

FAM={ # name -> (edges, u, v) ; vertices 0..; u,v distinct from edges' use allowed
 'empty':([],0,1),
 'match3':([(2,3),(4,5),(6,7)],0,1),
 'path_uv_ends':([(0,2),(2,3),(3,1)],0,1),   # u-2-3-v path
 'star_u3':([(0,2),(0,3),(0,4)],0,1),
 'tri_far':([(2,3),(3,4),(2,4)],0,1),
 'K22_far':([(2,3),(3,4),(4,5),(5,2)],0,1),
 'star_both':([(0,2),(0,3),(1,4),(1,5)],0,1),
}
if __name__=='__main__':
    D=int(sys.argv[1]); fam=sys.argv[2]; ns=[int(x) for x in sys.argv[3:]]
    N=make(D); H,u,v=FAM[fam]
    for n in ns:
        if n*D%2: continue
        P=contains(N,n,D,H+[(u,v)])/contains(N,n,D,H)
        base,A,B=gao(n,D,H,u,v)
        rp=P/(base*(1-A)*(1-B))-1; re=P/(base*exp(-A-B))-1
        print(f"D={D} {fam} n={n} n2*prod={rp*n*n:.4f} n2*exp={re*n*n:.4f}",flush=True)
