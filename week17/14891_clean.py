import sys
from collections import deque
input=sys.stdin.readline
gears=[]
def checkLeft(index,clockwise,isPoleSame,gears):
    if(1<=index<=3):
        if(not isPoleSame[index-1]):
            gears[index-1].rotate(-clockwise)
            checkLeft(index-1,-clockwise,isPoleSame,gears)
        else:
            return
    else:
        return
def checkRight(index,clockwise,isPoleSame,gears):
    if(0<=index<=2):
        if(not isPoleSame[index]):
            gears[index+1].rotate(-clockwise)
            checkRight(index+1,-clockwise,isPoleSame,gears)
        else: 
            return
    else:
        return
    
for i in range(4):                    ## gears에다가 각각 deque생성해서 넣어주긴했는데 사실 gears는 deque가 아니라 deque의 주소를 가지는거잖아
    gear=deque()                      ## 같은변수명을 사용해도 매번 새로 할당하면 기존 주소는 남아있고 새로 생기는 deque주소가 각각 저장되는거같네
    temp=list(map(int,list(input().strip("\n"))))
    for i in temp:
        gear.append(i)
    gears.append(gear)

k=int(input())

for i in range(k):
    gearIndex,clockwise=map(int,input().split(" "))
    isPoleSame=[0,0,0]
    for i in range(3):
        if(gears[i][2]==gears[i+1][6]):
            isPoleSame[i]=1
    gears[gearIndex-1].rotate(clockwise)
    checkLeft(gearIndex-1,clockwise,isPoleSame,gears)
    checkRight(gearIndex-1,clockwise,isPoleSame,gears)
        
answer=0
for i in range(4):
    if(gears[i][0]==1):
        answer+=2**i 
print(answer)
## 알고리즘은 간단했음 구현문제인듯 처음에 톱니바퀴 4개여서 그냥 모든 경우의수 건드려줄까 하다가 그냥 left right함수 만들어서 
## 쭉 탐색하게함 톱니바퀴 개수가 늘어나도 구현할수있게


    