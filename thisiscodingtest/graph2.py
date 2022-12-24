n,m=map(int,input().split())

arr=[0]*(n+1)

for i in range(n+1):
    arr[i]=i

def merge(a,b):
    a=find(a)
    b=find(b)
    if(a>b):
        arr[a]=b
    else:
        arr[b]=a
        
def find(x):
    if(arr[x]!=x):
        arr[x]=find(arr[x])
    return arr[x]

for i in range(m):
    i,a,b=map(int,input().split())
    if(i==0):
        merge(a,b)
    else:
        if(find(a)==find(b)):
            print("YES")
        else:
            print("NO")