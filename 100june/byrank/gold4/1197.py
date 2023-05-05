import sys
import heapq
input=sys.stdin.readline
v,e=map(int,input().rstrip().split())

arr=[]
for i in range(e):
    s,e,d=map(int,input().rstrip().split())
    heapq.heappush(arr,(d,s,e))

parent=[0]*v
for i in range(v):
    parent[i]=i

def find(x):
    if(parent[x]==x):
        return x
    parent[x]=find(parent[x])
    return parent[x]

def merge(x,y):
    x=find(x)
    y=find(y)
    if(x!=y):
        if(x<y):
            parent[y]=x
        else:
            parent[x]=y
        return True
    else:
        return False

answer=0
while(arr):
    d,s,e=heapq.heappop(arr)
    if(merge(s-1,e-1)):
        answer+=d
print(answer)