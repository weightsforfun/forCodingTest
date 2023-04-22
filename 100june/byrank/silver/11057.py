n=int(input())
dp=[[0]* 10 for _ in range(n+1)]
dp[0]=[0,0,0,0,0,0,0,0,0,0]
for i in range(1,n+1):
    for j in range(10):
        if(j==0):
            dp[i][j]=1
        else:
            dp[i][j]=(dp[i][j-1]+dp[i-1][j])%10007
print(sum(dp[n])%10007)