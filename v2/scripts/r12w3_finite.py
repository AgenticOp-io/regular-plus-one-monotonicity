# r12w3: evaluate the r11w3 formula at FINITE n (no series) and compare n^2*err with r7 data directly.
import sympy as sp, os, sys
n,D=sp.symbols('n D',positive=True)
ff=lambda a,m: sp.prod([a-i for i in range(m)]) if m>0 else sp.Integer(1)
def errexpr(j,k,r1=3*(D-1)/D):
    F=lambda t: sum(sp.binomial(j,c)*ff(t,c)*ff(D-1-t,j-c)*ff(D-1-c,k) for c in range(0,min(j,t)+1))
    F0,F1,F2=F(0),F(1)-F(0),F(2)-2*F(1)+F(0)
    Et=(D-1)**3/(n*D)*(1+r1/n); Et2=((D-1)**3/(n*D))**2
    N2=n*D*(F0+F1*Et+F2*Et2/2)
    g=lambda s: ff(D-s,k); gm=[sum((-1)**(m-i)*sp.binomial(m,i)*g(i) for i in range(m+1)) for m in range(3)]
    eL=sp.binomial(j,2)*(D-1)**2/(n*D)
    pairs=j*(D-j)*(D-1)**2/(n*D)+sp.binomial(j,2)*(D-1)**3/(n*D)
    N1=n*ff(D,j)*((n-1-j)*gm[0]+gm[1]*((j+1)*D-2*j-2*eL)+gm[2]*pairs)
    du,dv=D-j,D-k; leaves=[D-1]*(j+k)
    M=n*D-2*(j+k); M2=du*(du-1)+dv*(dv-1)+sum(d*(d-1) for d in leaves)+(n-2-len(leaves))*D*(D-1)
    A=M2**2/M**3+M2/M**2
    phi=-2*(du+dv)+2-j*(D-1)-k*(D-1)-(du+dv-2)*M2/M+du*dv
    return N2/N1/(du*dv/M*sp.exp(-A-phi/M))-1
if __name__=='__main__':
    base=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','notes','r7_data')
    for j,k in [(2,1),(2,2),(3,1),(3,2)]:
        e=errexpr(j,k)
        for Dv in (6,8):
            print(j,k,'D',Dv,'n: data/formula(n^2 err)')
            for l in open(f'{base}/d{Dv}.txt'):
                t=l.split()
                if len(t)==5 and t[1]==f'S{j}_{k}_0': nv=int(t[2]); print(' ',nv,t[4],round(float(e.subs({D:Dv,n:nv}))*nv**2,4))
