// r14w3: exact histogram of T=|E(G1)&E(G2)|, G1,G2 iid uniform labeled L-regular on n<=11 vertices.
// G1 restricted to N(0)={1..L} (valid by simultaneous relabeling symmetry), bucketed by an isomorphism-invariant hash
// (2 refinement rounds of triangle/4-cycle/distance counts; collisions between non-iso graphs not excluded, see note).
// Output: lines "H <count_of_T=0..M>" per bucket as "B weight t0 t1 ..." . Usage: r14w3_gen L n
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64;
int L,n,M,idx[12][12],deg[12],mode; u64 N,NF; u64 *hist; 
#define MAXB 200000
u64 bh[MAXB],bw[MAXB],bm[MAXB]; int nb;
static u64 mix(u64 x){x^=x>>33;x*=0xff51afd7ed558ccdULL;x^=x>>33;x*=0xc4ceb9fe1a85ec53ULL;x^=x>>33;return x;}
static int cmp(const void*a,const void*b){u64 x=*(u64*)a,y=*(u64*)b;return x<y?-1:x>y;}
u64 ghash(u64 m){
  int A[12][12]={0},i,j,k; for(i=0;i<n;i++)for(j=i+1;j<n;j++)if(m>>idx[i][j]&1)A[i][j]=A[j][i]=1;
  u64 lab[12],nl[12],P[12]; { long W[12][12],V[12][12]; int a,b,c2;
    for(a=0;a<n;a++)for(b=0;b<n;b++)W[a][b]=A[a][b];
    for(a=0;a<n;a++)P[a]=0;
    for(int p=2;p<=8;p++){ for(a=0;a<n;a++)for(b=0;b<n;b++){long s2=0;for(c2=0;c2<n;c2++)s2+=W[a][c2]*A[c2][b];V[a][b]=s2;}
      memcpy(W,V,sizeof W); for(a=0;a<n;a++)P[a]=mix(P[a]*1000003+W[a][a]);}}
  for(i=0;i<n;i++){ int c2[12]; long tri=0,q=0; int d1=0;
    for(j=0;j<n;j++){ if(j==i)continue; int c=0; for(k=0;k<n;k++)c+=A[i][k]&A[j][k]; c2[j]=c; if(A[i][j])tri+=c; else q+=0; q+=c*(c-1)/2;}
    int dist2=0; for(j=0;j<n;j++)if(j!=i&&!A[i][j]&&c2[j])dist2++;
    lab[i]=mix(tri*1000003+q*1009+dist2+P[i]);}
  for(int r=0;r<2;r++){ for(i=0;i<n;i++){u64 s[12];int c=0; for(j=0;j<n;j++)if(A[i][j])s[c++]=lab[j]; qsort(s,c,8,cmp);
      u64 h=lab[i]; for(k=0;k<c;k++)h=mix(h*31+s[k]); 
      // also hash of non-neighbors multiset sum (distance-2 structure)
      u64 t=0; for(j=0;j<n;j++)if(j!=i&&!A[i][j])t+=mix(lab[j]); nl[i]=mix(h+t);} memcpy(lab,nl,sizeof lab);}
  qsort(lab,n,8,cmp); u64 h=7; for(i=0;i<n;i++)h=mix(h*131+lab[i]); return h;}
u64 cur; 
void leaf(u64 m){
  if(mode==0){N++; if(m&(((1ULL<<L)-1)<<0)){} // N(0)={1..L} iff edges (0,1..L) are the first L bits
    if((m&((1ULL<<(n-1))-1))==((1ULL<<L)-1)){NF++; u64 h=ghash(m); int b; for(b=0;b<nb;b++)if(bh[b]==h)break;
      if(b==nb){if(nb==MAXB){fprintf(stderr,"too many buckets\n");exit(1);} bh[nb]=h;bw[nb]=0;bm[nb]=m;nb++;} bw[b]++;}}
  else hist[__builtin_popcountll(m&cur)]++;
}
void rec(int i,u64 m){
  if(i==n){leaf(m);return;}
  int need=L-deg[i],cand[12],c=0; for(int j=i+1;j<n;j++)if(deg[j]<L)cand[c++]=j;
  if(need<0||need>c)return;
  int sel[12]; // combinations of size need from cand
  for(int k=0;k<need;k++)sel[k]=k;
  while(1){ u64 mm=m; for(int k=0;k<need;k++){deg[cand[sel[k]]]++;mm|=1ULL<<idx[i][cand[sel[k]]];}
    int old=deg[i];deg[i]=L; rec(i+1,mm); deg[i]=old;
    for(int k=0;k<need;k++)deg[cand[sel[k]]]--;
    int k=need-1; while(k>=0&&sel[k]==c-need+k)k--; if(k<0)break; sel[k]++; for(int t=k+1;t<need;t++)sel[t]=sel[t-1]+1;}
}
int main(int ac,char**av){L=atoi(av[1]);n=atoi(av[2]);M=n*(n-1)/2;int k=0;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)idx[i][j]=idx[j][i]=k++;
  hist=calloc(M+1,8); mode=0; rec(0,0);
  printf("N %llu NF %llu NB %d\n",(unsigned long long)N,(unsigned long long)NF,nb); fflush(stdout);
  mode=1; for(int b=0;b<nb;b++){cur=bm[b];memset(hist,0,(M+1)*8);rec(0,0);
    printf("B %llu",(unsigned long long)bw[b]); for(int t=0;t<=M;t++)printf(" %llu",(unsigned long long)hist[t]); printf("\n"); fflush(stdout);}
}
