# Verify: every <=4-edge subgraph count of a D-regular graph is affine in (t=#triangles, q=#4-cycles); brute-force check.
import itertools, random, sys, networkx as nx
from math import comb
def formulas(n,D,t,q):
    import sympy
    comb=(lambda a,b: sympy.expand_func(sympy.binomial(a,b))) if hasattr(n,'free_symbols') else globals()['comb']
    m=n*D/2 if hasattr(n,'free_symbols') else n*D//2; c2=n*comb(D,2); s3=n*comb(D,3)
    F={}
    F['K13']=s3; F['P3']=c2; F['K2']=m; F['K3']=t
    F['2K2']=comb(m,2)-c2
    F['P3K2']=c2*(m-3*D+2)+3*t
    F['P4']=m*(D-1)**2-3*t
    F['3K2']=comb(m,3)-F['P3K2']-F['P4']-s3-t
    F['K14']=n*comb(D,4)
    F['chair']=n*D*(D-1)*comb(D-1,2)-6*(D-2)*t
    F['P5']=c2*(D-1)**2-4*q-3*t*(2*D-3)
    F['C4']=q
    F['paw']=3*(D-2)*t
    F['K13K2']=s3*(m-4*D+3)+3*t*(D-2)
    F['P4K2']=F['P4']*(m-4*D+3)+4*q+6*t*(D-2)
    F['K3K2']=t*(m-3*D+3)
    F['4K2']=(F['3K2']*(m-6*D+3)+F['P4K2'])/4
    # two equations: total and cherry-weighted
    cher={'K14':6,'chair':4,'P5':3,'C4':4,'paw':5,'K13K2':3,'P4K2':2,'K3K2':3}
    rest=comb(m,4)-sum(F[k] for k in cher)-F['4K2']
    cw=c2*comb(m-2,2)-sum(F[k]*v for k,v in cher.items())
    # P3P3 + P3_2K2 = rest ; 2 P3P3 + P3_2K2 = cw
    F['P3P3']=cw-rest; F['P3_2K2']=rest-F['P3P3']
    return F
HOSTS={ 'K14':[(0,1),(0,2),(0,3),(0,4)],'chair':[(0,1),(0,2),(0,3),(3,4)],'P5':[(0,1),(1,2),(2,3),(3,4)],
 'C4':[(0,1),(1,2),(2,3),(3,0)],'paw':[(0,1),(1,2),(2,0),(2,3)],'K13K2':[(0,1),(0,2),(0,3),(4,5)],
 'P4K2':[(0,1),(1,2),(2,3),(4,5)],'K3K2':[(0,1),(1,2),(2,0),(3,4)],'P3P3':[(0,1),(1,2),(3,4),(4,5)],
 'P3_2K2':[(0,1),(1,2),(3,4),(5,6)],'4K2':[(0,1),(2,3),(4,5),(6,7)],
 'K3':[(0,1),(1,2),(2,0)],'P4':[(0,1),(1,2),(2,3)],'3K2':[(0,1),(2,3),(4,5)],'P3K2':[(0,1),(1,2),(3,4)],
 'K13':[(0,1),(0,2),(0,3)],'2K2':[(0,1),(2,3)],'P3':[(0,1),(1,2)],'K2':[(0,1)]}
# #copies in K_n = n!/(n-v)!/|Aut|
AUT={'K14':24,'chair':2,'P5':2,'C4':8,'paw':2,'K13K2':12,'P4K2':4,'K3K2':12,'P3P3':8,'P3_2K2':16,'4K2':384,
 'K3':6,'P4':2,'3K2':48,'P3K2':4,'K13':6,'2K2':8,'P3':2,'K2':2}
def ncopies(n,k):
    H=nx.Graph(HOSTS[k]); v=H.number_of_nodes(); r=1
    for i in range(v): r*=n-i
    return r//AUT[k]
if __name__=="__main__":
    for (n,D) in [(10,3),(12,4),(11,4)]:
        for trial in range(3):
            G=nx.random_regular_graph(D,n,seed=random.randrange(10**9))
            E=list(G.edges()); m=len(E)
            t=sum(nx.triangles(G).values())//3
            q=sum(1 for c in nx.simple_cycles(G,length_bound=4) if len(c)==4)
            F=formulas(n,D,t,q)
            # brute: classify 4-subsets of edges by canonical hash
            names={}
            for k,h in HOSTS.items(): names[nx.weisfeiler_lehman_graph_hash(nx.Graph(h),iterations=4)+str(len(h))]=k
            cnt={k:0 for k in HOSTS}
            for r in (1,2,3,4):
                for S in itertools.combinations(E,r):
                    cnt[names[nx.weisfeiler_lehman_graph_hash(nx.Graph(S),iterations=4)+str(r)]]+=1
            bad=[(k,cnt[k],F[k]) for k in F if F[k]!=cnt[k]]
            print(n,D,t,q,'MISMATCH' if bad else 'ok',bad)
