# Empty host: exact p=D/(n-1) vs Gao Thm6 principal term, product vs exp form. Expands in x=1/n.
import sympy as sp
D,n,x=sp.symbols('D n x',positive=True)
M=D*n; M2=D*(D-1)*n
A=M2**2/M**3+M2/M**2
phi=-4*D+2-(2*D-2)*M2/M+D**2
B=phi/M
p=D/(n-1); base=D*D/M
def ser(e,k=4): return sp.series(sp.simplify(e.subs(n,1/x)),x,0,k).removeO()
for name,f in [('product',(1-A)*(1-B)),('exp',sp.exp(-A-B))]:
    r=sp.expand(sp.series(sp.simplify((p/(base*f)).subs(n,1/x)),x,0,4).removeO())
    print(name,'p/principal - 1 =',sp.collect(sp.simplify(r-1),x))
