import sys
def input():
    return sys.stdin.readline().rstrip()

n,k=map(int,input().split())
arr=list(map(int,input().split()))

diff=[]
for i in range(n-1):
    diff.append(arr[i+1]-arr[i])

diff.sort()

for i in range(n-k):
    diff.pop()

print(sum(diff))