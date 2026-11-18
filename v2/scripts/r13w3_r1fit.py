# r13w3: D=4,5 check of r1=3(D-1)/D from exact E[T] (R=E[T]/((D-1)^3/6)) in G(n,D); data from r13w3_et.exe (= r11w1_et.cpp)
import numpy as np, os
h=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','notes','r13w3_data')
for D in (4,):  # D=5 impossible: r11w1_et.cpp uses array<int,5> (needs D<=4)
    a=np.loadtxt(f'{h}/et_d{D}.txt'); n=a[:,0]; R=a[:,1]; r1=3*(D-1)/D
    for nmin in (30,50,80):
        m=n>=nmin
        if m.sum()<8: continue
        for deg in (4,5,6):
            X=np.vstack([n[m]**-i for i in range(1,deg+1)]).T; c=np.linalg.lstsq(X,R[m]-1,rcond=None)[0]
            print(f'D={D} nmax={int(n.max())} nmin={nmin} free-fit deg={deg}: r1={c[0]:.5f} (pred {r1:.5f}) r2={c[1]:.4f}')
