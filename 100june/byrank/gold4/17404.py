import sys
input=sys.stdin.readline
INF=100000000
n=int(input().rstrip())
arr=[]
dp=[[0]*3 for _ in range(n)]
answer=INF
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(3):
    
    for j in range(3):
        dp[0][j]=INF
    
    dp[0][i]=arr[0][i]
    
    for j in range(1,n):
        dp[j][0]=min(dp[j-1][1],dp[j-1][2])+arr[j][0]
        dp[j][1]=min(dp[j-1][0],dp[j-1][2])+arr[j][1]
        dp[j][2]=min(dp[j-1][0],dp[j-1][1])+arr[j][2]
    
    for j in range(3):
        if(j!=i):
            answer=min(answer,dp[n-1][j])
print(answer)
    

