import sys
from collections import deque

n,l,s=map(int,sys.stdin.readline().split(" "))

arr=[[-1]*(n+2)]

for i in range(n):
    li=list(map(int,sys.stdin.readline().split(" ")))
    arr.append([-1]+li+[-1])
    
arr.append([-1]*(n+2))


move=[[1,-1,0,0],[0,0,1,-1]]

que=deque()

changed=0

answer=0

while(True):
    checked=[[0]*(n+2) for _ in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(checked[i][j]==0):
                que.append([i,j])
                checked[i][j]=1
                count=1
                total=arr[i][j]
                stack=[]
                while(que):
                    item=que.popleft()
                    stack.append(item)
                    for k in range(4):
                        x=item[0]+move[0][k]
                        y=item[1]+move[1][k]
                        if(arr[x][y]!=-1 and checked[x][y]==0 and l<=abs(arr[x][y]-arr[item[0]][item[1]])<=s):
                            changed=1
                            que.append([x,y])
                            checked[x][y]=1
                            count+=1
                            total+=arr[x][y]
                for q in stack:
                    arr[q[0]][q[1]]=total//count
    if(changed==0):
        print(answer)
        break;
    else:
        answer+=1
        changed=0
### 처음에는 dfs 함수를 만들어서 접근했는데 방문여부 값 배열 이동이 있었는지 없었는지 등 전역변수 선언을 너무 많이 해야하고 함수 나갈때 들어갈대
##3 컨트롤이 힘들어서 bfs로 방향을 바꾸고 queue 사용 바뀐건 다 배열에 넣어놨다가 마지막에 queue에 아무것도 업으면 이동이 끝난것이므로
### 평균값 계산해서 바꿈 만약 이동이 1번이라도 일어났으면 changed 를 1로 바꿔 while 계속 돌아가게 하고 아니면 break로 답도출