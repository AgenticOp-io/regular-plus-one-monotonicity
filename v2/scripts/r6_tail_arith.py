# exact check: sum_{k>=4} (Cw)^k L^{k+1}/n^{k-1} <= 2 (Cw)^4 L^5/n^3 when r=CwL/n<=1/2
from fractions import Fraction as F
for n,L,Cw in [(10**6,100,3),(10**8,1000,5),(10**4,30,2),(10**6,10**3,1)]:
    r=F(Cw*L,n); assert r<=F(1,2)
    s=sum(F(Cw)**k*F(L)**(k+1)/F(n)**(k-1) for k in range(4,200))
    b=2*F(Cw)**4*F(L)**5/F(n)**3
    assert s<=b; print(n,L,Cw,float(s),float(b),float(b) if L**5/n**3 else 0)
# o(1) range: L^5/n^3 -> 0 iff L=o(n^{3/5}); at L=n^{1/2}: n^{-1/2}
print("L^5/n^3 at L=n^.5, n=1e8:",(1e8**.5)**5/1e8**3)
