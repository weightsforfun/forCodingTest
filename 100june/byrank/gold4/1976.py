n=int(input())
m=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
    
parent=[0]*n

for i in range(n):
    parent[i]=i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def merge(u,v):
    u=find(u) 
    v=find(v)
    if(u!=v):
        if(u<v):
            parent[v]=u
        else:
            parent[u]=v

for i in range(n):
    for j in range(n):
        if(arr[i][j]==1):
            merge(i,j)

route=list(map(int,input().split()))
fail=0

for i in range(len(route)-1):
    if(parent[route[i]-1]!=parent[route[i+1]-1]):
        fail=1
        print("NO")
        break
if(not fail):
    print("YES")
    