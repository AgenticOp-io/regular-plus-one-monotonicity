# r12w1: independent derivation of r1 in E[T]=(D-1)^3/6(1+r1/n) for G(n,D) via pairing model + simplicity conditioning,
# plus free fit of r1 from exact data (r11w1_d3/d4.txt). No use of the n^-1 cancellation.
import sympy as sp, numpy as np, os
n,D=sp.symbols('n D',positive=True); x=sp.symbols('x',positive=True)  # x=1/n
M=n*D
# 1. pairing model, exact: E_pair[T]=(n)_3/6 (D(D-1))^3 /((M-1)(M-3)(M-5))
Ep=n*(n-1)*(n-2)/6*(D*(D-1))**3/((M-1)*(M-3)*(M-5))
R_pair=sp.series((Ep/((D-1)**3/6)).subs(n,1/x),x,0,2).removeO()
# 2. P(simple|T)/P(simple)=exp(-dLam); Lam=E loops+E double edges (leading, first order in 1/n)
S=n*D*(D-1); S2=S-(12*D-18); M2=M-6      # 3 vertices drop from D(D-1) to (D-2)(D-3); 6 stubs removed
loops=S2/(2*M2)-S/(2*M); dbl=S2**2/(4*M2**2)-S**2/(4*M**2)
extra=3*(D-2)**2/M                        # extra a-b edge parallel to a triangle edge
dLam=sp.series(sp.together(loops+dbl+extra).subs(n,1/x),x,0,2).removeO()
print('dLam*n =',sp.factor(dLam.coeff(x,1)))
r1=sp.factor(R_pair.coeff(x,1)-dLam.coeff(x,1))
print('r1 =',r1,'  matches 3(D-1)/D:',sp.simplify(r1-3*(D-1)/D)==0)
# 3. free fit of r1 from exact E[T] (not assuming r1)
h=os.path.dirname(os.path.abspath(__file__))
for d in (3,4):
    a=np.atleast_2d(np.loadtxt(f"{h}/r11w1_d{d}.txt")); 
    if a.shape[0]<10: print(f"D={d}: data file too short, skipped"); continue
    m=a[:,0]>=80; N=a[m,0]; R=a[m,1]
    X=np.vstack([N**-i for i in range(1,6)]).T; c=np.linalg.lstsq(X,R-1,rcond=None)[0]
    print(f'D={d}: free-fit r1={c[0]:.6f}  predicted {3*(d-1)/d:.6f}')
