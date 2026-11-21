# phi(k)=ln(n^k q_k)=-sum_{i<k} ln(1-(2i+1)/n); compare k^2/n; remainder ~ 2k^3/(3n^2)?
from math import log
for n in (10**4,10**6):
  for k in (10,100,1000):
    if k>n//4: continue
    phi=-sum(log(1-(2*i+1)/n) for i in range(k)); r=phi-k*k/n
    print(n,k,phi,k*k/n,r,r/(2*k**3/(3*n*n)))
