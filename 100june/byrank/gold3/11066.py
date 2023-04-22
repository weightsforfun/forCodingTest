t=int(input())

    
for i in range(t):
    k=int(input())
    arr=list(map(int,input().split()))
    dp=[[0]*k for _ in range(k)]
    
    for i in range(k-1):
        dp[i][i+1]=arr[i]+arr[i+1]
    
    for i in range(2,k):
        for j in range(k-i):
            target=min(dp[j+1][j+i],dp[j][j+i-1])
            
            for m in range(2,i):
                
                target=min(target,dp[j][j+i-m]+dp[j+(i+1-m)][j+i])
                
            dp[j][j+i]=target+sum(arr[j:j+i+1])
    print(dp[0][k-1])
