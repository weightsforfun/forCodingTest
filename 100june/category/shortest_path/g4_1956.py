import sys


answer=4000000
def input():
    return sys.stdin.readline().strip()

def dfs(arr,index,cost,prefix):
    global answer
    global visited
    for i in range(len(arr)):
        if(i==index):
            continue
        if(arr[index][i]!=INF and prefix[i]==0):
            visited[i]=1
            prefix[i]+=arr[index][i]
            dfs(arr,i,cost+arr[index][i],prefix)
            prefix[i]-=arr[index][i]
        elif(arr[index][i]!=INF and prefix[i]>0):
            answer=min(answer,cost+arr[index][i]-prefix[i])
    return 

v,e=map(int,input().split(" "))
INF=float(10**9)
arr=[[INF] * v for _ in range(v)]

for i in range(e):
    start,end,d=map(int,input().split(" "))
    arr[start-1][end-1]=d

for k in range(v):
    for i in range(v):
        for j in range(v):
            if(i==j):
                arr[i][j]=0
            else:
                arr[i][j]=min(arr[i][k]+arr[k][j],arr[i][j])

visited=[0]*v
prefix=[0]*v
for i in range(v):
    if(visited[i]==0):
        visited[i]=1
        dfs(arr,i,0,prefix)
print(answer)
                    


