import sys
INF=float("inf")
def input():
    return sys.stdin.readline()

n,m=map(int,input().split())

arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()

start=0
end=0
answer=INF
while(end<n and start<n):
    value=abs(arr[end]-arr[start])
    if(value>=m):
        answer=min(answer,value)
        start+=1
    else:
        end+=1
print(answer)