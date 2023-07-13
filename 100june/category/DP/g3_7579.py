n,m=map(int,input().split(" "))


mem=list(map(int,input().split(" ")))

cost=list(map(int,input().split(" ")))

total_cost=sum(cost)

dp=[[0]*(total_cost+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,total_cost+1):
        if(cost[i-1]<=j):
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-cost[i-1]]+mem[i-1])
        else:
            dp[i][j]=dp[i-1][j]
           

answer=total_cost

for i in range(total_cost+1):
    if(dp[-1][i]>=m):
        answer=min(answer,i)

print(answer)
