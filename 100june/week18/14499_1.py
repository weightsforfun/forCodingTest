import sys
input=sys.stdin.readline
n,m,y,x,k=map(int,input().split(" "))

arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split(" "))))

oredrs=list(map(int,input().split(" ")))
dice=[0,0,0,0,0,0,0]
def move(y,x,index):
    if(index==1):
        return y,x+1
    elif(index==2):
        return y,x-1
    elif(index==3):
        return y-1,x
    else:
        return y+1,x
def changeDice(index):
    if(index==1):
        dice[1],dice[3],dice[6],dice[4]=dice[4],dice[1],dice[3],dice[6]
    elif(index==2):
        dice[1],dice[3],dice[6],dice[4]=dice[3],dice[6],dice[4],dice[1]
    elif(index==3):
        dice[1],dice[5],dice[6],dice[2]=dice[5],dice[6],dice[2],dice[1]
    else:
        dice[1],dice[5],dice[6],dice[2]=dice[2],dice[1],dice[5],dice[6]


for order in oredrs:
    ny,nx=move(y,x,order)
    if(0<=ny<=n-1 and 0<=nx<=m-1):
        y,x=ny,nx
        changeDice(order)
        if(arr[y][x]==0):
            arr[y][x]=dice[6]
        else:
            dice[6]=arr[y][x]
            arr[y][x]=0
        print(dice[1])