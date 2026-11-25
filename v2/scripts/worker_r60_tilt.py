# numeric check of ln E_a e^{R}, R = (A0/2) tau^2, A0 = n L^2, on window t<=2/n; tilted by a=nL/2
import numpy as np
def logsumexp(x):
  m=x.max(); return m+np.log(np.exp(x-m).sum())
for n in (200,800,3200):
  al=(n+1)/2; q1=1/(n-1)
  for L in (2,10,n/200):
    a=n*L/2; A0=n*L*L
    t=np.linspace(1e-3/n,2/n,400001); dt=t[1]-t[0]
    lf=-(al+1)*np.log(t)-1/(2*t); tau=t-q1
    l0=lf+a*tau; l1=l0+A0*tau**2/2
    d=logsumexp(l1)-logsumexp(l0)
    print(n,L,"lnE_a e^R=",d," L^2/n^2=",L*L/n**2," ratio",d/(L*L/n**2), "L^3/n^2=",L**3/n**2)
