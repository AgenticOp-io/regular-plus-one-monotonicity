"""Mean-field McKay exponent of E[Z^2]/E[Z]^2 for a NON-regular host h_v (cells of h_v points), factor degree L.
Psi = E1+E2+E3+E4 - lam(h)-lam(h)^2 - 2*E0, class sums -> per-cell hypergeometric means (as Lemma mckay-exponent).
Regular case must give -x/2-x^2/4, x=1/(h-1)."""
from fractions import Fraction as Fr
import random, math

def lam(g): return Fr(sum(x*(x-1) for x in g), 2*sum(g))
def cell(h, L):  # per-cell means for a ~ |A∩B|, A,B random L-subsets of h points
    q = Fr(L*L, h); a2 = q + Fr((L*(L-1))**2, h*(h-1))      # E a, E a^2
    return q, a2
def psi(hs, L):
    n = len(hs); S = lambda f: sum(f(*cell(h, L), h) for h in hs)
    Sa = S(lambda q, a2, h: q); Sa2 = S(lambda q, a2, h: a2)
    Sc = n*L - Sa                                   # sum (L-a)
    Sc2 = S(lambda q, a2, h: L*L - 2*L*q + a2)      # sum (L-a)^2
    Sg = S(lambda q, a2, h: h-2*L+q)
    Sg2 = S(lambda q, a2, h: (h-2*L)**2 + 2*(h-2*L)*q + a2)
    Sag = S(lambda q, a2, h: (h-2*L)*q + a2)        # sum a*g
    Scg = S(lambda q, a2, h: (L*(h-2*L)) + L*q - (h-2*L)*q - a2)  # sum (L-a)*g
    Sac = L*Sa - Sa2                                # sum a(L-a)
    lB = (Sa2-Sa)/(2*Sa); l1 = (Sc2-Sc)/(2*Sc); lg = (Sg2-Sg)/(2*Sg)
    E1 = -lB-lB**2
    E2 = -l1-l1**2 - Sac**2/(2*Sa)/Sc
    E3 = -l1-l1**2 - (Sac**2/(2*Sa) + Sc2**2/(2*Sc))/Sc
    E4 = -lg-lg**2 - (Sag**2/(2*Sa) + Scg**2/Sc)/Sg
    gp = [h-L for h in hs]; Sgp = sum(gp)
    E0 = -(L*L-1)/Fr(4) - lam(gp)-lam(gp)**2 - Fr(L*Sgp, 2*n)
    h = lam(hs)
    return E1+E2+E3+E4 - h - h**2 - 2*E0
if __name__ == "__main__":
    for h, L in [(20, 3), (50, 4), (200, 6)]:
        x = Fr(1, h-1); r = psi([h]*10, L)
        print("regular", h, L, float(r), float(-x/2-x*x/4)); assert r == -x/2-x*x/4
    random.seed(1)
    for h, L, n in [(60, 3, 2000), (200, 5, 2000), (800, 6, 2000)]:
        for c in (0.5, 1.0, 2.0):             # degree std = c*sqrt(h)  (conditioned G(n,p) host: c~1)
            ys = [round(random.gauss(0, c*math.sqrt(h))) for _ in range(n)]
            ys[0] -= sum(ys)
            hs = [h+y for y in ys]; V = sum(y*y for y in ys)/n
            d = float(psi(hs, L) - psi([h]*n, L)) 
            print(f"h={h} L={L} var/h={V/h:.2f}  Psi(y)-Psi(0)={d:+.3e}   (1/h)^2={1/h**2:.1e}  V/h^3={V/h**3:.1e}")
