"""Exact Var_{mu_D}(T), T(G0)=sum_{ij in G0} b_i b_j, sum b=0, mu_D uniform D-regular on [n].
Only S_n-invariance + regularity used:  c1=-p(1-p)/(n-2) (edges sharing a vertex), c2=p(1-p)/C(n-2,2) (disjoint), p=D/(n-1).
Closed form:  Var T = p(1-p)*[ s2^2/2 ... ] computed below and checked against brute force."""
from fractions import Fraction as Fr
from itertools import combinations
import random
def regular_graphs(n,D):
    E=list(combinations(range(n),2)); deg=[0]*n; out=[]
    def rec(i,chosen):
        if i==len(E):
            if all(d==D for d in deg): out.append(tuple(chosen))
            return
        a,b=E[i]
        # prune: vertex a finished after its last edge (a,n-1)
        if deg[a]<D and deg[b]<D:
            deg[a]+=1;deg[b]+=1;chosen.append(E[i]);rec(i+1,chosen);chosen.pop();deg[a]-=1;deg[b]-=1
        if b==n-1 and deg[a]!=D: return
        if a==n-2 and b==n-1 and deg[a]!=D: return
        rec(i+1,chosen)
    rec(0,[]);return out
def formula(b,D):
    n=len(b); p=Fr(D,n-1); s2=sum(x*x for x in b); s4=sum(x**4 for x in b); assert sum(b)==0
    P=(s2*s2-s4)/2                      # sum_e b_e^2
    A=(2*s4-s2*s2)/2*2                  # ordered pairs (e,f) sharing exactly one vertex, sum b_e b_f
    Dis=(s2*s2/4-P-A)                   # ordered disjoint pairs (e!=f)  since (sum b_e)^2=s2^2/4
    c1=-p*(1-p)/(n-2); c2=p*(1-p)/Fr((n-2)*(n-3),2)
    return p*(1-p)*P+c1*A+c2*Dis
def brute(b,D):
    gs=regular_graphs(len(b),D); Ts=[sum(b[i]*b[j] for i,j in g) for g in gs]; m=Fr(sum(Ts),len(Ts))
    return Fr(sum((t-m)**2 for t in Ts),len(Ts)),len(gs)
if __name__=="__main__":
    random.seed(5)
    for n,D in [(6,2),(7,2),(8,2),(8,3)]:
        b=[Fr(random.randint(-6,6)) for _ in range(n)]; b[0]-=sum(b)
        bv,N=brute(b,D); f=formula(b,D); print(n,D,N,"graphs  brute",float(bv),"formula",float(f)); assert bv==f
    # asymptotics: Var(T)/(2M')^2, b~N(0,h), residual degree r=h-D=eps*D
    import math
    for D,n,eps in [(50,10**5,.5),(200,10**6,.5),(200,10**6,.1)]:
        h=(1+eps)*D; s2=n*h; s4=3*n*h*h; v=float(formula([0]*0+[],0)) if False else None
        p=D/(n-1); Pv=(s2*s2-s4)/2; VarT=p*(1-p)*Pv  # leading
        sd_u=math.sqrt(VarT)/(n*eps*D); print(f"D={D} n={n} eps={eps}: sd(T/2M')~{sd_u:.2e}  D^(-3/2)={D**-1.5:.2e}  D^2/sqrt(n)/eps~{D*D/math.sqrt(n)/eps:.2e}")
