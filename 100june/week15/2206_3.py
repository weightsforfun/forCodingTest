import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split(" "))

arr=[list(map(int,input().strip())) for _ in range(n)]

visited=[[[0]*2 for _ in range(m)] for _ in range(n)] ## 얘를 3중배열로 만들어서 벽을 뚥고 특정 노드에 도착했을때의 거리 그냥 왔을때의 거리를 구분해줌
que=deque([[0,0,1,1]])## x,y,break,distance
move=[[1,0,-1,0],[0,1,0,-1]]
distance=0
flag=0


while(que):
    item=que.popleft()
    x=item[0]
    y=item[1]
    can_break=item[2]
    distance=item[3]
    if(x==m-1 and y==n-1): ##도착
            flag=1
            break
    else:
         for i in range(4):
                new_x=x+move[0][i]
                new_y=y+move[1][i]
                if(0<=new_x<m and 0<=new_y<n):
                    if(arr[new_y][new_x]==1 and can_break==1):  ##벽을 만났는데 벽을 아직 안부숴서 부술수 있는경유
                        visited[new_y][new_x][1]=visited[new_y][new_x][0]+1    
                        que.append([new_x,new_y,0,distance+1])
                    elif(arr[new_y][new_x]==0 and visited[new_y][new_x][can_break]==0): ## 그냥 길 만났을때 can_break에 visited배열에 다르게 저장됌
                        visited[new_y][new_x][can_break]=1
                        que.append([new_x,new_y,can_break,distance+1])
                            
                    
    
    


if(flag):
    print(distance)
else:
    print(-1)
    
##구글링함 _1에서 막혔던 벽을 뚫고 온것과 안온거에 여부를 visited에 3차원 배열로 저장해줌 que에다가만 넣을 생각했는데
## visited까지 쓰면 가능하네
