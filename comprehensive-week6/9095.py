n=int(input())
dp=[0]*10
dp[0]=1
dp[1]=2
dp[2]=4

for i in range(3,10):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for i in range(n):
    k=(int(input()))
    print(dp[k-1])


