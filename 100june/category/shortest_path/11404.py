import sys

def input():
    return sys.stdin.readline()


n=int(input())
m=int(input())
INF=int(1e9)
arr=[[INF]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(i==j):
            arr[i][j]=0

for i in range(m):
    start,end,cost=map(int,input().split(" "))
    arr[start-1][end-1]=min(arr[start-1][end-1],cost)

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j]=min(arr[i][k]+arr[k][j],arr[i][j])



for i in range(n):
    for j in range(n):
        if(arr[i][j]==INF):
            print(0,end=' ')
        else:
            print(arr[i][j],end=' ')
    print()
