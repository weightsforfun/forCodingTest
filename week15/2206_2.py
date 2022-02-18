import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

n,m=map(int,input().split(" "))

arr=[list(map(int,input().strip())) for _ in range(n)]

visited=[[0]*m for _ in range(n)]
move=[[1,0,-1,0],[0,1,0,-1]]
flag=0
answer=10000001

def dfs(x,y,can_break,distance):
    global arr
    global visited
    global flag
    global answer
    if(distance<=answer):
        if(x==m-1 and y==n-1):
            answer=min(answer,distance)
        else:
            if(can_break==0):  ##벽 안부숨
                for i in range(4):
                    new_x=x+move[0][i]
                    new_y=y+move[1][i]
                    if(0<=new_x<m and 0<=new_y<n):
                        if(visited[new_y][new_x]==0):
                            if(arr[new_y][new_x]==0): # 벽 안만나서 안부숨
                                visited[new_y][new_x]=1
                                dfs(new_x,new_y,0,distance+1)
                                visited[new_y][new_x]=0
                            else:
                                visited[new_y][new_x]=1
                                dfs(new_x,new_y,1,distance+1)
                                visited[new_y][new_x]=0
            else:  ## 벽 부숨
                for i in range(4):
                    new_x=x+move[0][i]
                    new_y=y+move[1][i]
                    if(0<=new_x<m and 0<=new_y<n):
                        if(arr[new_y][new_x]==0):
                            if(visited[new_y][new_x]==0):
                                visited[new_y][new_x]=1
                                dfs(new_x,new_y,1,distance+1)
                                visited[new_y][new_x]=0
                        
    
    

dfs(0,0,0,1)
if(answer==10000001):
    print(-1)
else:
    print(answer)


    
##visited 를 추가해 이미 도착한곳은 안가게 만듬 5%에서 메모리 초과뜸
## 2번째 시도에서는 visit위치를 바꿨는데 21%에서 틀렸다 뜸
## 빨리 왔다 하더라도 벽을 부수고 온 경우면 도착이제 갈때 벽을 못부수기때문에 단순히 최단거리로 왔다고 판단하면 안됌
## 백트래킹으로 시도해봤는데 계속 반례가 안됌 왤까 
# 반례는 해결했는데 python3 로는 시간초과 pypy는 메모리 초과뜸

