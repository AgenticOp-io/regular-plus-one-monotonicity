# r44: check psi(k)=phi(k)-k^2/n <= 0.75 k^3/n^2 for k<=n/10 (phi(k)=-sum_{i<k}ln(1-(2i+1)/n)); numerics only
import numpy as np
for n in (10**3, 10**4, 10**6):
    k = np.arange(1, n//10 + 1)
    phi = np.cumsum(-np.log1p(-(2*(k-1)+1)/n))
    r = (phi - k**2/n) / (k**3/n**2)
    print(n, r.min(), r.max())
    assert r.max() <= 0.75
