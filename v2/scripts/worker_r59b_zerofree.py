# r59b: Gamma-cumulant step via a zero-free disc + Borel-Caratheodory + Cauchy.
# t=1/g, g~chi2_{n+1}, g=2G, G~Gamma(a), a=(n+1)/2, window W={t<=2/n}={G>=n/4}.
# I(s)=E[e^{st};W] = (a^a/Gamma(a)) J(zeta),  J(zeta)=int_{y0}^inf e^{a psi(y)} dy,
# psi(y)=y-e^y+zeta e^{-y},  zeta=s/(2a^2),  y0=ln(n/(4a)).
# Saddle X*=(1+w)/2, w=sqrt(1-4zeta); psi''(y*)=-w; psi(y*)=ln X* - w;
# along y=y*+r: psi-psi* = f(r) = (r-sinh r) - w(cosh r-1)  (exact).
# Part A: explicit bound eps(a) >= |J/main-1| on |zeta|<=Z0 (proof constants), checked vs quadrature.
# Part B: remainders ln I(s)-[s m1+k2 s^2/2] (and the order-3 one) vs the proved Cauchy bound, real s; exact poly P(s).
# Part C: exact cumulants kappa_j(t) (from q_k) vs the proved j! M (2/R)^j.
# Part D: two-parameter step  ln E[e^{c1 t+c2 t^2};W] - [c1 q1 + c2 q2 + k2 c1^2/2]  vs L^3/n^2.
# Part E: actual nearest zero of I(s) for moderate n (zero-free radius is not tight).
from mpmath import mp, mpf, mpc, sqrt, log, exp, quad, gamma, gammainc, pi, cosh, sinh, cos, asin, atan, sin, inf, fabs, factorial, binomial, arg, findroot, loggamma
mp.dps = 20
Z0 = mpf('0.02'); NMIN = 20

# ---------------- Part A: proof constants ----------------
rho = 4*Z0
wabs_max = sqrt(1+rho)
argw_max = asin(rho)/2
rew_min = sqrt(1-rho)*cos(argw_max)
imw_max = wabs_max*sin(argw_max)
eta_max = atan(imw_max/(1+rew_min))           # |arg X*|
x0min = mpf(NMIN)/(2*(NMIN+1))
lnX_max = log((1+wabs_max)/2); lnX_min = log((1+rew_min)/2)
rmin_abs_max = lnX_max - log(x0min)            # |r_min| <= this
rmin_abs_min = lnX_min + log(2)                # |r_min| >= this (x0<1/2)
u = rmin_abs_max
rho_u = (sinh(u)-u)/(cosh(u)-1)                # (sinh u-u)/(cosh u-1) increasing
c = rew_min - rho_u
Delta = lnX_min - wabs_max - (log(mpf(1)/2) - cos(eta_max)/2) - Z0/x0min
print("A: Z0=%s  Re w>=%.4f |w|<=%.4f |eta*|<=%.4f  |rmin| in [%.3f,%.3f]  rho(u)=%.4f  c=%.4f  Delta=%.4f" %
      (Z0, rew_min, wabs_max, eta_max, rmin_abs_min, rmin_abs_max, rho_u, c, Delta))
assert c > 0 and Delta > 0
def eps_bound(a):
    a = mpf(a); beta = a*c-1
    EH1 = a*(mpf(2)/(3*beta**2) + wabs_max*sqrt(2*pi)/(8*beta**mpf(2.5)))
    EH2 = sqrt(pi/(2*a*rew_min))*exp(-a*rew_min*rmin_abs_min**2/2)
    EV = eta_max*exp(-a*Delta)
    return sqrt(a*wabs_max/(2*pi))*(EH1+EH2+EV)
for a in (10, 15, 20, 30, 50, 100, 1000):
    print("   a=%5d eps_bound=%.4f" % (a, eps_bound(a)))
# smallest n>=NMIN with eps<=1/2 for all larger a (eps_bound decreasing)
n0 = NMIN
while eps_bound(mpf(n0+1)/2) > 0.5: n0 += 1
print("   eps_bound<=1/2 for all n>=%d" % n0)

