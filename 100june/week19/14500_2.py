import sys
input=sys.stdin.readline

n,m=map(int,input().split(" "))

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(" "))))

answer=0
move=[[1,-1,0,0],[0,0,1,-1]]
visited=[[0]*m for _ in range(n)]
max_value=max(max(arr))

def dfs(y,x,index,value):
    global answer
    global n,m
    if(index==4):
        answer=max(answer,value)
    if(value+((4-index)*max_value)<answer):
        return
    else:
        for i in range(4):
            newY=y+move[0][i]
            newX=x+move[1][i]
            if(0<=newY<n and 0<=newX<m):
                if(visited[newY][newX]==0):
                    visited[newY][newX]=1
                    dfs(newY,newX,index+1,value+arr[newY][newX])
                    visited[newY][newX]=0
                    if(index==1):  ## 다른 블럭은 전부 dfs로만 구현이 가능하나 ㅗ이모양은 안되기때문에 얘 만들어주는거만 구현함
                        if(i==0 or i ==1):
                            leftY=newY+move[0][2]
                            leftX=newX+move[1][2]
                            rightY=newY+move[0][3]
                            rightX=newX+move[1][3]
                        else:
                            leftY=newY+move[0][0]
                            leftX=newX+move[1][0]
                            rightY=newY+move[0][1]
                            rightX=newX+move[1][1]
                        if(0<=leftY<n and 0<=leftX<m and 0<=rightY<n and 0<=rightX<m):
                            newvalue=value+arr[newY][newX]+arr[leftY][leftX]+arr[rightY][rightX]
                            answer=max(answer,newvalue)
                        
                        
for i in range(n):
    for j in range(m):
        visited[i][j]=1
        dfs(i,j,1,arr[i][j])
        visited[i][j]=0
print(answer)
## 1%에서 시간초과
#pypy에서는 통과 근데 ㅗ 이블럭 찾을때 조금 비효율적으로 하지 않았나 싶네 그냥 그블럭에서만 dfs로 돌려줬어도 됐을듯
## 구글링해보니까 브루트 포스가 아니라 백트래킹처럼 가장 큰값 남은거 더해줘도 안되는 애들은 가지지기 해야 python3에서 시간초과 안날뻔 했는데 나네
## 시간이 더 줄긴 할거같은데 오히려 이렇게 하니까 시간초과가 나네 큰 의마가 없는 코드 같은데 오히려 max max에서 시간 잡아먹는듯