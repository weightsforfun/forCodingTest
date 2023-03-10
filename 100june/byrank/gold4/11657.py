import sys
input=sys.stdin.readline
INF=int(1e9)
n,m=map(int,input().split())
flag=0
distance=[INF]*(n+1)
distance[1]=0
lines=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    lines.append((a,b,c))


for i in range(n):
    for line in lines:
        a,b,c=line
        if(distance[a]!=INF and distance[a]+c<distance[b]):
            distance[b]=distance[a]+c
            if(i==n-1):
                flag=1
if(flag):
    print(-1)
else:
    for i in range(2,n+1):
        if(distance[i]==INF):
            print(-1)
        else:
            print(distance[i])