import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
k=int(input())

computers=[]
visited=[0]*(n+1)
for i in range(n+1):
    computers.append([])
for i in range(k):
    start,end=map(int,input().split(" "))
    computers[start].append(end)
    computers[end].append(start)

computerQue=deque()
computerQue.append(1)
answer=-1
while(computerQue):
    current=computerQue.popleft()
    for i in computers[current]:
        if(not visited[i]):
            visited[i]=1
            computerQue.append(i)
            answer+=1
           
            
print(answer)
