import sys
input=sys.stdin.readline
 
n=int(input())

days=[]

def dfs(index,value):
    global answer
    answer=max(value,answer)
    for i in range(index,len(days)):
        if(days[index][1]<=days[i][0]):
            dfs(i,value+days[i][2])
    
for startday in range(1,n+1):
    counselingPeriod,cost=map(int,input().split(" "))
    endDay=startday+counselingPeriod
    if(endDay>n+1):
        continue
    else:
        days.append([startday,endDay,cost])
        

days.sort(key=lambda x:x[1])

answer=0

for i in range(len(days)):
    dfs(i,days[i][2])
print(answer)

## n 15인거 보고 그냥 브루트로 풀음 좀더 깔끔하게 풀수있긴할듯