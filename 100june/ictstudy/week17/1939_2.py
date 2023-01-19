import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split(" "))
nodeList=[[0]*n for _ in range(n)]

def whatIsBigger(a,b):
    return max(a,b), min(a,b)

for i in range(m):
    a,b,c=map(int,input().split(" "))
    bigNode,smallNode=whatIsBigger(a,b)
    bigNode-=1
    smallNode-=1
    if(not nodeList[bigNode][smallNode]):
        nodeList[bigNode][smallNode]=c
       
    else:
        nodeList[bigNode][smallNode]=max(c,nodeList[bigNode][smallNode])
        

a,b=map(int,input().split(" "))
start,end=whatIsBigger(a,b)
start-=1
end-=1
priorityQ=[]

for i in range(n):
    bigNode,smallNode=whatIsBigger(i,start)
    print(bigNode,smallNode)
    heapq.heappush(priorityQ,(-nodeList[bigNode][smallNode],i))


while(priorityQ):
    currentNode=heapq.heappop(priorityQ)[1]
    bigNode,smallNode=whatIsBigger(start,currentNode)
    if(nodeList[start][end]<=nodeList[bigNode][smallNode]):
        for i in range(n):
            bigNode1,smallNode1=whatIsBigger(currentNode,i)
            bigNode2,smallNode2=whatIsBigger(start,i)
            newWeightLimit=min(nodeList[bigNode1][smallNode1],nodeList[bigNode2][smallNode2])
            nodeList[bigNode][smallNode]=max(newWeightLimit,nodeList[bigNode][smallNode])

print(nodeList[start-1][end-1])




## 질문 검색 보니까 한번의 이동이 다리 한번만 건너는게 아니라 경로 하나를 선택하는것임
## 다익스트라 알고리즘으로 짰더니 6퍼에서 메모리 초과 나옴
## 메모리 초과 해결을 위해 기존에 2중배열중 1,2  2,1 값을 둘다 할당해줬었는데
## 어자피 값은 같으므로 1,2 만 할당해주고 거리를 확인할때 2,1이 들어오면 1,2를 확인하게 고쳐줄꺼임