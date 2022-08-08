import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().strip())))
    
move=[[0,1],[0,-1],[-1,0],[1,0]]
que=deque()
answer=0
print(arr)
for i in range(n):
    for j in range(m):
        if(arr[i][j]==0):
            answer+=1
            que.append([i,j])
            arr[i][j]=2
            while(que):
                current_node=que.pop()
                x=current_node[1]
                y=current_node[0]
                for k in move:
                    new_x=x+k[1]
                    new_y=y+k[0]
                    if(0<=new_x<m and 0<=new_y<n and arr[new_y][new_x]==0):
                        que.append([new_y,new_x])
                        arr[new_y][new_x]=2
print(answer)
            