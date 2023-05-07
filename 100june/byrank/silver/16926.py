import sys
def input():
    return sys.stdin.readline().rstrip()

n,m,r=map(int,input().split())
arr=[]

move=[[0,1],[1,0],[0,-1],[-1,0]]


for i in range(n):
    arr.append(list(map(int,input().split())))

def rotate(n,m,level):
    y,x=level,level
    start=arr[y][x]
    for i in range(4):
        while(True):
            dy=y+move[i][0]
            dx=x+move[i][1]
            if(dy<level or dy>n-level-1 or dx<level or dx>m-level-1):
                break
            else:
                arr[y][x]=arr[dy][dx]
                y=dy
                x=dx
    arr[level+1][level]=start


 
    

for i in range(r):
    for j in range(min(n,m)//2):
        rotate(n,m,j)

for i in arr:
    for j in i:
        print(j,end=" ")
    print()           
        
    
