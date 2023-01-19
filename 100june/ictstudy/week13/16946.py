import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split(" "))

arr=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

fixed_arr=[]

move=[[1,-1,0,0],[0,0,1,-1]]

checked=[[0]*m for _ in range(n)]

que=deque()

count=0

stack=[]  ## 배열들 보관했다가 값 바꿔줌

index=0

for i in range(n):   ## 먼저 한번 돌리면서 각각 연결되어있는 0들이 몇개씩 연결되있는지 센다음 표시해주고 나중에 구분을 위해 index도 부여해서 리스트로 [겂,인덱스]이렇게 만든다
    for j in range(m):
        if(arr[i][j]==1):
            arr[i][j]=-1
        if(arr[i][j]==0 and checked[i][j]==0):
            count+=1
            checked[i][j]=1
            stack.append([i,j])
            que.append([i,j])
            while(que):
                item=que.popleft()
                for k in range(4):
                    x=item[0]+move[0][k]
                    y=item[1]+move[1][k]
                    if(0<=x<n and 0<=y<m):
                        if(checked[x][y]!=1 and arr[x][y]==0):
                            count+=1
                            checked[x][y]=1
                            stack.append([x,y])
                            que.append([x,y])
            while(stack):
                item=stack.pop()
                arr[item[0]][item[1]]=[count%10,index]
            count=0
            index+=1
                

check_index=[]  ## 중복되는 영역 구분하기위해 영역 인덱스를 보관하는 배열

for i in range(n):    ## 벽을 미리 -1로 만들었기 때문에 -1도달할때마다 상하좌우 숫자를 다 더해준다 이때 인덱스를 이용하여 상하좌우중 중복되는 영역을 걸러주고 더해준다
    new_list=[]
    for j in range(m):
        if(arr[i][j]==-1):
            new_value=0
            for k in range(4):
                x=i+move[0][k]
                y=j+move[1][k]
                if(0<=x<n and 0<=y<m):
                        if(arr[x][y]!=-1 and (not arr[x][y][1] in check_index)):
                            new_value+=arr[x][y][0]
                            check_index.append(arr[x][y][1])
            new_list.append((new_value+1)%10)
            check_index=[]
        else:
            new_list.append(0)
    fixed_arr.append(new_list)

for i in fixed_arr:
    for j in i:
        print(j,end="")
    print()
    
## 플러드필 알고리즘 어려웠다 처음에는 그냥 bfs로 접근했다가 시간초과가 계속떠서 힌트를 보고 접근했다 
## 다시 접근한 방법도 문제가 중복되는 숫자를 더할수도 있는건데 0으로 묶인 영역마다 각각 index를  부여해서
## 나중에 더할때 중복없이 더해야 풀리는 문제 난 스택으로 따로 중복을 체크했지만 딕셔너리를 만들어서 하는게 좀 더 나을듯