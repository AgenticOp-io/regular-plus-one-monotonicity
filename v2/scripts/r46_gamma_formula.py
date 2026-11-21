"""r46: (1) true gamma-correction delta(y,j,m) from the r36 s2 second-order ln Z formula (analytic in m),
(2) rerun the r36/r45 backward recursion with that gamma (m_j=jL/2 mean overlap) vs leading gamma, report total shift.
Regular F (deg L), U (deg u=j-1), overlap o=2m/n per vertex. Linear regime."""
import numpy as np
def lnZ(n,L,u,m,y):
    nF=n*L/2; nU=n*u/2; a=y-1
    W1=a*(nF-m)-nU; Q2=a*a*(nF-m)+nU
    o=2*m/n; s=a*(L-o)-u; P2=n*(s*s-(a*a*(L-o)+u))/2
    q1=1/(n-1); q2=1/((n-1)*(n-3))
    return q1*W1+(q2-q1*q1)*W1**2/2-q2*(Q2/2+P2)
def gam(n,L,j,m,y,h=0.5):  # d lnZ/dm
    u=j-1
    return (lnZ(n,L,u,m+h,y)-lnZ(n,L,u,m-h,y))/(2*h)
def run(n,L,x,true):
    y=np.zeros(L+2); y[L]=x; acc=0.0
    for j in range(L-1,0,-1):
        k=j+1; m=k*L/2
        acc+=(gam(n,L,k,m,y[k]) if true else -(y[k]-1)/(n-1)); y[j]=x*np.exp(acc)
    return y[1:L+1]
if __name__=="__main__":
    x=2.0
    print("n L | per-step delta*n^2/L (j=L/2) | total S shift*n^2/L^4  (S=sum j dy_j)")
    for n in (10**4,10**6,10**8):
        for L in (10,30,100,300,1000):
            if L*L>n/2: continue
            j=L//2; y=1.5; d=gam(n,L,j,j*L/2,y)+(y-1)/(n-1)
            t=run(n,L,x,True); l=run(n,L,x,False)
            dS=sum((i+1)*(t[i]-l[i]) for i in range(L))
            print(n,L,"%.3f  %.3f  dS=%.2e"%(d*n*n/L,dS*n*n/L**4,dS))
