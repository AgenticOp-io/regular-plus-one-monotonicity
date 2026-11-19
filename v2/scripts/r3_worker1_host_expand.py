"""Symbolic coefficient of the host degree variance m2=(1/n)sum y^2 (and m3) in Psi (see r3_worker1_host_exponent.py)."""
import sympy as sp
h,L,t,m2,m3,H=sp.symbols('h L t m2 m3 H',positive=True)
def avg(f):  # (1/n) sum_v f(h+y_v), mean y=0, to 3rd order
    return f(h)+sp.diff(f(H),H,2).subs(H,h)*m2*t**2/2+sp.diff(f(H),H,3).subs(H,h)*m3*t**3/6
q=lambda H:L**2/H; a2=lambda H:L**2/H+(L*(L-1))**2/(H*(H-1))
Sa=avg(q); Sa2=avg(a2); Sc=L-Sa; Sc2=avg(lambda H:L*L-2*L*q(H)+a2(H))
Sg=avg(lambda H:H-2*L+q(H)); Sg2=avg(lambda H:(H-2*L)**2+2*(H-2*L)*q(H)+a2(H))
Sag=avg(lambda H:(H-2*L)*q(H)+a2(H)); Scg=avg(lambda H:L*(H-2*L)+L*q(H)-(H-2*L)*q(H)-a2(H))
Sac=L*Sa-Sa2
lam=lambda s2,s1:(s2-s1)/(2*s1)
lB=lam(Sa2,Sa); l1=lam(Sc2,Sc); lg=lam(Sg2,Sg)
E1=-lB-lB**2; E2=-l1-l1**2-Sac**2/(2*Sa)/Sc
E3=-l1-l1**2-(Sac**2/(2*Sa)+Sc2**2/(2*Sc))/Sc
E4=-lg-lg**2-(Sag**2/(2*Sa)+Scg**2/Sc)/Sg
S1=avg(lambda H:H-L); S2=avg(lambda H:(H-L)**2)
l0=lam(S2,S1); E0=-(L*L-1)/sp.Integer(4)-l0-l0**2-L*S1/2
Sh1=avg(lambda H:H); Sh2=avg(lambda H:H**2); lh=lam(Sh2,Sh1)
Psi=E1+E2+E3+E4-lh-lh**2-2*E0
c=sp.series(Psi,t,0,4).removeO()
A=sp.factor(sp.simplify(c.coeff(t,2)/m2)); B=sp.factor(sp.simplify(c.coeff(t,3)/m3))
print("t^0 :",sp.factor(sp.simplify(c.coeff(t,0)))); print("A (coef of m2):",A); print("B (coef of m3):",B)
for lv in (1,2,5,50):
    print("L=",lv," A*h^3 as h->oo:",sp.limit(A.subs(L,lv)*h**3,h,sp.oo)," A*h^2:",sp.limit(A.subs(L,lv)*h**2,h,sp.oo))
