# u_T for paths P_k (k edges) in D-regular, to test exponent: n^-ceil((k-1)/2) (first-order defect clusters) vs n^-(k-1)
import sys, os, itertools
from math import log
sys.path.insert(0, os.path.dirname(__file__))
from r5w3_exact import make, contains, Nseq
D=int(sys.argv[1]); K=int(sys.argv[2]); ns=[int(x) for x in sys.argv[3:]]
N=make(D)
S=[(i,i+1) for i in range(K)]
for n in ns:
    if n*D%2: continue
    tot=Nseq(N,D,[D]*n)
    lp=lambda U: log(contains(N,n,D,list(U))/tot) if U else 0.0
    u=sum((-1)**(K-r)*lp(U) for r in range(K+1) for U in itertools.combinations(S,r))
    print(D,'P%d'%K,n,'u=%.4e'%u,' '.join('n^%d u=%.4f'%(a,n**a*u) for a in range(1,K)),flush=True)
