n=int(input())
arr=[]
dp=[0]*1000001
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(n):
    num=int(input())
    arr.append(num)
for i in range(4,max(arr)+1):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009

for i in arr:
    print(dp[i])


