import sys, itertools
from functools import lru_cache
from fractions import Fraction
from math import log
sys.setrecursionlimit(10000)
def count(n, L, forb):
    """# simple graphs on [n] with degrees L - deg_forb... forb = frozenset of edges forced IN (we count with them removed)."""
    forced=set(forb); d=[L]*n
    for a,b in forced: d[a]-=1; d[b]-=1
    if min(d)<0: return 0
    @lru_cache(None)
    def rec(v, rem):
        if v==n: return 1 if not any(rem) else 0
        r=list(rem); k=r[v]; r[v]=0
        cand=[u for u in range(v+1,n) if r[u]>0 and (v,u) not in forced]
        if k>len(cand): return 0
        t=0
        for c in itertools.combinations(cand,k):
            q=r[:]
            for u in c: q[u]-=1
            t+=rec(v+1,tuple(q))
        return t
    return rec(0,tuple(d))
def run(n,L,shapes):
    Z=count(n,L,[])
    cache={}
    def lp(A):
        A=frozenset(A)
        if A not in cache:
            cache[A]=log(count(n,L,A)/Z) if count(n,L,A) else float('-inf')
        return cache[A]
    out={}
    for name,S in shapes.items():
        u=sum((-1)**(len(S)-r)*lp(A) for r in range(len(S)+1) for A in itertools.combinations(S,r))
        out[name]=u
    return out
shapes={'P5':[(0,1),(1,2),(2,3),(3,4)],'star4':[(0,1),(0,2),(0,3),(0,4)],'C4':[(0,1),(1,2),(2,3),(0,3)],
 'tri+pend':[(0,1),(1,2),(0,2),(2,3)],'4matching':[(0,1),(2,3),(4,5),(6,7)],'P3+2':[(0,1),(1,2),(3,4),(5,6)],
 'fork':[(0,1),(0,2),(0,3),(3,4)],'paw-ish P4+e':[(0,1),(1,2),(2,3),(4,5)]}
if __name__=='__main__':
    L=int(sys.argv[1])
    for n in map(int,sys.argv[2:]):
        r=run(n,L,shapes); print('L',L,'n',n,{k:'%.3e'%v for k,v in r.items()},flush=True)
