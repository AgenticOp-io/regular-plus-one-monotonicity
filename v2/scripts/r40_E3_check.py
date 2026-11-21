# r40: numeric checks for the sharpened E3 (true fresh weight w=(D^2-1)/4, bundle-level free-site accounting).
import math, random

def w_of(D): return (D*D-1)/4

# (a) exact fresh weights vs lam1, lam2 (D-regular, N=Dn): E X, E Y
def exact_means(n, D):
    N = D*n
    EX = n*math.comb(D, 2)/(N-1)
    EY = math.comb(n, 2)*math.comb(D, 2)**2*2/((N-1)*(N-3))
    return EX, EY

# (b) Monte Carlo E[(X+Y)_l] vs 2 w^l (the E3 bound at leading order)
def mc(n, D, reps, lmax=4, seed=1):
    rnd = random.Random(seed); N = n*D
    pts = [i//D for i in range(N)]
    acc = [0.0]*(lmax+1)
    for _ in range(reps):
        p = pts[:]; rnd.shuffle(p)
        X = 0; cnt = {}
        for i in range(0, N, 2):
            a, b = p[i], p[i+1]
            if a == b: X += 1
            else:
                k = (a, b) if a < b else (b, a)
                cnt[k] = cnt.get(k, 0) + 1
        Y = sum(c*(c-1)//2 for c in cnt.values())  # unordered pairs of parallel pairs
        T = X+Y; f = 1.0
        for l in range(1, lmax+1):
            f *= max(T-l+1, 0); acc[l] += f
    return [a/reps for a in acc]

# (c) admissible D under the new conditions vs r30
def lnrho(D, L):
    l = L+1
    return math.log(2)+3*math.log(l)+2*math.log(D)+D*(math.log(D)+2*math.log(l))

def ok_new(D, ln_n):
    w = w_of(D); L = max(math.ceil(math.e**2*w), math.ceil(3*ln_n))
    g1 = lnrho(D, L) <= ln_n-math.log(2)                 # rho/n <= 1/2
    err = 2*w + 2*lnrho(D, L) + math.log(200) <= ln_n/2   # e^{2w} rho^2 * C <= n^{1/2}
    return g1 and err

def ok_old(D, ln_n):
    L = max(math.ceil(2*math.e**2*D**4), math.ceil(3*ln_n))
    a = math.log(2*(D*D+1))+(D*D+1)*(math.log(8)+3*math.log(L+1)) <= ln_n-math.log(2)
    return a and 5*D**4+(3*D*D+7)*math.log(max(ln_n, 2)) <= ln_n/2

if __name__ == "__main__":
    for D in (3, 4, 6):
        EX, EY = exact_means(10**4, D); lam1, lam2 = (D-1)/2, (D-1)**2/4
        assert abs(EX-lam1) < 1e-3*lam1 and abs(EY-lam2) < 1e-3*lam2
        assert abs(lam1+lam2-w_of(D)) < 1e-12
    print("exact fresh weights = lam1, lam2, sum = (D^2-1)/4: OK")
    # free-site count: sum_i C(b_i,2) <= (D-1)m/2 and per-n-cost ratio C(b,2)/(b-2) <= D
    for D in range(3, 200):
        assert max(math.comb(b, 2)/(b-2) for b in range(3, D+1)) <= D
    print("C(b,2)/(b-2) <= D for 3<=b<=D<200: OK")
    for D, n in ((3, 400), (4, 400), (6, 400)):
        m = mc(n, D, 40000); w = w_of(D)
        print(f"D={D} n={n} w={w:.2f}  E(T)_l/w^l:", [round(m[l]/w**l, 3) for l in range(1, 5)], "(bound: <= 2(1+R_l))")
        assert all(m[l] <= 2*w**l*(1+10*l**3*D**2/n) for l in range(1, 5))
    print(f"{'ln n':>9} {'D_old(r30)':>11} {'D_new':>7} {'sqrt(ln n)':>11}")
    for e in (3, 10, 100, 1000, 10**4, 10**5, 10**6, 10**8):
        ln_n = e*math.log(10)
        out = []
        for ok in (ok_old, ok_new):
            D = 2
            while ok(D+1, ln_n): D += 1
            out.append(D if D >= 3 else None)
        print(f"{ln_n:9.0f} {str(out[0]):>11} {str(out[1]):>7} {ln_n**.5:11.1f}")
