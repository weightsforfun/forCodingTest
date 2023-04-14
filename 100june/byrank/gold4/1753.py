import heapq
v,e=map(int,input().split())
k=int(input())

distance=[float("inf")]*v
graph=[[] for _ in range(v)]

for i in range(e):
    start,end,cost=map(int,input().split())
    graph[start-1].append([end-1,cost])

def dijk(start):
    distance[start]=0
    heap=[]
    heapq.heappush(heap,[0,start])
    while(heap):
        cost,current=heapq.heappop(heap)
        if(cost<distance[current]):
            continue
        for next in graph[current]:
            next_cost=cost+next[1]
            if(distance[next[0]]>next_cost):
                distance[next[0]]=next_cost
                heapq.heappush(heap,[next_cost,next[0]])
dijk(k-1)
for i in distance:  
    if(i==float("inf")):
        print("INF")
    else:
        print(i)
    