n=int(input())

arr=list(map(int,input().split()))

dp=arr[:]
dp[0]=arr[0]
for i in range(n):
    for j in range(i):
        if(arr[i]>arr[j]):
            dp[i]=max(dp[j]+arr[i],dp[i])

print(max(dp))