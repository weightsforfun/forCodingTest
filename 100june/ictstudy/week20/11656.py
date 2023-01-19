import sys
import heapq
input=sys.stdin.readline

char=input().strip()

heap=[]

for i in range(len(char)):
    heapq.heappush(heap,char[i:])

for i in range(len(heap)):
    print(heapq.heappop(heap))

