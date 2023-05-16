import sys

def input():
    return sys.stdin.readline().rstrip()

n,m,r=map(int,input().split())
nodes=list(map(int,input().split()))

distance=[[float("INF")] * n for _ in range(n)]
for i in range(n):
    distance[i][i]=0
dijk=[float("INF")]*n
for i in range(r):
    a,b,l=map(int,input().split())
    a-=1
    b-=1
    distance[a][b]=l
    distance[b][a]=l

for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

max_item=0
for i in range(n):
    temp_item=0
    for j in range(n):
        if(distance[i][j]<=m):
            temp_item+=nodes[j]
    max_item=max(max_item,temp_item)

print(max_item)

