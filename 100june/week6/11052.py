n=int(input())
cards_packs=list(map(int,input().split(" ")))

dp=[[0]*(n) for _ in range(n)]

for i in range(n):
    dp[i][0],dp[i][i]=cards_packs[i],cards_packs[i]
    
for i in range(1,n):
    for j in range(1,i+1):
        dp[i][j]=max(dp[i][j-1],dp[i-j][i-j]+dp[j-1][j-1])

print(dp[n-1][-1])