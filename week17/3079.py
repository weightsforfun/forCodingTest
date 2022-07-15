import sys
import heapq
input=sys.stdin.readline

n,m=map(int,input().split(" "))

priorityQue=[]

for i in range(n):
    item=int(input())
    heapq.heappush(priorityQue,[item,item])

for i in range(m-1):
    heapqItme=heapq.heappop(priorityQue)
    endTime=heapqItme[0]
    requiredTime=heapqItme[1]
    heapq.heappush(priorityQue,[endTime+requiredTime,requiredTime])

print(heapq.heappop(priorityQue)[0])

## 힙큐로 한번 해봤는데 10%에서 시간초과 나옴
#3 m이 10^9라 힙큐써도 10^10정도 나오네