def psi(y, z): return y - exp(y) + z*exp(-y)
def saddle(z):
    w = sqrt(1-4*z); X = (1+w)/2; return w, X, log(X)
def J_rel(n, z):
    """J e^{-a psi*} / sqrt(2pi/(a w))  computed by quadrature on the REAL line (independent of the proof contour)."""
    a = mpf(n+1)/2; y0 = log(mpf(n)/(4*a)); w, X, ys = saddle(z); ps = log(X) - w
    f = lambda y: exp(a*(psi(y, z) - ps))
    h = 1/sqrt(a)
    pts = [y0] + [ys.real + k*h for k in range(-12, 13) if ys.real + k*h > y0] + [ys.real+3]
    return quad(f, pts)/sqrt(2*pi/(a*w))
import sys
PARTS=sys.argv[1] if len(sys.argv)>1 else 'ABCDE'
if 'A' in PARTS: print("A-check: max over |zeta|=Z0 (24 pts) of |J/main-1| (quadrature) vs eps_bound, and the same at |zeta|=Z0/2")
for n in ((21, 101) if 'A' in PARTS else ()):
    a = mpf(n+1)/2
    m1 = max(fabs(J_rel(n, Z0*exp(2j*pi*k/8)) - 1) for k in range(8))
    m2 = max(fabs(J_rel(n, Z0/2*exp(2j*pi*k/8)) - 1) for k in range(8))
    print("   n=%5d  actual=%.4e (half-radius %.4e)  bound=%.4e  ok=%s  actual*sqrt(a)=%.3f" % (n, m1, m2, eps_bound(a), m1 <= eps_bound(a), m1*sqrt(a)))

# ---------------- Part B: remainders for real s ----------------
def q(n, k):
    r = mpf(1)
    for i in range(1, k+1): r /= (n-2*i+1)
    return r
def cums(n, J):
    m = [mpf(1)] + [q(n, k) for k in range(1, J+1)]; k = [mpf(0)]*(J+1)
    for r in range(1, J+1): k[r] = m[r] - sum(binomial(r-1, j-1)*k[j]*m[r-j] for j in range(1, r))
    return k
def lnI(n, s):   # ln E[e^{st}; t<=2/n], real s, quadrature in y
    a = mpf(n+1)/2; y0 = log(mpf(n)/(4*a)); z = mpf(s)/(2*a**2)
    w, X, ys = saddle(z); ps = log(X) - w
    h = 1/sqrt(a); pts = [y0] + [ys + k*h for k in range(-12, 13) if ys + k*h > y0] + [ys+3]
    return a*log(a) - loggamma(a) + a*ps + log(quad(lambda y: exp(a*(psi(y, z) - ps)), pts))
