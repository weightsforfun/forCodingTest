n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

dp=[1000001]*(k+1)
dp[0]=0
arr.sort()

for i in range(1,k+1):
    for j in range(n):
        if(i-arr[j]>=0):
            dp[i]=min(dp[i],dp[i-arr[j]]+1)
        else:
            break
if(dp[k]==1000001):
    print(-1)
else:
    print(dp[k])
