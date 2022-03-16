import sys
from collections import deque


input=sys.stdin.readline
n=int(input())
k=int(input())
apples=[]
for i in range(k):
    apples.append(list(map(int,input().split(" "))))
l=int(input())
snakesDirections=deque()

for i in range(l):
    snakesDirections.append(list(input().strip().split(" ")))

arr=[[0] *(n+2) for _ in range(n+2)]

for i in range(1,n+1):
    for j in range(1,n+1):
        arr[i][j]=1
for apple in apples:
    y=apple[0]
    x=apple[1]
    arr[y][x]=2


snakeQue=deque()
snakeQue.append([1,1])
time=0
snakesDirection=[0,1]
def isItSameNode(node1,node2):
    if(node1[0]==node2[0] and node1[1]==node2[1]):
        return True
    else:
        return False
def changeDirection(currentDirection,turnWay):
    if(currentDirection[0]==0):
        if(turnWay=="D"):
            currentDirection[0],currentDirection[1]=currentDirection[1],currentDirection[0]
        else:
            currentDirection[0],currentDirection[1]=-1*currentDirection[1],-1*currentDirection[0]
    else:
        if(turnWay=="L"):
            currentDirection[0],currentDirection[1]=currentDirection[1],currentDirection[0]
        else:
            currentDirection[0],currentDirection[1]=-1*currentDirection[1],-1*currentDirection[0]

while(True):
    currentNode=snakeQue[-1]
    if(snakesDirections):
        if(time==int(snakesDirections[0][0])):
            changeDirection(snakesDirection,snakesDirections.popleft()[1])
    nextY=currentNode[0]+snakesDirection[0]
    nextX=currentNode[1]+snakesDirection[1]
    nextNode=[nextY,nextX]
    time+=1
    for snake in snakeQue:
        if(isItSameNode(snake,nextNode)):
            print(time)
            exit(0)
    if(arr[nextY][nextX]==0):
        print(time)
        exit(0)
    elif(arr[nextY][nextX]==2):
        snakeQue.append(nextNode)
        arr[nextY][nextX]=1
    else:
        snakeQue.append(nextNode)
        snakeQue.popleft()
   
    
    
