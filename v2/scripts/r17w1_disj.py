# Ursell u_T for custom (incl. disjoint) shapes, exact. usage: python r17w1_disj.py D shape n...
import sys, os, itertools
from math import log
sys.path.insert(0, os.path.dirname(__file__))
from r5w3_exact import make, contains, Nseq
D=int(sys.argv[1]); nm=sys.argv[2]; ns=[int(x) for x in sys.argv[3:]]
def P(o,k): return [(o+i,o+i+1) for i in range(k)]
sh={'2e':[(0,1),(2,3)],'P2+P2':P(0,2)+P(3,2),'P3+e':P(0,3)+[(5,6)],'P3+P3':P(0,3)+P(4,3),'P3+P2':P(0,3)+P(4,2)}
S=sh[nm];K=len(S);N=make(D)
for n in ns:
    if n*D%2: continue
    tot=Nseq(N,D,[D]*n)
    lp=lambda U: log(contains(N,n,D,list(U))/tot) if U else 0.0
    u=sum((-1)**(K-r)*lp(U) for r in range(K+1) for U in itertools.combinations(S,r))
    print(D,nm,n,'u=%.4e'%u,' '.join('n^%d u=%.3f'%(a,n**a*u) for a in range(1,K+1)),flush=True)
