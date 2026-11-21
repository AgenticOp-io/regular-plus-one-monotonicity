"""r48 step 2: tree-like (regular, uniform overlap o=2m/n) degree-3 cluster term of ln Z, gamma3=d/dm,
symbolic large-n series, and backward-recursion shift dS with gamma2+gamma3 vs gamma2 (mpmath)."""
import sympy as sp, mpmath as mp, sys
n,L,u,a,m=sp.symbols('n L u a m',positive=True)
o=2*m/n; da=L-o
s=a*da-u; Q2v=a**2*da+u; Q3v=a**3*da-u
e1=n/2*s; Q2=n/2*Q2v; P2=n*(s**2-Q2v)/2
e2=(e1**2-Q2)/2-P2
D3=e1**3-3*e1*Q2+n/2*2*(a**3*da-u)
A1=e1*P2-n*(Q2v*s-Q3v)
# B: per edge of weight w, N=2(s-w), SQ=2(Q2v-w^2); edge counts n/2*da (w=a), n/2*u (w=-1)
Bf=lambda w: w*((2*(s-w))**2-2*(Q2v-w**2))/2
B=n/2*(da*Bf(a)+u*Bf(-1))
Tr=n*(s**3-3*s*Q2v+2*Q3v)/6
e3=D3/6-(A1-B+Tr)
q=lambda k: 1/sp.prod([n-1-2*i for i in range(k)])
q1,q2,q3=q(1),q(2),q(3)
lnZ2=q1*e1+(q2-q1**2)*e1**2/2-q2*(Q2/2+P2)
lnZ3=q3*e3-q1*q2*e1*e2+q1**3*e1**3/3
g2=sp.diff(lnZ2,m); g3=sp.diff(lnZ3,m)
# large-n series of g3 with m=jL/2, u=j-1  (j,y symbolic)
j,y,eps=sp.symbols('j y eps',positive=True)
G3=sp.simplify(g3.subs({m:j*L/2,u:j-1,a:y-1}))
ser=sp.series(G3.subs(n,1/eps),eps,0,4).removeO()
print("gamma3 series in 1/n:"); print(sp.collect(sp.expand(ser),eps))
G2=g2.subs({m:j*L/2,u:j-1,a:y-1})
ser2=sp.series(sp.simplify(G2.subs(n,1/eps)),eps,0,4).removeO()
print("gamma2 series:"); print(sp.collect(sp.expand(ser2),eps))
f2=sp.lambdify((n,L,j,y),G2,'mpmath'); f3=sp.lambdify((n,L,j,y),g3.subs({m:j*L/2,u:j-1,a:y-1}),'mpmath')
mp.mp.dps=60
def run(N,LL,x,fs):
    ys=[None]*(LL+2); ys[LL]=mp.mpf(x); acc=mp.mpf(0)
    for jj in range(LL-1,0,-1):
        k=jj+1; acc+=sum(f(mp.mpf(N),mp.mpf(LL),mp.mpf(k),ys[k]) for f in fs); ys[jj]=x*mp.e**acc
    return ys[1:LL+1]
if __name__=="__main__":
    x=2
    print("n L | gamma3*n^2/L^2 (j=L/2,y=1.5) | dS3 n^2/L^4 | dS3 n^2/L^5 | dS3 n^3/L^6 | dS(2 vs lead) n^2/L^4")
    lead=lambda N,LL,k,yy: -(yy-1)/(N-1)
    for N in (10**4,10**6,10**8):
        for LL in (10,30,100,300):
            if LL*LL>N/2: continue
            t2=run(N,LL,x,[f2]); t23=run(N,LL,x,[f2,f3]); l=run(N,LL,x,[lead])
            d3=sum((i+1)*(t23[i]-t2[i]) for i in range(LL)); d2=sum((i+1)*(t2[i]-l[i]) for i in range(LL))
            g=f3(mp.mpf(N),mp.mpf(LL),mp.mpf(LL//2),mp.mpf(1.5))
            print(N,LL,mp.nstr(g*N**2/LL**2,4),mp.nstr(d3*N**2/LL**4,4),mp.nstr(d3*N**2/LL**5,4),mp.nstr(d3*N**3/LL**6,4),mp.nstr(d2*N**2/LL**4,4)); sys.stdout.flush()
