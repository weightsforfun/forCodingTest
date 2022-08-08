import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().strip())))

answer=[[99999]*m for _ in range(n)] 

   
move=[[0,1],[0,-1],[-1,0],[1,0]]
que=deque()

que.append([0,0,0])

while(que):
    node=que.pop()
    x,y,distance=node[1],node[0],node[2]+1
    answer[y][x]=min(distance,answer[y][x])
    arr[y][x]=-1
    for i in move:
        new_x=x+i[1]
        new_y=y+i[0]
        if(0<=new_x<m and 0<=new_y<n and arr[new_y][new_x]==1):
            que.append([new_y,new_x,distance])
            
        

for i in answer:
    print(i)
            