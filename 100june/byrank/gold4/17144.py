from collections import deque
r,c,t=map(int,input().split())
arr=[]
moves=[[1,0],[-1,0],[0,1],[0,-1]]
air=[]
deq=deque()
for i in range(r):
    arr.append(list(map(int,input().split())))

for i in range(t):
    # print(arr)
    #미세먼지 확인
    for i in range(r):
        for j in range(c):
            if(0<arr[i][j]):
                deq.append((arr[i][j],i,j))
            if(arr[i][j]==-1):
                air.append([i,j])
    air_hig_y=air[0][0]
    air_low_y=air[1][0]
    #미세먼지 확산
    while(deq):
        density,y,x=deq.popleft()
        count=0
        for move in moves:
            new_y=y+move[0]
            new_x=x+move[1]
            if(0<=new_y<r and 0<=new_x<c and arr[y][x]>=0 and arr[new_y][new_x]>=0):
                arr[new_y][new_x]+=(density//5)
                count+=1
        arr[y][x]-=(count*(density//5))
    #공기청정기 작동
    #위쪽
    edge=arr[air_hig_y][-1]
    for i in range(c-1,1,-1):
        arr[air_hig_y][i]=arr[air_hig_y][i-1]
    arr[air_hig_y][1]=0
    
    edge2=arr[0][-1]
    for i in range(0,air_hig_y-1):
        arr[i][-1]=arr[i+1][-1]
    arr[air_hig_y-1][-1]=edge
    
    edge3=arr[0][0]
    for i in range(0,c-1):
        arr[0][i]=arr[0][i+1]
    arr[0][-2]=edge2
    
    for i in range(air_hig_y-1,0,-1):
        arr[i][0]=arr[i-1][0]
    arr[1][0]=edge3
    
    #아래쪽
    edge=arr[air_low_y][-1]
    for i in range(c-1,1,-1):
        arr[air_low_y][i]=arr[air_low_y][i-1]
    arr[air_low_y][1]=0
    
    edge2=arr[-1][-1]
    for i in range(r-1,air_low_y,-1):
        arr[i][-1]=arr[i-1][-1]
    arr[air_low_y+1][-1]=edge
    
    edge3=arr[-1][0]
    for i in range(0,c-1):
        arr[-1][i]=arr[-1][i+1]
    arr[-1][-2]=edge2
    
    for i in range(air_low_y+1,r-1):
        arr[i][0]=arr[i+1][0]
    arr[-2][0]=edge3
    

answer=0
for i in range(r):
    for j in range(c):
        if(arr[i][j]>0):
            answer+=arr[i][j]
print(answer)          
            
        
