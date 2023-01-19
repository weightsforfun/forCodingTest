import sys

n,k=map(int,sys.stdin.readline().split())

length=len(str(n))
total=0
answer=0
k_length=0
short=1
prev=0
for i in range(1,length+1):
    counts=9*i*(10**(i-1))
    total+=counts
    if(k<=total):
        prev=total-counts
        k_length=i-1
        sur=(n-((10**k_length)-1 if k_length else 0))*i
        if(k<=prev+sur):
            short=0
        break

if(short):
    print(-1)
else:
    answer=(((k-prev-1) if prev else k )//(k_length+1))+(10**k_length if k_length  else 0)
    print(str(answer)[(k-prev-1)%(k_length+1)])
    



