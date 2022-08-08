import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split(" "))

arr=[list(map(int,input().split(" "))) for _ in range(n)]

move=[[1,-1,0,0],[0,0,1,-1]]

answer=0

flag=1

que=deque()

for i in range(m):     ## 익은 토마토 좌표 que에 넣어주기
    for j in range(n):
        if(arr[j][i]==1):
            que.append([i,j,0])
            
while(que):             ## 익은 토마토들 부터 시작해서 bfs 끝가지 탐색
    item=que.popleft()
    a=item[0]
    b=item[1]
    day=item[2]
    answer=max(answer,day)   # 마지막 날짜 저장
    for i in range(4):
        x=a+move[0][i]
        y=b+move[1][i]
        if(0<=x<m and 0<=y<n):
            if(arr[y][x]==0):
                que.append([x,y,day+1])
                arr[y][x]=1

for i in range(m):     ## 만약 하나라도 안익었으면 -1출력하고 break flag를 통해 있는지 없는지 구분후 만약 다 익었으면 answer출력
    for j in range(n):
        if(arr[j][i]==0):
            print(-1)
            flag=0
            break
    if(flag==0):
        break
if(flag):
    print(answer)
    
