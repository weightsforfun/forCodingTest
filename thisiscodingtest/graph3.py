import heapq
n,m=map(int,input().split())
heap=[]
arr=[0]*(n+1)
answer=0
last=0
for i in range(1,n+1):
    arr[i]=i

def find_parent(arr,x):
    if(arr[x]!=x):
        arr[x]=find_parent(arr,arr[x])
    return arr[x]

def merge(arr,a,b):
    a=find_parent(arr,a)
    b=find_parent(arr,b)
    if(a!=b):
        if(a>b):
            arr[a]=b
        else:
            arr[b]=a
        return True
    else:
        return False

for i in range(m):
    a,b,c=map(int,input().split())
    heapq.heappush(heap,[c,a,b])

while(heap):
    cost,a,b=heapq.heappop(heap)
    if(merge(arr,a,b)):
        answer+=cost
        last=cost
    
print(answer-last)
    
    