# c_n(D)=D2 log Q = Delta(P3)-2Delta(e) via exact degree-type DP (r5w3_exact.contains). usage: r21a_cD.py D n1 n2 ...
import sys,os,time; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from math import log,factorial
from r5w3_exact import make,contains
sys.setrecursionlimit(100000)
def lf2(m): return sum(log(k) for k in range(m,0,-2))
D=int(sys.argv[1]); N=make(D)
for n in map(int,sys.argv[2:]):
    if n*D%2: continue
    t=time.time()
    def lq(H):
        h=[0]*n
        for a,b in H: h[a]+=1;h[b]+=1
        return log(contains(N,n,D,H))+sum(log(factorial(D-x)) for x in h)-lf2(n*D-2*len(H)-1)
    c=lq([(0,1),(1,2)])-2*lq([(0,1)])+lq([])
    print(D,n,'%.8f'%c,'n*c=%.5f'%(n*c),'t=%.1f'%(time.time()-t),flush=True)
