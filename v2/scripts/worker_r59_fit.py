# fit a(n)=n^2 err/2 = a0+a1/n+a2/n^2+... by least squares on exact data files
import re,sys,numpy as np,glob,os
base=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','notes')
for D in (3,4,5,6):
    rows=[l.split() for l in open(os.path.join(base,f'r59_D{D}.txt')) if re.match(r'^\d+ ',l)]
    n=np.array([float(r[0]) for r in rows]);a=np.array([float(r[3].split('=')[1]) for r in rows])
    m=n>=20
    for k in (2,3,4):
        if m.sum()>k:
            A=np.vander(1/n[m],k+1,increasing=True);c=np.linalg.lstsq(A,a[m],rcond=None)[0]
            print(D,k,np.round(c,4))
print("constrained test: a0=-(13D-1)/24, fit remaining 2 terms; rms resid vs unconstrained-free a0 +-0.03")
for D in (3,4,5,6):
    rows=[l.split() for l in open(os.path.join(base,f'r59_D{D}.txt')) if re.match(r'^\d+ ',l)]
    n=np.array([float(r[0]) for r in rows]);a=np.array([float(r[3].split('=')[1]) for r in rows]);m=n>=20
    for a0 in (-(13*D-1)/24-0.03,-(13*D-1)/24,-(13*D-1)/24+0.03):
        A=np.vander(1/n[m],3,increasing=True)[:,1:];c,res,*_=np.linalg.lstsq(A,a[m]-a0,rcond=None)
        print(D,round(a0,4),np.round(c,2),"rms",np.sqrt(np.mean((A@c-(a[m]-a0))**2)))
