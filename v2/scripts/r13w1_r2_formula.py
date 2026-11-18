# r13w1: check r2(D)=(D-1)(11D-16)/D^2 against exact E[T] data; split into pairing part + conditioning remainder.
import sympy as sp, numpy as np, os
h=os.path.dirname(os.path.abspath(__file__))
D,x=sp.symbols('D x',positive=True); n=1/x; M=D/x
Ep=n*(n-1)*(n-2)/6*(D*(D-1))**3/((M-1)*(M-3)*(M-5))
Rp=sp.series(sp.simplify(Ep/((D-1)**3/6)),x,0,3).removeO()
r2pair=sp.factor(Rp.coeff(x,2)); r2=(D-1)*(11*D-16)/D**2
print('pairing n^-2 coeff:',r2pair,'\nremainder (conditioning on simple, incl. r1 cross terms):',sp.factor(sp.simplify(r2-r2pair)))
print('r2 =',sp.apart(r2,D),'; S1_1_1 c0 =',sp.factor(r2-sp.Rational(9,2)-15/D+sp.Rational(67,2)/D**2))
for d,f in ((3,'r11w1_d3.txt'),(4,'r13w1_d4.txt'),(5,'r13w1_d5.txt'),(6,'r13w1_d6.txt'),(7,'r13w1_d7.txt')):
    a=np.loadtxt(f'{h}/{f}'); nn=a[:,0]; y=nn**2*(a[:,1]-1-3*(d-1)/d/nn); m=nn>=(26 if d==7 else 30)
    X=np.vstack([nn[m]**-i for i in range(6)]).T; c=np.linalg.lstsq(X,y[m],rcond=None)[0][0]
    pred=float(r2.subs(D,d)); print(d,'fit %.5f pred %.5f'%(c,pred)); assert abs(c-pred)<2e-3
