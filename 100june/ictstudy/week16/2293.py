import sys
input=sys.stdin.readline
n,k=map(int,input().split(" "))
coins=[]
dp=[0]*(k+1)
dp[0]=1
for i in range(n):
    coin=int(input())
    coins.append(coin)
    

for coin in coins:
    for i in range(coin,k+1):
        dp[i]+=dp[i-coin]

        

print(dp[k])
            
## dp인건 알았는데 점화식을 못구해냄 dp너무 약한듯 공부하자