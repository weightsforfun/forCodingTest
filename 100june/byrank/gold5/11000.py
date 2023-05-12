import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key= lambda x : (x[0],x[1]) )
heap=[]
heapq.heappush(heap,arr[0][1])
count=1
answer=1
for i in range(1,n):
    if(arr[i][0]<heap[0]):
        count+=1
        heapq.heappush(heap,(arr[i][1]))
    else:
        while(heap[0]<=arr[i][0]):
            heapq.heappop(heap)
            count-=1
        heapq.heappush(heap,(arr[i][1]))
        count+=1
    answer=max(answer,count)
print(answer)