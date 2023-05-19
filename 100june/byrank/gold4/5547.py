import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

w,h=map(int,input().split())

arr=[]
arr.append([0]*(w+2))

for i in range(h):
    arr.append([0]+list(map(int,input().split()))+[0])

arr.append([0]*(w+2))

deq=deque()
deq.append((0,0))

move_odd=[(1,0),(-1,0),(0,-1),(0,1),(-1,1),(1,1)]
move_even=[(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(1,-1)]


while(deq):
    y,x=deq.popleft()
    temp=[]
    if(y%2!=0):
        temp=move_odd
    else:
        temp=move_even
    for i in temp:
        dy=y+i[0]
        dx=x+i[1]
        if(0<=dy<=h+1 and 0<=dx<=w+1 and arr[dy][dx]==0):
            arr[dy][dx]=-1
            deq.append((dy,dx))
answer=0
for y in range(h+2):
    for x in range(w+2):
        if(arr[y][x]==1):
            temp=[]
            if(y%2!=0):
                temp=move_odd
            else:
                temp=move_even
            for k in temp:
                dy=y+k[0]
                dx=x+k[1]
                if(arr[dy][dx]==-1):
                    answer+=1
print(answer)            



