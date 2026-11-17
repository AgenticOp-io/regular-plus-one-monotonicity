# fit r2(D): n^2*(R-1-r1/n) = r2 + r3/n + ... ; R=E[T]/((D-1)^3/6) from r11w1_et.cpp output files
import numpy as np, os
h=os.path.dirname(os.path.abspath(__file__))
for D,nmin_list in ((3,(40,80,120)),(4,(30,60,90))):
    a=np.loadtxt(f'{h}/r11w1_d{D}.txt'); n=a[:,0]; R=a[:,1]; r1=3*(D-1)/D
    y=n**2*(R-1-r1/n); print(f'D={D} nmax={int(n.max())}  n^2(R-1-r1/n) at n=nmax: {y[-1]:.6f}')
    for nmin in nmin_list:
        m=n>=nmin
        for deg in (3,4,5):
            X=np.vstack([n[m]**-i for i in range(deg+1)]).T; c=np.linalg.lstsq(X,y[m],rcond=None)[0]
            print(f'  nmin={nmin} deg={deg} r2={c[0]:.6f} r3={c[1]:.4f}')
    m=n>=nmin_list[1]; X=np.vstack([n[m]**-i for i in range(1,6)]).T   # free r1 too
    c=np.linalg.lstsq(X,n[m]**0*(R[m]-1),rcond=None)[0]; print(f'  free fit of R-1: r1={c[0]:.6f} (pred {r1}) r2={c[1]:.5f}')
    for nn in (6,8,10,12,16,20,24,40):
        i=np.where(n==nn)[0]
        if len(i): print(f'  finite n={nn}: n^2(R-1-r1/n)={y[i[0]]:.4f}')
