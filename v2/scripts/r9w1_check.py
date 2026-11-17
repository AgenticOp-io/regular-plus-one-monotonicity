"""r9w1: (1) verify kappa3(G0)-kappa3(G0') = -48 p^3 q^3 (t0-t0') exactly (rational) vs brute force, n=6,8,10; Var formula vs brute.
(2) scale table for E3 = (c^3/6)*Delta kappa3 = (2 c p q)^3 * Delta t0 at the two candidate tilt scales."""
import math
from fractions import Fraction as F
from r9w1_k3 import *
cyc = lambda off, k: [(off+i, off+(i+1) % k) for i in range(k)]
kk = lambda off, k: [(off+a, off+b) for a in range(k) for b in range(a+1, k)]
q3 = [(a, b) for a in range(8) for b in range(a+1, 8) if bin(a ^ b).count("1") == 1]
fam = [(6, 1, [("C6", cyc(0,6)), ("2xK3", cyc(0,3)+cyc(3,3))]),
       (8, 3, [("Q3", q3), ("2xK4", kk(0,4)+kk(4,4))]),
       (10, 6, [(nm, comp_edges(10, sum([cyc(o, k) for o, k in zip([0,3,5,7][:len(ps)], ps)], []) if False else
                 [e for part, off in zip(ps, [sum(ps[:i]) for i in range(len(ps))]) for e in cyc(off, part)]))
                for nm, ps in [("H=C10", [10]), ("H=C5+C5", [5,5]), ("H=C3+C7", [3,7]), ("H=C4+C6", [4,6]), ("H=C3+C3+C4", [3,3,4])]])]
def var_formula(n, d, p, w1):   # H d-regular, S = w1*|E_X| + 2*P2(X)
    q = 1-p; m = F(n*d, 2); ch = n*d*(d-1)//2
    vE = m*p*q; cov = ch*2*p*p*q; vP = ch*(p*p-p**4) + m*2*(d-1)*(2*d-3)*p**3*q
    return w1*w1*vE + 4*w1*cov + 4*vP
for n, D, gs in fam:
    t_ref = None
    for p in [F(3,10), F(1,2)]:
        q = 1-p; w1 = 2+4*D; res = []
        for nm, E0 in gs:
            k3 = eval_poly(kappa3_poly(n, E0), w1, p); t0, _ = counts(n, E0); res.append((nm, t0, k3))
        for nm, t0, k3 in res[1:]:
            assert k3 - res[0][2] == -48*p**3*q**3*(t0 - res[0][1]), (nm, p)
        print(f"n={n} D={D} p={p}: Delta k3 == -48p^3q^3 Delta t0 for {[r[0] for r in res]} (t0={[r[1] for r in res]}) exact")
# variance formula vs brute (n=8, D=3 -> d=4)
E0 = q3; H = comp_edges(8, E0); p = F(3,10)
H_ = H; m = len(H_); tot = {}
mu = 0; m2 = 0
import itertools
for mask in range(1 << m):
    r = [0]*8; k = 0
    for i, (a, b) in enumerate(H_):
        if mask >> i & 1: r[a] += 1; r[b] += 1; k += 1
    S = sum((3+x)**2 for x in r); pr = p**k*(1-p)**(m-k); mu += S*pr; m2 += S*S*pr
assert m2-mu*mu == var_formula(8, 4, p, 14), (m2-mu*mu, var_formula(8, 4, p, 14))   # w1=2+4D=14 (S-const irrelevant)
print("Var(S) closed form == brute (n=8,D=3,p=.3) exact")
print("\nScale table: |E3| = (2 c p q)^3 |dt0|, dt0 = D^{3/2} (typical) and n D^2/6 (worst case)")
print("A: c=beta/(2(n*hbar-1)), beta=D/(3 hbar^2) [r6 params]; B: c=sqrt(K)/sd(S), K=n/1550 [r6 fit hbar=12,D=9]")
for n in [10**3, 10**4, 10**6]:
    D, hbar = 9, 12; p = (hbar-D)/(n-1-D); q = 1-p; d = n-1-D
    beta = D/(3*hbar**2); cA = beta/(2*(n*hbar-1))
    sd = math.sqrt(float(var_formula(n, d, F(p), 2+4*D))); cB = math.sqrt(n/1550)/sd
    for nm, c in [("A", cA), ("B", cB)]:
        print(f"n={n:8d} {nm}: c={c:.3e} c*sd(S)={c*sd:.3g}  E3 typ={(2*c*p*q)**3*D**1.5:.3e}  E3 worst={(2*c*p*q)**3*n*D*D/6:.3e}")
print("dense p=0.3, D=9, K=D^2/9 fixed:")
for n in [10**2, 10**3, 10**4]:
    D = 9; p = .3; q = .7; d = n-1-D; sd = math.sqrt(float(var_formula(n, d, F(3,10), 2+4*D))); c = math.sqrt(D*D/9)/sd
    print(f"n={n:6d} c={c:.3e} E3 typ={(2*c*p*q)**3*D**1.5:.3e} worst={(2*c*p*q)**3*n*D*D/6:.3e}")
print("OK")
