import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
m,n,k=map(int,input().split(" "))

arr=[[0]*n for _ in range(m)]

move=[[1,-1,0,0],[0,0,1,-1]]

answers=[]

def dfs(x,y):             ## 방문체크하고 4방향으로 방문여부 범위 여부 체크하고 통과되면 재귀함수로 들어감
    global arr
    global move
    global m
    global n
    global answer
    arr[y][x]=1
    for i in range(4):
        next_x=x+move[0][i]
        next_y=y+move[1][i]
        if(0<=next_x<n and 0<=next_y<m):
            if(arr[next_y][next_x]==0):
                answer+=1
                dfs(next_x,next_y)
    
for i in range(k):           ## 직사각형 부분 -1로 만들어서 탐색할때 걸러줌
    xy=list(map(int,input().split(" ")))     ## 꼭짓점 좌표 
    for j in range(xy[0],xy[2]):   ## x좌표
        for l in range(m-xy[3],m-xy[1]):  ## y 좌표
            arr[l][j]=-1

for i in range(m):         ## 전부 돌아보면서 방문 안한 노드일때 들어가서 영역 탐색해줌
    for j in range(n):
        if(arr[i][j]==0):
            answer=1
            arr[i][j]=1
            dfs(j,i)
            answers.append(answer)      ## 영역 넓이 리스트에 넣어줌
print(len(answers))
for i in sorted(answers):
    print(i,end=" ")
    


## 아무생각없이 재귀함수로 구현했더니 백준에서 rexursion error 뜸 제한 바꿔주니까 맞긴 맞았는데 que로하는게 좀더 bfs취지에도 맞고
## 제한 바꿔줄 필요도 없었을듯 기억해놓자.