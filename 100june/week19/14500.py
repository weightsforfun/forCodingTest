import sys
input=sys.stdin.readline

n,m=map(int,input().split(" "))

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(" "))))

answer=0
move=[[1,-1,0,0],[0,0,1,-1]]
visited=[[0]*m for _ in range(n)]

def dfs(y,x,index,value):
    global answer
    global n,m
    if(index==4):
        answer=max(answer,value)
    else:
        for i in range(4):
            newY=y+move[0][i]
            newX=x+move[1][i]
            if(0<=newY<n and 0<=newX<m):
                if(visited[newY][newX]==0):
                    visited[newY][newX]=1
                    dfs(newY,newX,index+1,value+arr[newY][newX])
                    visited[newY][newX]=0
for i in range(n):
    for j in range(m):
        visited[i][j]=1
        dfs(i,j,1,arr[i][j])
        visited[i][j]=0
print(answer)
## 브루트 포스 느낌으로 dfs로 쭉들어가면 될거라 생각했는데 그러면 ㅏ 이모양을 구현할수가 없네