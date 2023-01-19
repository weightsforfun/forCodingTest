import sys
from collections import deque


input=sys.stdin.readline

def ac(command,arr):
    que=deque()
    command=command.replace("RR","")
    for i in arr:
        if(i==''):
            print("error")
            return
        que.append(int(i))
    for i in command:
        if(not que):
            print("error")
            return 
        if(i=="R"):
            que.reverse()
        elif(i=="D"):
            que.popleft()
    answer=[]
    while(que):
        answer.append(que.popleft())
    print(answer)

t=int(input())

for i in range(t):
    command=input().strip()
    n=int(input())
    arr=(input().replace("[","").replace("]","").strip().split(","))
    ac(command,arr)


## 33%에서 시간초과 났음  
