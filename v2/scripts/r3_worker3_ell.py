# r3_worker3: exact l = dPhi0/dK at the typical overlap, from the four McKay exponents (lem:mckay-exponent)
# with abar free and E[a^2] following the exchangeable-conditioned (tilted) law.  Run: python v2/scripts/r3_worker3_ell.py
import sympy as sp
D,L,ab,m2=sp.symbols('D L ab m2',positive=True)
ff=lambda k:sp.ff(L,k)**2/sp.ff(D,k)           # E (a)_k, a~Hypergeom(D;L,L)
q=ff(1); Ea2=ff(2)+q; Ea3=ff(3)+3*ff(2)+q
slope=sp.simplify((Ea3-Ea2*q)/(Ea2-q**2))        # d E[a^2] / d abar = Cov(a^2,a)/Var(a)
Ea2_of=lambda a: Ea2+slope*(a-q)
def Phi(a):
    s=Ea2_of(a); g1=D-2*L+a
    Ef=lambda poly: sp.expand(poly)  # moments of a polynomial of degree<=2 in a
    def E(expr):                      # expectation of quadratic polynomial in a
        P=sp.Poly(sp.expand(expr),sp.Symbol('A')); c=P.all_coeffs()[::-1]+[0,0]
        return c[0]+c[1]*a+c[2]*s
    A=sp.Symbol('A')
    lB=E(A*(A-1))/(2*a); l1=E((L-A)*(L-A-1))/(2*(L-a))
    muB=E(A*(L-A))**2/(2*a*(L-a)); mu1=E((L-A)**2)**2/(2*(L-a)**2)
    gam=D-2*L+a; lg=E((D-2*L+A)*(D-2*L+A-1))/(2*gam)
    mu4=(E(A*(D-2*L+A))**2/(2*a)+E((L-A)*(D-2*L+A))**2/(L-a))/gam
    return (-lB-lB**2)+(-l1-l1**2-muB)+(-l1-l1**2-muB-mu1)+(-lg-lg**2-mu4)
P0=sp.simplify(Phi(q)); x=1/(D-1)
E0=-(D**2-2)/4
print("lemma check (should be 0):",sp.simplify(P0-(D**2-1)/4-2*E0-(-x/2-x**2/4)))
dPhi=sp.simplify(sp.diff(Phi(ab),ab).subs(ab,q))   # dPhi/d abar ; dK = n d abar/2  => ell = 2 dPhi/(n)... see below
ell_n=sp.simplify(dPhi*2)                          # n*ell
print("n*ell exact:",sp.factor(ell_n))
for Dv,Lv in [(20,1),(100,1),(100,5),(1000,1),(1000,10),(1000,100)]:
    v=ell_n.subs({D:Dv,L:Lv}); print(f"D={Dv} L={Lv}  n*ell={float(v):.4f}  ratio to D-2L={float(v)/(Dv-2*Lv):.4f}")
print("series D->oo, L fixed:",sp.series(ell_n.subs(L,1),D,sp.oo,3))
sig2=L**2*(D-L)**2/(D**2*(D-1)); psi=D/(2*(D-1))
sK2=sp.simplify(sig2/(4*(1-psi)))                  # sigma_K^2 / n
print("sigma_K^2/n:",sp.factor(sK2))
t=sp.simplify(ell_n**2*sK2/2)                      # n * ell^2 sigma_K^2/2
for Dv,Lv in [(100,1),(1000,1),(1000,10),(1000,100)]:
    print(f"D={Dv} L={Lv}  n*ell^2*sK^2/2={float(t.subs({D:Dv,L:Lv})):.5g}   vs L^2 D/4={Lv**2*Dv/4}")
print("DONE r3_worker3_ell")
