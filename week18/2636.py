import sys
from collections import deque
input=sys.stdin.readline
y,x=map(int,input().split(" "))

arr=[]
directions=[[1,-1,0,0],[0,0,1,-1]]
cheeseHoles=[]
for i in range(y):
    arr.append(list(map(int,input().split(" "))))

def initalize():
    global y
    global x
    visited=[[0]* x for _ in range (y)]
    queForInitialize=deque()
    queForInitialize.append([0,0])
    while(queForInitialize):
        currentNode=queForInitialize.popleft()
        arr[currentNode[0]][currentNode[1]]=2
        for i in range(4):
            nextX=currentNode[1]+directions[1][i]
            nextY=currentNode[0]+directions[0][i]
            if(0<=nextY<=y-1 and 0<=nextX<=x-1):
                if(arr[nextY][nextX]==0): 
                    queForInitialize.append([nextY,nextX])
    for i in range(y):
        for j in range(x):
            if(arr[i][j]==0 and visited[i][j]==0):
                queForLookForHole=deque()
                queForSaveHole=deque()
                queForLookForHole.append([i,j])
                visited[i][j]=1
                while(queForLookForHole):
                    current=queForLookForHole.popleft()
                    queForSaveHole.append(current)
                    for k in range(4):
                        nextX=current[1]+directions[1][k]
                        nextY=current[0]+directions[0][k]
                        if(0<=nextY<=y-1 and 0<=nextX<=x-1):
                            if(arr[nextY][nextX]==0 and not visited[nextY][nextX]==1):
                                queForLookForHole.append([nextY,nextX])
                                visited[nextY][nextX]=1
                cheeseHoles.append(queForSaveHole)

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

while(True):
    cheeseWillBeMelted=deque()
    holeWillBeChargedWithAir=[]
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
        
    for i in range(y): ## 치즈가 공기에 노출되었나
        for j in range(x):
            if(arr[i][j]==1 and isThereAir(i,j)):
                answer=0
                isThereMoreCheese=1
                cheeseWillBeMelted.append([i,j])
    
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
#그 치즈덩어리들 bfs하면서 녹는 치즈 구해야  시간복잡도 더 줄어들긴하겠다