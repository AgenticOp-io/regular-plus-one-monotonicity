# Symbolic 4th Ursell u_T = sum_{U<=T}(-1)^{4-|U|} log P(U in G), T connected 4-edge, via counts affine in (t,q).
import sympy as sp, itertools, networkx as nx
from r23a_counts import formulas,HOSTS,ncopies
n,e1,e2,f1,f2,x=sp.symbols('n e1 e2 f1 f2 x')
Et=sp.Rational(8,6)*(1+e1/n+e2/n**2); Eq=sp.Rational(16,8)*(1+f1/n+f2/n**2)
D=3
F=formulas(n,D,Et,Eq)
names={}
for k,h in HOSTS.items(): names[(nx.weisfeiler_lehman_graph_hash(nx.Graph(h),iterations=4),len(h))]=k
def P(S):
    if not S: return 1
    k=names[(nx.weisfeiler_lehman_graph_hash(nx.Graph(list(S)),iterations=4),len(S))]
    return sp.Integer(1)*F[k]/ncopies(n,k)
def u(T):
    tot=0
    for r in range(1,5):
        for S in itertools.combinations(T,r): tot+=(-1)**(4-r)*sp.log(P(S))
    return tot

import mpmath as mp
mp.mp.dps=80
for name in ['P5','C4','paw','chair']:
    f=sp.lambdify((n,e1,e2,f1,f2),u(HOSTS[name]),'mpmath')
    for N in (10**3,10**4,10**5):
        N=mp.mpf(N); b=f(N,0,0,0,0)
        d=[ (f(N,*[1 if j==i else 0 for j in range(4)])-b) for i in range(4)]
        print(name,'n=%g'%N,'u0*n^2=%.4g'%(b*N**2),' du/de1*n^2=%.4g de2*n^3=%.4g df1*n^2=%.4g df2*n^3=%.4g'%(d[0]*N**2,d[1]*N**3,d[2]*N**2,d[3]*N**3))
