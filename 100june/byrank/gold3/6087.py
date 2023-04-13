


##3 틀림

from collections import deque

move=[[1,0],[-1,0],[0,1],[0,-1]]

w,h=map(int,input().split())
arr=[]
visited=[[float("inf")]* w for _ in range(h)]
mirror_count=[[0]* w for _ in range(h)]
for i in range(h):
    arr.append(list(input()))
c=[]
for i in range(h):
    for j in range(w):
        if(arr[i][j]=="C"):
            c.append([i,j])

deq=deque([c[0]])
visited[c[0][0]][c[0][1]]=0

while(deq):
    current=deq.popleft()
    y,x=current[0],current[1]
    for i in range(4):
        new_y=y+move[i][0]
        new_x=x+move[i][1]
        while(True):
            if(not(0<=new_x<w) or not(0<=new_y<h)):
                break
            if(arr[new_y][new_x]=="*"):
                break
            if(visited[new_y][new_x]<visited[y][x]+1):
                break
            visited[new_y][new_x]=visited[y][x]+1
            deq.append([new_y,new_x])
            new_y+=move[i][0]
            new_x+=move[i][1]
            
print(visited[c[1][0]][c[1][1]]-1)
            

