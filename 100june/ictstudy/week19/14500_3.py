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
                    if(index==2):
                        visited[newY][newX]=1
                        dfs(y,x,index+1,value+arr[newY][newX])
                        visited[newY][newX]=0
                    visited[newY][newX]=1
                    dfs(newY,newX,index+1,value+arr[newY][newX])
                    visited[newY][newX]=0
                   
                        
                        
for i in range(n):
    for j in range(m):
        visited[i][j]=1
        dfs(i,j,1,arr[i][j])
        visited[i][j]=0
print(answer)
## 1%에서 시간초과
#pypy에서는 통과 근데 ㅗ 이블럭 찾을때 조금 비효율적으로 하지 않았나 싶네 그냥 그블럭에서만 dfs로 돌려줬어도 됐을듯
## 얘도 통과는 하는데 내가 처음짠 코드보다 시간이 더걸림