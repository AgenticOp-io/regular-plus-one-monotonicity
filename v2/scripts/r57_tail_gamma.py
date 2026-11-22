# r57: (A) tail t>2/n bound with explicit constants (checked vs exact), (B) Gamma step: exact cumulants of t=1/chi2_{n+1}, windowed ln E e^{s t} vs cumulant formula
from mpmath import mp, mpf, gammainc, log, exp, quad, gamma, e, factorial, binomial
mp.dps = 40
def q(n,k):
    r = mpf(1)
    for i in range(1,k+1): r /= (n-2*i+1)
    return r
# ---- (A) tail lemma:  T := sum_k u_k P_k,  u_k=(w m)^k q_k/k! >= M_k(|w|) q_k (M_k<=(w m)^k/k!), P_k=P(Gamma(a-k)<n/4)
# claim: for 1<=wL<=n/16:  T <= exp(-0.027 n) * e^{wL}  +  (n/2) * max(u_{n/8}, u_end)  ; we just evaluate T exactly and compare with e^{-n/40}
def tail(n, wL):
    m_w = mpf(wL)*n/2          # w*m, worst case m=nL/2
    a = mpf(n+1)/2; T = mpf(0); Z = mpf(0)
    for k in range(0, (n-1)//2+1):
        u = m_w**k*q(n,k)/factorial(k)
        Z += u
        T += u*gammainc(a-k, 0, mpf(n)/4, regularized=True)
    return T, Z
print("(A) n wL  T(exact abs tail)  e^{-n/40}  Z_abs   T<=e^{-n/40}*Z_abs?")
for n in (100, 200, 400, 800):
    for wL in (1, 4, 10):
        if wL <= n/16:
            T, Z = tail(n, wL)
            print(n, wL, float(T), float(exp(-mpf(n)/40)), float(Z), bool(T <= exp(-mpf(n)/40)*Z))
# ---- (B) exact cumulants of t: kappa_j from moments q_k
def cum(n, J):
    m = [mpf(1)]+[q(n,k) for k in range(1,J+1)]
    k = [mpf(0)]*(J+1)
    for r in range(1,J+1):
        k[r] = m[r] - sum(binomial(r-1,j-1)*k[j]*m[r-j] for j in range(1,r))
    return k
print("(B) n^3 k2/2, n^5 k3/8, n^7 k4/48 (expected -> 1 if k2~2/n^3,k3~8/n^5,k4~48/n^7)")
for n in (10**3,10**4,10**5):
    k = cum(n,4); print(n, float(k[2]*n**3/2), float(k[3]*n**5/8), float(k[4]*n**7/48))
# windowed ln E e^{s t}: density of t=1/g2, g2/2~Gamma(a); window |n t -1|<=d
def lnE_window(n, s, d):
    a = mpf(n+1)/2
    f = lambda g: exp(s/g)*(g/2)**(a-1)*exp(-g/2)/2/gamma(a)   # density of g2 times e^{s/g2}
    lo, hi = n/(1+d), n/(1-d)
    return log(quad(f, [lo, n, hi]))
print("(B) n L s  rem=lnE_win - [q1 s + k2 s^2/2 + k3 s^3/6]   rem*n^3/L^4(k4 scale) ; L^3/n^2")
for n in (10**3, 10**4, 10**5):
    for L in (5, 20):
        s = mpf(L)*n/2; d = 8*mpf(L)/mpf(n)**0.5/ (1)*0 + mpf(8)/mpf(n)**0.5*3
        k = cum(n,4); q1=q(n,1)
        r = lnE_window(n, s, d) - (q1*s + k[2]*s**2/2 + k[3]*s**3/6)
        print(n, L, float(r), "k4 s^4/24=", float(k[4]*s**4/24), " L^3/n^2=", float(mpf(L)**3/n**2))
