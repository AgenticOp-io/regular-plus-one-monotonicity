# L=1: P(1+w)=sum_i C(m,i)(2m-2i-1)!!/(2m-1)!! w^i, n=2m. Nearest zero to w=0 (R), report R/n.
import mpmath as mp, sys
mp.mp.dps=120
def df(k): # (2k-1)!!
    r=mp.mpf(1)
    for j in range(1,k+1): r*=2*j-1
    return r
for m in [4,5,8,12,16,24,32,48,64]:
    c=[mp.binomial(m,i)*df(m-i)/df(m) for i in range(m+1)]
    z=mp.polyroots(c[::-1],maxsteps=2000,extraprec=400)
    zz=min(z,key=abs)
    print(m,2*m,mp.nstr(abs(zz),8),mp.nstr(zz,6),"R/n=",mp.nstr(abs(zz)/(2*m),6),"R/sqrt(n)=",mp.nstr(abs(zz)/mp.sqrt(2*m),6))
# checks: (a) Gaussian rep  P(1+w)=E(g^2+w)^m/E g^{2m} equals the series; (b) rho=W(1/e) vs Richardson limit of R/n
m=6; w=mp.mpf('0.7')+0.3j
ser=sum(mp.binomial(m,i)*df(m-i)/df(m)*w**i for i in range(m+1))
rep=mp.quad(lambda g:(g*g+w)**m*mp.exp(-g*g/2),[-mp.inf,0,mp.inf])/mp.quad(lambda g:g**(2*m)*mp.exp(-g*g/2),[-mp.inf,0,mp.inf])
assert abs(ser-rep)<1e-20, (ser,rep)
rho=mp.lambertw(1/mp.e).real
def Rn(m):
    c=[mp.binomial(m,i)*df(m-i)/df(m) for i in range(m+1)]
    return abs(min(mp.polyroots(c[::-1],maxsteps=2000,extraprec=400),key=abs))/(2*m)
a,b=Rn(32),Rn(48); lim=(48*b-32*a)/16   # R/n = c + a/m
print("Richardson limit R/n =",mp.nstr(lim,6)," W(1/e) =",mp.nstr(rho,6))
