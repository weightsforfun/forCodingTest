import sys

n,m=map(int,sys.stdin.readline().split())

arr=[]
arr.append([-1]*(m+1))
for i in range(n):
    arr.append([-1]+list(map(int,sys.stdin.readline().split())))

for i in range(1,n+1):
    for j in range(1,m+1):
        arr[i][j]=max(arr[i-1][j-1],arr[i][j-1],arr[i-1][j],0)+arr[i][j]

print(arr[-1][-1])