def union(a,b):
    a=find(a)
    b=find(b)
    if(a>b):
        arr[b]=a
    else:
        arr[a]=b

def find(a):
    if(a!=arr[a]):
        arr[a]=find(arr[a])
    return arr[a]


n,m=map(int,input().split())
arr=[0]*(n+1)
for i in range(n+1):
    arr[i]=i

for _ in range(m):
    i,a,b=map(int,input().split())
    if(i==0):
        union(a,b)
    else:
        a=find(a)
        b=find(b)
        if(a==b):
            print("yes")
        else:
            print("no")

    