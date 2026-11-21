# Largest integer D allowed by the explicit conditions of r30 note, as a function of ln n.
import math
def ok(D, ln_n):
    L = max(math.ceil(2*math.e**2*D**4), math.ceil(3*ln_n))
    lhs_a = math.log(2*(D*D+1)) + (D*D+1)*(math.log(8)+3*math.log(L+1))  # ln of ratio numerator
    a = lhs_a <= ln_n + math.log(0.5)                                     # (E3) ratio <= 1/2
    b = 5*D**4 + (3*D*D+7)*math.log(max(ln_n,2)) <= ln_n/2                # error factor <= n^(1/2)
    return a and b
for e in (3,6,10,20,50,100,300,1000,10**4,10**6,10**8):
    ln_n = e*math.log(10); D=2
    while ok(D+1, ln_n): D+=1
    print(f"n=1e{e}: max D = {D if D>=3 else 'none'}   (ln n)^(1/4)={ln_n**.25:.2f}")
