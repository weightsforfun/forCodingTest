import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split(" "))

arr=[list(map(int,input().strip())) for _ in range(n)]

visited=[[0]*m for _ in range(n)]
que=deque([[0,0,0,1]])## x,y,break,distance
move=[[1,0,-1,0],[0,1,0,-1]]
distance=0
flag=0


while(que):
    item=que.popleft()
    x=item[0]
    y=item[1]
    can_break=item[2]
    distance=item[3]
    if(visited[y][x]==0):
        visited[y][x]=1
        if(x==m-1 and y==n-1): ##도착
            flag=1
            break
        else:
            if(can_break==0):  ##벽 안부숨
                for i in range(4):
                    new_x=x+move[0][i]
                    new_y=y+move[1][i]
                    if(0<=new_x<m and 0<=new_y<n):
                        if(arr[new_y][new_x]==0): # 벽 안만나서 안부숨
                            que.append([new_x,new_y,0,distance+1])
                            
                        else:   # 벽 만나서 부숨
                            que.append([new_x,new_y,1,distance+1])
                            
            else:  ## 벽 부숨
                for i in range(4):
                    new_x=x+move[0][i]
                    new_y=y+move[1][i]
                    if(0<=new_x<m and 0<=new_y<n):
                        if(arr[new_y][new_x]==0):
                            que.append([new_x,new_y,1,distance+1])
                            
                    
    
    


if(flag):
    print(distance)
else:
    print(-1)
    
##visited 를 추가해 이미 도착한곳은 안가게 만듬 5%에서 메모리 초과뜸
## 2번째 시도에서는 visit위치를 바꿨는데 21%에서 틀렸다 뜸
