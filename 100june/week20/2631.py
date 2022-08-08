import sys
input=sys.stdin.readline
n=int(input())
children=[]
dp = [0 for i in range(n)]
for i in range(n):
    children.append(int(input()))
dp[0]=1
for i in range(1,n):
    a=[]
    for j in range(i):
        if children[i] > children[j]:
            a.append(dp[j])
    if not a:
        dp[i] = 1
    else:
        dp[i] = max(a) + 1
print(n-max(dp))