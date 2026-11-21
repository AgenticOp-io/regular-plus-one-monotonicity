// r49: exact histogram N_j=#{simple D-regular G on [n] : |E(G)∩H|=j} for cycle/path hosts. usage: r49_enum n D
#include <stdio.h>
#include <stdlib.h>
#define MX 12
int n,D,E,eu[80],ev[80],deg[MX],nh,hl[40],hid[40][80];
char hname[40][16]; long long hist[40][MX+2]; int cnt[40]; long long total=0;
void rec(int i){
  if(i==E){ for(int x=0;x<n;x++) if(deg[x]!=D) return; total++; for(int h=0;h<nh;h++) hist[h][cnt[h]]++; return; }
  int u=eu[i],v=ev[i];
  if(deg[u]<D&&deg[v]<D){ deg[u]++;deg[v]++;
    if(v<n-1||deg[u]==D){ for(int h=0;h<nh;h++)cnt[h]+=hid[h][i]; rec(i+1); for(int h=0;h<nh;h++)cnt[h]-=hid[h][i]; }
    deg[u]--;deg[v]--; }
  if(deg[u]+(n-1-v)>=D && (v<n-1||deg[u]==D)) rec(i+1);
}
int eid(int a,int b){ if(a>b){int t=a;a=b;b=t;} for(int i=0;i<E;i++) if(eu[i]==a&&ev[i]==b) return i; return -1; }
int main(int c,char**a){ n=atoi(a[1]);D=atoi(a[2]);
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++){eu[E]=u;ev[E]=v;E++;}
  for(int k=3;k<=n;k++){ sprintf(hname[nh],"cyc%d",k); for(int i=0;i<k;i++) hid[nh][eid(i,(i+1)%k)]=1; hl[nh++]=k; }
  for(int k=2;k<=n-1;k++){ sprintf(hname[nh],"path%d",k); for(int i=0;i<k;i++) hid[nh][eid(i,i+1)]=1; hl[nh++]=k; }
  rec(0); printf("n %d D %d total %lld\n",n,D,total);
  for(int h=0;h<nh;h++){ printf("%s",hname[h]); for(int j=0;j<=hl[h];j++) printf(" %lld",hist[h][j]); printf("\n"); }
}
