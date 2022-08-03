from sys import stdin
import heapq
input=stdin.readline


##dfs로 시작지점으로부터 최소지점 방문하다가 k번 이내에 목적지 도착하면 값출력하는 알고리즘
# 이였는데 생각해보니까 완전 틀린 알고리즘임 
n,k=map(int,input().split(" "))

checkPoint=[]
visited=[0]*n
for i in range(n):
    checkPoint.append(list(map(int,input().split(" "))))
checkPoint.append([10000,10000])
def getOilForDistance(start,end):
    x=(start[0]-end[0])**2
    y=(start[1]-end[1])**2
    distance=(x+y)**0.5
    if(distance%10==0):
        return distance//10
    else:
        return (distance//10)+1

def dfs(currentPoint,countOfLandscape,maximumOilAmount):
    oilRequirementToCheckPoint=[]
    if(countOfLandscape>k):
        return 
    elif(currentPoint[0]==10000 and currentPoint[1]==10000):
        print(maximumOilAmount)
        exit(0)
    else:
        for i in range(n):
            if(visited[i]==0):
                neededOil=getOilForDistance(currentPoint,checkPoint[i])
                heapq.heappush(oilRequirementToCheckPoint,[neededOil,checkPoint[i],i])
        while(oilRequirementToCheckPoint):
            destination=heapq.heappop(oilRequirementToCheckPoint)
            visited[destination[2]]=1
            dfs(destination[1],countOfLandscape+1,max(maximumOilAmount,destination[0]))
            visited[destination[2]]=0
dfs([0,0],0,0)

##dfs로 시작지점으로부터 최소지점 방문하다가 k번 이내에 목적지 도착하면 값출력하는 알고리즘
# 이였는데 생각해보니까 완전 틀린 알고리즘임 
    
            