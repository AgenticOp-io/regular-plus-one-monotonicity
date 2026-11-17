# r9w3: S1_1_1 (u-w, v-w, target uv) exp-form err as exact function of E[T]=(D-1)^3/6*(1+r1/n+r2/n^2).
# Exact: P(uv|uw,vw)=6E[T]/(n D (D-1)).  Gao exp-form pieces as in r7_run.gao (j=k=w=1).
import sympy as sp
n,D,x,r1,r2=sp.symbols('n D x r1 r2')
dt={'u':D-1,'v':D-1,'w':D-2}
M=n*D-sum(D-d for d in dt.values())            # remaining half-edges
M2=sum(d*(d-1) for d in dt.values())+(n-3)*D*(D-1)
A=M2**2/M**3+M2/M**2
su=dt['w']; sv=dt['w']
phi=-2*(dt['u']+dt['v'])+2-su-sv-(dt['u']+dt['v']-2)*M2/M+dt['u']*dt['v']
B=phi/M
ET=(D-1)**3/6*(1+r1*x+r2*x**2)
P=6*ET/(n*D*(D-1))
err=(P/(dt['u']*dt['v']/M*sp.exp(-A-B))-1).subs(n,1/x)
s=sp.series(err,x,0,3).removeO()
c=[sp.factor(sp.simplify(s.coeff(x,i))) for i in range(3)]
print('n^0:',c[0]); 
r1s=sp.solve(c[1],r1)[0]; print('r1(D) forced by n^-1 vanishing =',sp.factor(r1s))
c0=sp.factor(sp.simplify(c[2].subs(r1,r1s))); print('c0 =',c0)
r2s=sp.solve(sp.Eq(c0,sp.Symbol('c')),r2)[0]; print('r2(D) =',sp.factor(r2s))
# n^-1 check: E[T] known exactly? D=3: E[T]=(8/6)(1+r1/n)
print('r1(3)=',r1s.subs(D,3),' r1(4)=',r1s.subs(D,4))
import pickle; pickle.dump((str(r1s),str(r2s)),open('r9w3_tri.pkl','wb'))
