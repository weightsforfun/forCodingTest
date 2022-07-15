n=int(input())
value=list(map(int,input().split(" ")))
dp=[10001]*(n+1)

for i in range(len(value)):
    dp[i+1]=value[i]

for i in range(1,n+1):
    for j in range(1,i):
        dp[i]=min(dp[i],dp[j]+dp[i-j])

print(dp[n])