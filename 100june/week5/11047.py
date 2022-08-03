n,k=map(int,input().split(" "))
coins=[]
for i in range(n):
    coin=int(input())
    coins.append(coin)

count=0


for i in reversed(range(n)):
        count=count+(k//coins[i])
        k=k%coins[i]
        
        
        

print(count)