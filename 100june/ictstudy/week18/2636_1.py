import sys
from collections import deque
input=sys.stdin.readline
y,x=map(int,input().split(" "))

arr=[]
directions=[[1,-1,0,0],[0,0,1,-1]]
cheeseHoles=[]
cheeses=[]
for i in range(y):
    arr.append(list(map(int,input().split(" "))))

def initalize():
    global y
    global x
    visited=[[0]* x for _ in range (y)]
    queForInitialize=deque()
    queForInitialize.append([0,0])
    while(queForInitialize): ##외부 공기들 2로 바꿔줘서 구멍이랑 구분
        currentNode=queForInitialize.popleft()
        arr[currentNode[0]][currentNode[1]]=2
        for i in range(4):
            nextX=currentNode[1]+directions[1][i]
            nextY=currentNode[0]+directions[0][i]
            if(0<=nextY<=y-1 and 0<=nextX<=x-1):
                if(arr[nextY][nextX]==0): 
                    queForInitialize.append([nextY,nextX])
    for i in range(y):## 구멍들 배열로 만들어놓기
        for j in range(x):
            if(arr[i][j]==0 and visited[i][j]==0):
                queLookForCheeseHole=deque()
                queForSaveHole=deque()
                queLookForCheeseHole.append([i,j])
                visited[i][j]=1
                while(queLookForCheeseHole):
                    current=queLookForCheeseHole.popleft()
                    queForSaveHole.append(current)
                    for k in range(4):
                        nextX=current[1]+directions[1][k]
                        nextY=current[0]+directions[0][k]
                        if(0<=nextY<=y-1 and 0<=nextX<=x-1):
                            if(arr[nextY][nextX]==0 and not visited[nextY][nextX]==1):
                                queLookForCheeseHole.append([nextY,nextX])
                                visited[nextY][nextX]=1
                cheeseHoles.append(queForSaveHole)
            elif(arr[i][j]==1 and visited[i][j]==0):
                queLookForCheese=deque()
                queSavecheese=deque()
                queLookForCheese.append([i,j])
                visited[i][j]=1
                while(queLookForCheese):
                    current=queLookForCheese.popleft()
                    queSavecheese.append(current)
                    for k in range(4):
                        nextX=current[1]+directions[1][k]
                        nextY=current[0]+directions[0][k]
                        if(0<=nextY<=y-1 and 0<=nextX<=x-1):
                            if(arr[nextY][nextX]==1 and not visited[nextY][nextX]==1):
                                queLookForCheese.append([nextY,nextX])
                                visited[nextY][nextX]=1
                cheeses.append(queSavecheese)
            
initalize()






def isThereAir(currentY,currentX):
    global y
    global x
    for i in range(4):
        nearY=currentY+directions[0][i]
        nearX=currentX+directions[1][i]
        if(0<=nearY<=y-1 and 0<=nearX<=x-1):
            if(arr[nearY][nearX]==2):
                return True
    return False


time=0
answer=0    
cheeseWillBeMelted=deque()
while(True):
    isThereMoreCheese=0
    for cheeseHole in cheeseHoles:##치즈구멍이 공기에 노출되었나
        flag=0
        for i in range(len(cheeseHole)):
            if(isThereAir(cheeseHole[i][0],cheeseHole[i][1])):
                flag=1
        if(flag):
            while(cheeseHole):
                item=cheeseHole.popleft()
                arr[item[0]][item[1]]=2
        
    for cheese in cheeses:
        for i in range(len(cheese)):
            if(isThereAir(cheese[0][0],cheese[0][1])):
                cheeseWillBeMelted.append(cheese.popleft())
                isThereMoreCheese=1
                answer=0
            else:
                cheese.rotate(-1)
    while(cheeseWillBeMelted): #노출된 치즈 공기로 바꾸기
        item=cheeseWillBeMelted.popleft()
        arr[item[0]][item[1]]=2
        answer+=1  #마지막남은 치즈개수 저장하려고
    
    if(not isThereMoreCheese): ## 더이상 녹을 치즈 없으면 끝내기
        print(time)
        print(answer)
        break
    time+=1
    
#while문에서 브루트포스로 공기에 접촉해있는 치즈를 찾았었는데 initalize할때 미리 치즈 덩어리들 구해놔서
#그 치즈덩어리들 bfs하면서 녹는 치즈 구해야  시간복잡도 더 줄어들긴하겠다 이번껀 16%에서 시간초과뜸
## pypy는 66%에서 메모리 초과 deque while문 밖으로 빼도 66% 에서 메모리 초과뜨네