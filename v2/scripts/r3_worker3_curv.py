# r3_worker3: first and second derivative of Phi0 in abar, using the EXACT exponential tilt of the hypergeometric overlap law.
# n*ell = 2 Phi'(abar), n^2 Phi_KK = 4 Phi''(abar).  Run: python v2/scripts/r3_worker3_curv.py
from mpmath import mp, mpf, binomial, exp, diff, findroot
mp.dps=60
def run(D,L):
    D,L=mpf(D),mpf(L); Dn,Ln=int(D),int(L)
    sup=range(max(0,2*Ln-Dn),Ln+1)
    w0={a:binomial(Ln,a)*binomial(Dn-Ln,Ln-a)/binomial(Dn,Ln) for a in sup}
    def mom(th):
        w={a:w0[a]*exp(th*a) for a in sup}; Z=sum(w.values())
        return [sum(mpf(a)**k*w[a] for a in sup)/Z for k in (1,2)]
    def Phi_th(th):
        a,s=mom(th)
        def E(c0,c1,c2): return c0+c1*a+c2*s       # E[c0+c1 A+c2 A^2]
        # polynomials in A as coefficient triples
        def sq(c): return c
        lB=E(0,-1,1)/(2*a)
        l1=E(L*(L-1),-(2*L-1),1)/(2*(L-a))
        muB=E(0,L,-1)**2/(2*a*(L-a)); mu1=E(L*L,-2*L,1)**2/(2*(L-a)**2)
        g=D-2*L; gam=g+a
        lg=E(g*(g-1),2*g-1,1)/(2*gam)
        mu4=(E(0,g,1)**2/(2*a)+E(L*g,L-g,-1)**2/(L-a))/gam
        return (-lB-lB**2)+(-l1-l1**2-muB)+(-l1-l1**2-muB-mu1)+(-lg-lg**2-mu4), a
    f=lambda th: Phi_th(th)[0]; abar=lambda th: Phi_th(th)[1]
    d1=diff(f,0)/diff(abar,0)
    d2=(diff(f,0,2)-d1*diff(abar,0,2))/diff(abar,0)**2
    return d1,d2
for D,L in [(10,1),(20,1),(40,1),(40,5),(60,10),(80,30)]:
    d1,d2=run(D,L)
    print(f"D={D:3d} L={L:2d}  n*ell={float(2*d1):+.5f}  n^2*Phi_KK={float(4*d2):+.5f}  Phi''={float(d2):+.3e}")
print("DONE r3_worker3_curv")
