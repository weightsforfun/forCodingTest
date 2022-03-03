import sys
from collections import deque
input=sys.stdin.readline
gears=[]
for i in range(4):                    ## gears에다가 각각 deque생성해서 넣어주긴했는데 사실 gears는 deque가 아니라 deque의 주소를 가지는거잖아
    gear=deque()                      ## 같은변수명을 사용해도 매번 새로 할당하면 기존 주소는 남아있고 새로 생기는 deque주소가 각각 저장되는거같네
    print(id(gear))
    temp=list(map(int,list(input().strip("\n"))))
    for i in temp:
        gear.append(i)
    gears.append(gear)

# k=int(input())
# for i in range(k):
#     gearIndex,clockwise=map(int,input().split(" "))
    