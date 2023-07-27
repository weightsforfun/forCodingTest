import sys



def input():
    return sys.stdin.readline().strip()


v,e=map(int,input().split(" "))
INF=float("inf")
arr=[[INF] * v for _ in range(v)]

for i in range(e):
    start,end,d=map(int,input().split(" "))
    arr[start-1][end-1]=d

for k in range(v):
    for i in range(v):
        for j in range(v):
            arr[i][j]=min(arr[i][k]+arr[k][j],arr[i][j])

answer=INF
for i in range(v):
    for j in range(v):
        answer=min(answer,arr[i][j]+arr[j][i])
if(answer==INF):
    print(-1)
else:
    print(answer)


