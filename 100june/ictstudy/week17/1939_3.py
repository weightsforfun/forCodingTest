import sys

input=sys.stdin.readline
n,m=map(int,input().split(" "))
nodeList=[[0]*n for _ in range(n)]
visited=[0]*n
distance=[]

def getMaxIndex(list):
    global visited
    minNum=0
    index=0
    for i in range(len(list)):
        if(list[i]>=minNum and not visited[i]):
            minNum=list[i]
            index=i
    return index

for i in range(m):
    a,b,c=map(int,input().split(" "))
    node1,node2=a-1,b-1
    if(not nodeList[node1][node2]):
        nodeList[node1][node2]=c
        nodeList[node2][node1]=c
    else:
        limit=max(c,nodeList[node1][node2])
        nodeList[node1][node2]=limit
        nodeList[node2][node1]=limit

start,end=map(int,input().split(" "))
start-=1
end-=1

for i in range(n):
    distance.append(nodeList[start][i])
visited[start]=1

for i in range(n):
    current=getMaxIndex(distance)
    visited[current]=1
    for j in range(n):
        if(visited[j]==0):
            newWeightsLimit=min(nodeList[current][j],nodeList[start][current])
            distance[j]=max(nodeList[start][j],newWeightsLimit)


print(distance[end])




## 시간복잡도 nlogn으로 만들려고 힙으로 했더니 메모리 초과나고 메모리 줄일려고 배열 반토막냈는데 
## 답안나옴 ㅋㅋ 걍 일반 다익스트라 시간복잡도 n제곱으로 시도해볼꺼임 얘도 메모리초과남 gg
## 다익스타라에 왜 꽂혀서 이지랄 했을까 하지만 덕분에 다익스트라 마스터함