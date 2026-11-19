# Ursell u_T of the pure pairing-model log p_U (closed form) for P_k; compare to exact simple-graph u_T (r16_longpath.py).
# The difference is the Ursell of log P(simple|U). usage: python r17w1_pairing.py D K n...
import sys, itertools
from math import log, perm
D=int(sys.argv[1]); K=int(sys.argv[2]); ns=[int(x) for x in sys.argv[3:]]
S=[(i,i+1) for i in range(K)]
def lp(U,n):
    d={}
    for a,b in U: d[a]=d.get(a,0)+1; d[b]=d.get(b,0)+1
    v=sum(log(perm(D,x)) for x in d.values() if x<=D)
    return v-sum(log(n*D-1-2*i) for i in range(len(U)))
for n in ns:
    u=sum((-1)**(K-r)*lp(U,n) for r in range(K+1) for U in itertools.combinations(S,r))
    print(D,'P%d'%K,n,'pairing u=%.4e'%u,' '.join('n^%d u=%.4f'%(a,n**a*u) for a in range(K-2,K+1)))
