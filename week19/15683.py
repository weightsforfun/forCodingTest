import sys
input=sys.stdin.readline
n,m=map(int,input().split(" "))
arr=[]
answer=65
move=[[-1,0],[0,1],[1,0],[0,-1]]
for i in range(n):
    arr.append(list(map(int,input().split(" "))))

cctvs=[]
for i in range(n):
    for j in range(m):
        if(arr[i][j]!=0 and arr[i][j]!=6):
            cctvs.append([i,j,arr[i][j]])
            
def countZero():
    global n,m
    count=0
    for i in range(n):
        for j in range(m):
            if(arr[i][j]==0):
                count+=1
    return count
## 마지막에 0개수 세줌
def checkSight(direction,y,x,num):
    global n,m
    nX=direction[1]+x
    nY=direction[0]+y
    while(0<=nX<m and 0<=nY<n):
        if(arr[nY][nX]==6):
            break
        if(arr[nY][nX]==0):
            arr[nY][nX]=-1*num
        nX+=direction[1]
        nY+=direction[0]
## cctv진행방향 idrection으로 주고 그 방향 다 볼수있다고 체크
def resetSight(direction,y,x,num):
    global n,m
    nX=direction[1]+x
    nY=direction[0]+y
    while(0<=nX<m and 0<=nY<n):
        if(arr[nY][nX]==6):
            break
        if(arr[nY][nX]==-1*num):
            arr[nY][nX]=0
        nX+=direction[1]
        nY+=direction[0]
## dfs에 나올때 아까 볼수있다고 표시해줬던거 초기화
def dfs(index):
    global answer
    distinguishValue=index+1
    if(index==len(cctvs)):
        answer=min(answer,countZero())   
    else:
        item=cctvs[index]
        if(item[2]==1):
            for i in range(4):
                checkSight(move[i],item[0],item[1],distinguishValue)# distinguishValue는 cctv마다 감시하는 구역 숫자 바꿔주고 dfs나올때
                dfs(index+1)                                        # 초기화 시켜줄때 다른 cctv 영역까지 초기화 시캬버려서 구분하기 위해 cctv마다의
                resetSight(move[i],item[0],item[1],distinguishValue)# 고유숫자 부여해서 그 숫자만 초기화 시켜줌
        elif(item[2]==2):
            for i in range(2):
                checkSight(move[i],item[0],item[1],distinguishValue)
                checkSight(move[i+2],item[0],item[1],distinguishValue)
                dfs(index+1)
                resetSight(move[i],item[0],item[1],distinguishValue)
                resetSight(move[i+2],item[0],item[1],distinguishValue)
        elif(item[2]==3):
            for i in range(4):
                checkSight(move[i],item[0],item[1],distinguishValue)
                checkSight(move[(i+1)%4],item[0],item[1],distinguishValue)
                dfs(index+1)
                resetSight(move[i],item[0],item[1],distinguishValue)
                resetSight(move[(i+1)%4],item[0],item[1],distinguishValue)
        elif(item[2]==4):
            for i in range(4):
                checkSight(move[i],item[0],item[1],distinguishValue)
                checkSight(move[(i+1)%4],item[0],item[1],distinguishValue)
                checkSight(move[(i+3)%4],item[0],item[1],distinguishValue)
                dfs(index+1)
                resetSight(move[i],item[0],item[1],distinguishValue)
                resetSight(move[(i+1)%4],item[0],item[1],distinguishValue)
                resetSight(move[(i+3)%4],item[0],item[1],distinguishValue)
        elif(item[2]==5):
            for i in range(4):
                checkSight(move[i],item[0],item[1],distinguishValue)
            dfs(index+1)
            for i in range(4):
                resetSight(move[i],item[0],item[1],distinguishValue)

dfs(0)
print(answer)