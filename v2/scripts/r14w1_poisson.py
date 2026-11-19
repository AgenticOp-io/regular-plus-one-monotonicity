# Poisson (cluster-free) part of the conditioning ratio R, expanded to n^-2; residual vs fitted r2(D).
import sympy as sp
n,D,e=sp.symbols('n D e',positive=True)
def LL(degs_sum_cd2, pair_sum, M):  # loops + doubles exact pairing expectations
    return degs_sum_cd2/(M-1) + pair_sum/((M-1)*(M-3))
def C2(d): return d*(d-1)/2
M=n*D
# regular: sum_i C2 = n C2(D); sum_{i<j} 2 C2C2 = (T^2 - sum C2^2) where T=sum C2
T=n*C2(D); Q=n*C2(D)**2
L0=LL(T,(T**2-Q),M)
d2=D-2; Mp=M-6
Tp=T-3*(C2(D)-C2(d2)); Qp=Q-3*(C2(D)**2-C2(d2)**2)
Lp=LL(Tp,(Tp**2-Qp),Mp)
x=3*d2**2/(Mp-1)   # three forbidden extra edges among a,b,c
logR=-(Lp+x-L0)
Epair=sp.Rational(1,6)*n*(n-1)*(n-2)*(D*(D-1))**3/((M-1)*(M-3)*(M-5))
logE=sp.log(Epair/((D-1)**3/sp.Integer(6)))+logR
ser=sp.series(logE.subs(n,1/e),e,0,3).removeO()
E=sp.series(sp.exp(ser),e,0,3).removeO()
c1=sp.simplify(E.coeff(e,1)); c2=sp.simplify(E.coeff(e,2))
r2=(D-1)*(11*D-16)/D**2
print('r1',sp.factor(c1)); print('r2_poisson',sp.factor(c2)); print('residual r2-poisson',sp.factor(sp.simplify(r2-c2)), sp.apart(sp.simplify(r2-c2),D))
for d in range(3,8): print(d, float(c2.subs(D,d)), float(r2.subs(D,d)), float((r2-c2).subs(D,d)))