def lnP(n, s):   # exact polynomial  sum_{k<=(n-1)/2} q_k s^k/k!
    return log(sum(q(n, k)*mpf(s)**k/factorial(k) for k in range(0, (n-1)//2+1)))
def proved(n, s, K):
    # |F - T_K| <= M (rho/r1)^{K+1}/(1-rho/r1), r1=R/2, M=4R/n, R=2 a^2 Z0  (for the windowed F)
    a = mpf(n+1)/2; R = 2*a**2*Z0; r1 = R/2; M = 4*R/n; x = fabs(s)/r1
    return M*x**(K+1)/(1-x) if x < 1 else inf
if PARTS=='A': sys.exit()
print("B: real s=+-n*L/2. remK = ln E[e^{st};W]-ln P(W) - sum_{j<=K} k_j s^j/j!  (exact k_j of t). Bound = proved Cauchy bound (window k_j differ by e^{-cn}).")
print("    n    L   sign  rem2*n^2/L^3  k3s^3/6*n^2/L^3  rem3/(k4 s^4/24)  bound2*n^2/L^3  ok   |lnP-lnI|")
for n in (201, 801, 3201):
    k = cums(n, 4); a = mpf(n+1)/2
    lnPW = log(gammainc(a, mpf(n)/4, inf, regularized=True))
    for L in (2, 10):
        for sg in (1, -1):
            s = sg*mpf(n)*L/2
            if fabs(s) >= a**2*Z0: continue
            F = lnI(n, s) - lnPW
            r2 = F - (k[1]*s + k[2]*s**2/2); r3 = r2 - k[3]*s**3/6
            b2 = proved(n, s, 2)
            dP = fabs(lnP(n, s) - lnI(n, s)) if n <= 3201 else mpf(0)
            sc = mpf(n)**2/L**3
            print("  %5d %4d  %+d   %12.5f  %12.5f  %12.5f  %14.1f  %s  %.1e" % (n, L, sg, r2*sc, k[3]*s**3/6*sc, r3/(k[4]*s**4/24), b2*sc, fabs(r2) <= b2, dP))

# ---------------- Part C: cumulant bounds ----------------
print("C: exact kappa_j(t) vs proved |kappa_j^W| <= j! M (2/R)^j ; also n^{2j-1} kappa_j / (2^{j-1}(j-1)! Cat_{j-1})")
from math import comb
for n in (401, 4001):
    a = mpf(n+1)/2; R = 2*a**2*Z0; M = 4*R/n; k = cums(n, 12)
    for j in range(2, 13):
        cat = comb(2*(j-1), j-1)//j
        print("   n=%d j=%2d kappa=%.4e bound=%.4e ratio=%.2e  normalized=%.4f" % (n, j, k[j], factorial(j)*M*(2/R)**j, k[j]/(factorial(j)*M*(2/R)**j), k[j]*mpf(n)**(2*j-1)/(2**(j-1)*factorial(j-1)*cat)))

# ---------------- Part D: two-parameter step ----------------
print("D: rem = ln E[e^{c1 t + c2 t^2};W]-ln P(W) - [c1 q1 + c2 q2 + k2 c1^2/2],  c1=n L/2, c2=-n L^2/4 (sizes of r55)")
def lnI2(n, c1, c2):
    a = mpf(n+1)/2; G0 = mpf(n)/4
    f = lambda G: exp(c1/(2*G) + c2/(4*G**2) + (a-1)*log(G) - G - (a-1)*log(a) + a)
    return log(quad(f, [G0, a-3*sqrt(a), a, a+3*sqrt(a), a+25*sqrt(a)])) + (a-1)*log(a) - a - loggamma(a)
for n in (401, 1601):
    k = cums(n, 2); a = mpf(n+1)/2; lnPW = log(gammainc(a, mpf(n)/4, inf, regularized=True)); q1, q2 = q(n, 1), q(n, 2)
    for L in (3, 10, 20):
        c1 = mpf(n)*L/2; c2 = -mpf(n)*L**2/4
        rem = lnI2(n, c1, c2) - lnPW - (c1*q1 + c2*q2 + k[2]*c1**2/2)
        print("   n=%5d L=%3d rem*n^2/L^3=%.5f" % (n, L, rem*mpf(n)**2/L**3))

# ---------------- Part E: nearest zero of I ----------------
print("E: zero of J(zeta) nearest 0 (Newton from several starts on the imaginary-ish directions); proved zero-free radius Z0=%s" % Z0)
def Jfull(n, z):   # J e^{-a psi*(0)}... plain J up to the constant, real-line quadrature (oscillatory, high dps)
    a = mpf(n+1)/2; y0 = log(mpf(n)/(4*a))
    return quad(lambda y: exp(a*(psi(y, z) + 1)), [y0, y0/2, -0.2, 0, 0.2, 0.6, 1.5, inf])
for n in ((21,) if 'E' in PARTS else ()):
    best = None
    for st in (mpc(0.2, 0.3), mpc(0.0, 0.4), mpc(-0.2, 0.4), mpc(0.3, 0.1), mpc(0.25, 0.0)):
        try:
            z = findroot(lambda z: Jfull(n, z), st)
            if fabs(Jfull(n, z)) < mpf(10)**-20 and (best is None or fabs(z) < fabs(best)): best = z
        except Exception:
            pass
    print("   n=%d nearest zero found: %s  |zeta|=%s" % (n, best, fabs(best) if best is not None else None))
