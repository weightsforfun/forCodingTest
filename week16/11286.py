import sys
import heapq
input=sys.stdin.readline

n=int(input())
heap=[]
for i in range(n):
    command=int(input())
    if(command==0):
        if(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(abs(command),command))