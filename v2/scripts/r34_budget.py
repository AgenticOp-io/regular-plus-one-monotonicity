# Error budget: what each route gives for the *local variation* of ln P(simple) vs the target O(D/n^2).
# Local variation = difference of ln P over a perturbation of O(1) degree units (k cycle vertices).
# route -> bound on |error in ln P|, and what that implies for the variation if the error is only bounded
# (not differentiable) vs differentiable (gradient = error/n per unit change).
import math
routes = {
 "MW91 abs error D^3/n (bounded only)":       lambda D,n: D**3/n,
 "MW91 gradient-type D^3/n^2 (if smooth)":    lambda D,n: D**3/n**2,
 "Isaev-McKay sparse, next term D^2/n^2*D?":  lambda D,n: D**4/n**2,
 "single switching (r29/r31) D^3/n^2":        lambda D,n: D**3/n**2,
 "double switching, conditional on L1'":      lambda D,n: D**4/n**3,
}
target = lambda D,n: D/n**2
for name,f in routes.items():
    # largest D (scan) with f<=target, n=1e6
    n=10**6; best=0
    for D in range(1,20000):
        if f(D,n)<=target(D,n): best=D
    print(f"{name:45s} max D at n=1e6 meeting O(D/n^2): {best}")
