from collections import deque
r,c=map(int,input().split(" "))
arr=[]

for i in range(r):
    arr.append(list(input()))
dic={}
dic['M']=[[-1,0],[1,0],[0,-1],[0,1]]
dic['Z']=[[-1,0],[1,0],[0,-1],[0,1]]
dic['-']=[[0,1],[0,-1]]
dic['|']=[[1,0],[-1,0]]
dic['+']=[[1,0],[-1,0],[0,-1],[0,1]]
dic['1']=[[0,1],[1,0]]
dic['2']=[[-1,0],[0,1]]
dic['3']=[[-1,0],[0,-1]]
dic['4']=[[0,-1],[1,0]]


start=[]
end=[]
answer=[]
visited=[[0]*c for _ in range(r)]
broken=[[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if(arr[i][j]=="."):
            continue
        elif(arr[i][j]=='M'):
            start=[i,j]
        elif(arr[i][j]=='Z'):
            end=[i,j]

deq=deque()
visited[start[0]][start[1]]=1
for dy,dx in dic['M']:
        ny=start[0]+dy
        nx=start[1]+dx
        if(0<=ny<r and 0<=nx<c):
            if(visited[ny][nx]==0 and arr[ny][nx]!="." and arr[ny][nx]!="Z"):
                visited[ny][nx]=1
                deq.append([ny,nx])


visited[end[0]][end[1]]=1
for dy,dx in dic['M']:
        ny=end[0]+dy
        nx=end[1]+dx
        if(0<=ny<r and 0<=nx<c):
            if(visited[ny][nx]==0 and arr[ny][nx]!="." and arr[ny][nx]!="M"):
                visited[ny][nx]=1
                deq.append([ny,nx])

while(deq):
    current=deq.popleft()
    y,x=current[0],current[1]
    node=arr[y][x]
    for dy,dx in dic[node]:
        ny=y+dy
        nx=x+dx
        if(0<=ny<r and 0<=nx<c):
            if(visited[ny][nx]==0):
                if(arr[ny][nx]=="."):
                    # print("y,x: " ,y,x)
                    # print(ny,nx)    
                    answer=[ny,nx]
                    broken[y][x]=1
                else:
                    deq.append([ny,nx])
                    visited[ny][nx]=1
                    
        
move=[0,0,0,0]
index=0

for dy2,dx2 in dic['M']:
    fy=answer[0]+dy2
    fx=answer[1]+dx2
    if(0<=fy<r and 0<=fx<c):
        if(arr[fy][fx]!="."  and (broken[fy][fx]==1 or visited[fy][fx]==0)):
            move[index]=1
    index+=1

if(sum(move)==4):
        answer.append('+')
elif(move[0]==1 and move[1]==1):
        answer.append('|')
elif(move[2]==1 and move[3]==1):
        answer.append('-')
elif(move[1]==1 and move[3]==1):
        answer.append('1')
elif(move[0]==1 and move[3]==1):
        answer.append('2')
elif(move[0]==1 and move[2]==1):
        answer.append('3')
elif(move[1]==1 and move[2]==1):
        answer.append('4')

print(answer[0]+1,answer[1]+1,answer[2])
