# r11w3: symbolic c0(D;j,k) for TWO-SIDED star hosts with w=0 (u has j leaves, v has k leaves, target uv).
# Method: P(uv|H)=E[N2]/E[N1] (exchangeability), N2/N1 = counts of embedded trees, written exactly via inclusion-exclusion in
# t=#common nbrs of edge uv (N2) and s_v=#nbrs of v in {u}+L (N1). Only needs E[triangles] to n^-1 (r1=3(D-1)/D, ASSUMED as in r9w3)
# and LEADING-order stub-model values for diamond/C4/triangle-near-leaf terms (those enter at relative n^-2).
import sympy as sp, sys
n,D,x=sp.symbols('n D x',positive=True)
ff=lambda a,m: sp.prod([a-i for i in range(m)]) if m>0 else sp.Integer(1)
def c0(j,k,r1=3*(D-1)/D):
    # --- N2 per directed edge: F(t)
    F=lambda t: sum(sp.binomial(j,c)*ff(t,c)*ff(D-1-t,j-c)*ff(D-1-c,k) for c in range(0,min(j,t)+1))
    F0,F1,F2=F(0),F(1)-F(0),F(2)-2*F(1)+F(0)
    Et=(D-1)**3/(n*D)*(1+r1/n); Et2=(D-1)**4*(D-2)**2/(n*D)**2   # E(t)_1, E(t)_2 (leading)
    N2=n*D*(F0+F1*Et+F2*Et2/2)
    # --- N1 = n (D)_j * E_L[ ... ]
    g=lambda s: ff(D-s,k); gm=[sum((-1)**(m-i)*sp.binomial(m,i)*g(i) for i in range(m+1)) for m in range(3)]
    eL=sp.binomial(j,2)*(D-1)**2/(n*D)
    pairs=j*(D-j)*(D-1)**2/(n*D)+sp.binomial(j,2)*(D-1)**3/(n*D)
    N1=n*ff(D,j)*((n-1-j)*gm[0]+gm[1]*((j+1)*D-2*j-2*eL)+gm[2]*pairs)
    P=N2/N1
    du,dv=D-j,D-k; leaves=[D-1]*(j+k)
    M=n*D-2*(j+k); M2=du*(du-1)+dv*(dv-1)+sum(d*(d-1) for d in leaves)+(n-2-len(leaves))*D*(D-1)
    A=M2**2/M**3+M2/M**2
    phi=-2*(du+dv)+2-j*(D-1)-k*(D-1)-(du+dv-2)*M2/M+du*dv
    err=(P/(du*dv/M*sp.exp(-A-phi/M))-1).subs(n,1/x)
    s=sp.series(err,x,0,3).removeO()
    return [sp.factor(sp.simplify(s.coeff(x,i))) for i in range(3)]
if __name__=='__main__':
    for j,k in [(1,0),(2,0),(1,1),(2,1),(2,2),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(4,4)]:
        c=c0(j,k); L=(j+k+1)**2/2
        print(f'j,k={j},{k} n^0:{c[0]} n^-1:{c[1]}\n  c0(D)={c[2]}\n  limD={sp.limit(c[2],D,sp.oo)}  (j+k+1)^2/2={L}  D=5,10,50,1000:',[round(float(c[2].subs(D,d)),3) for d in (5,10,50,1000)],flush=True)
