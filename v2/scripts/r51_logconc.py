# r51: test (ultra-)log-concavity of N_j (host-intersection histograms) from r49 data, and Re z<=0 / Poisson-comparison
import glob,re,math,sys
for f in sorted(glob.glob('../data/r49_enum_*.txt')+glob.glob('../data/r51_enum_*.txt')):
    L=open(f).read().split('\n'); hdr=L[0]; bad=[];ubad=[];tot=0
    for l in L[1:]:
        p=l.split()
        if len(p)<3: continue
        N=list(map(int,p[1:])); tot+=1
        for j in range(1,len(N)-1):
            if N[j]**2<N[j-1]*N[j+1]: bad.append((p[0],j)); break
        # ultra: (N_j/C(k,j)) log-concave
        k=len(N)-1; M=[N[j]/math.comb(k,j) for j in range(k+1)]
        for j in range(1,k):
            if M[j]**2<M[j-1]*M[j+1]: ubad.append((p[0],j)); break
    print(hdr,'hosts',tot,'not-LC',bad[:6],'not-ULC',ubad[:6])
