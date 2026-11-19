# fit n*c = a + b/n + c2/n^2 on the largest points of r21a_out_D*.txt; compare a with (D-2)/D
import numpy as np,glob,re
for D in (3,4,5,6):
    try: rows=[(int(l.split()[1]),float(l.split('n*c=')[1].split()[0])) for l in open(f'r21a_out_D{D}.txt') if 'n*c=' in l]
    except OSError: continue
    for k in (2,3):
        r=[x for x in rows if x[0]>=20][-4:] if k==3 else rows[-3:]
        if len(r)<k+1: continue
        n=np.array([x[0] for x in r],float); y=np.array([x[1] for x in r])
        A=np.vander(1/n,k+1,increasing=True); s=np.linalg.lstsq(A,y,rcond=None)[0]
        print(f'D={D} order{k} pts n={r[0][0]}..{r[-1][0]}: a={s[0]:.4f} b={s[1]:.3f}  pred={(D-2)/D:.4f}')
