import sys
import heapq
def input():
    return sys.stdin.readline()
INF=float("inf")
k=int(input())

for i in range(k):
    n,d,c=map(int,input().split(" "))
    visited=[0]*n
    distance=[INF]*n
    graph=[[] for _ in range(n)]
    c-=1
    distance[c]=0
    for j in range(d):
        a,b,s=map(int,input().split(" "))
        graph[b-1].append((s,a-1))
    
    heap=[]
    heapq.heappush(heap,(0,c))
    while(heap):
        dist,index=heapq.heappop(heap)
        if(distance[index]<dist):
            continue
        for next_cost,next_index  in graph[index]:
            next_dist=dist+next_cost
            if(next_dist<distance[next_index]):
                distance[next_index]=next_dist
                heapq.heappush(heap,(next_dist,next_index))
    
    count=0
    time=0
    for j in range(n):
        if(distance[j]!=INF):
            count+=1
            time=max(time,distance[j])
    print(count,time)

                

        
            

        