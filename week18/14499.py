import sys
from collections import deque
input=sys.stdin.readline
n,m,x,y,k=map(int,input().split(" "))

arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split(" "))))

oredrs=list(map(int,input().split(" ")))

def move(y,x,index):
    if(index==1):
        return y,x+1
    elif(index==2):
        return y,x-1
    elif(index==3):
        return y-1,x
    else:
        return y+1,x

d1=[0]
d2=[0]
d3=[0]
d4=[0]
d5=[0]
d6=[0]

north_south_way=deque()
east_west_way0=deque()
east_west_way1=deque()

north_south_way.append(d1)
north_south_way.append(d5)
north_south_way.append(d6)
north_south_way.append(d2)
east_west_way0.append(d1)
east_west_way0.append(d4)
east_west_way0.append(d6)
east_west_way0.append(d3)
east_west_way1.append(d2)
east_west_way1.append(d4)
east_west_way1.append(d5)
east_west_way1.append(d3)
flag=1

for order in oredrs:
    ny,nx=move(y,x,order)
    if(0<=ny<=n-1 and 0<=nx<=m-1):
        y,x=ny,nx
        if(order==3 or order==4):
            flag*=-1
            north_south_way.rotate(1) if order==4 else north_south_way.rotate(-1)
            if(arr[y][x]==0):
                arr[y][x]=north_south_way[2][0]
            else:
                north_south_way[2][0]=arr[y][x]
                arr[y][x]=0
            print(north_south_way[0][0])
            while(north_south_way[0][0]!=east_west_way0[0][0]):
                east_west_way0.rotate(1)
            while(north_south_way[1][0]!=east_west_way1[3][0]):
                east_west_way1.rotate(1)
        else:
            currentWay=east_west_way0 if flag==1 else east_west_way1
            currentWay.rotate(1) if order==1 else currentWay.rotate(-1)
            if(arr[y][x]==0):
                arr[y][x]=currentWay[2][0]
            else:
                currentWay[2][0]=arr[y][x]
                arr[y][x]=0
            print(currentWay[0][0])
        
                
#차원을 3개로 나눠서 해보려 했는데 안될듯 하드웨어기 부족함
#그냥 2차원배열로 해야할듯  