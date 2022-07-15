n=int(input())
dp=[0]*1001

dp[1]=1
dp[2]=3
dp[3]=5
dp[4]=11
for i in range(5,n+1):
    dp[i]=((5*dp[i-2])-dp[i-4]*4)%10007

print(dp[n])