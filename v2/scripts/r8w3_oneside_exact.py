# r8w3: EXACT n^-2 exp-form coefficient c0(D,j) for host = star of j edges at u, target uv (v not a leaf).
# Exact truth: P(uv | star)=(D-j)/(n-1-j)  (regular graph is vertex-transitive: E[#(j+1)-stars at u] = C(D,j+1)).
import sympy as sp
n,D,x=sp.symbols('n D x',positive=True)
def c0(j):
    # degrees: u=D-j, v=D, j leaves D-1, rest D;  (mirrors r7_run.gao with k=0,w=0)
    M=n*D-2*j; M2=D*(D-1)+(D-j)*(D-j-1)+j*(D-1)*(D-2)+(n-2-j)*D*(D-1)
    A=M2**2/M**3+M2/M**2
    su=j*(D-1)
    phi=-2*(D-j+D)+2-su-0-(2*D-j-2)*M2/M+(D-j)*D
    B=phi/M
    P=(D-j)/(n-1-j)
    err=P/((D-j)*D/M*sp.exp(-A-B))-1
    s=sp.series(sp.simplify(err.subs(n,1/x)),x,0,3).removeO()
    return [sp.factor(sp.simplify(s.coeff(x,i))) for i in range(3)]
for j in range(1,5):
    c=c0(j); print('j=',j,'n^-0,-1,-2 coeffs:',c)
    print('  c0(D) =',c[2],'  D=4..10:',[float(c[2].subs(D,d)) for d in range(4,11)],' D->inf:',sp.limit(c[2],D,sp.oo))
