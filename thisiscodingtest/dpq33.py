n=int(input())

arr=[]

dp=[0]*(n+1)

for i in range(n):
    day,pay=map(int,input().split())
    arr.append([day,pay])

for i in range(n):
    if(i+arr[i][0]<=n):
        dp[i+arr[i][0]]=max(max(dp[:i+1])+arr[i][1],dp[i+arr[i][0]])
    print(i,dp)
