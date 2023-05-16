import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

string=["Z"]+list(input())
visited=[0]*len(string)
heap=[]

for i in range(1,len(string)):
    min_index=0
    for j in range(1,len(string)):
        if(string[j]<=string[min_index] and visited[j]==0):
            min_index=j
    visited[min_index]=1
    heap.append(min_index)
    heap.sort()
    for j in range(len(heap)):
        print(string[heap[j]],end="")
    if(i!=len(string)-1):
        print()

