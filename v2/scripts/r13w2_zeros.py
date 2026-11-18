# Exact P(y)=E y^T (T=|E(G1)&E(G2)|, G1,G2 iid uniform L-regular, n vertices); nearest zero of P to y=1.
# Exact integer histogram + Taylor shift at y=1 (exact ints) + mpmath companion-matrix eig at high precision (no bracketing).
# G1 ranges over isomorphism-class reps (WL-hash bucket + exact nx.is_isomorphic), G2 over all labeled graphs.
# Usage: r13w2_zeros.py L n [dps]
import sys, itertools, numpy as np, mpmath as mp, networkx as nx
from math import comb
L,n=int(sys.argv[1]),int(sys.argv[2]); dps=int(sys.argv[3]) if len(sys.argv)>3 else 200
idx={(i,j):k for k,(i,j) in enumerate((i,j) for i in range(n) for j in range(i+1,n))}; M=len(idx)
def gen():
    deg=[0]*n; out=[]
    def rec(i,mask):
        if i==n: out.append(mask); return
        need=L-deg[i]; cand=[j for j in range(i+1,n) if deg[j]<L]
        if need<0 or need>len(cand): return
        for S in itertools.combinations(cand,need):
            m=mask
            for j in S: deg[j]+=1; m|=1<<idx[(i,j)]
            old=deg[i]; deg[i]=L; rec(i+1,m); deg[i]=old
            for j in S: deg[j]-=1
    rec(0,0); return out
G=gen(); N=len(G); print("N=",N,flush=True)
if N==0: sys.exit("no L-regular graphs")
def graph(g): return nx.Graph([e for e,k in idx.items() if g>>k&1])
buckets={}; 
for g in G:
    H=graph(g); h=nx.weisfeiler_lehman_graph_hash(H,iterations=3); b=buckets.setdefault(h,[])
    for r in b:
        if nx.is_isomorphic(r[1],H): r[2]+=1; break
    else: b.append([g,H,1])
src=[(r[0],r[2]) for b in buckets.values() for r in b]; print("classes=",len(src),flush=True)
W=(M+63)//64; msk=(1<<64)-1
arr=np.array([[(g>>(64*w))&msk for w in range(W)] for g in G],dtype=np.uint64)
def pc(a):
    a=a-((a>>np.uint64(1))&np.uint64(0x5555555555555555)); a=(a&np.uint64(0x3333333333333333))+((a>>np.uint64(2))&np.uint64(0x3333333333333333))
    a=(a+(a>>np.uint64(4)))&np.uint64(0x0f0f0f0f0f0f0f0f); return (a*np.uint64(0x0101010101010101))>>np.uint64(56)
hist=[0]*(M+1)
for g,wt in src:
    t=sum(pc(arr[:,w]&np.uint64((g>>(64*w))&msk)) for w in range(W)).astype(np.int64)
    for k,v in enumerate(np.bincount(t,minlength=M+1)): hist[k]+=wt*int(v)
assert sum(hist)==N*N
d=max(t for t in range(M+1) if hist[t])
c=[sum(hist[t]*comb(t,i) for t in range(i,d+1)) for i in range(d+1)]  # exact coeffs in w=y-1
mp.mp.dps=dps
a=[mp.mpf(x) for x in c]; k=len(a)-1  # companion matrix eigenvalues, no bracketing
C=mp.zeros(k,k)
for i in range(1,k): C[i,i-1]=1
for i in range(k): C[i,k-1]=-a[i]/a[k]
z=mp.eig(C,left=False,right=False)
zz=min(z,key=abs); R=abs(zz)
# self-check: residual of found root relative to coefficient scale
res=abs(mp.polyval([mp.mpf(x) for x in c[::-1]],zz))/sum(abs(mp.mpf(x))*R**i for i,x in enumerate(c))
print(f"L={L} n={n} N={N} deg={d} R={mp.nstr(R,8)} w={mp.nstr(zz,6)} R*L/n={mp.nstr(R*L/n,6)} relres={mp.nstr(res,2)}")
