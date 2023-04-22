import heapq
n,m,x=map(int,input().split())
distance=[[float("inf")]*n for _ in range(n)]
graph=[[] for _ in range(n)]
students=[0]*n
for i in range(m):
    start,end,cost=map(int,input().split())
    graph[start-1].append([end-1,cost])

def dijk(start):
    distance[start][start]=0
    heap=[]
    heapq.heappush(heap,[0,start])
    while(heap):
        cost,current=heapq.heappop(heap)
        if(cost<distance[start][current]):
            continue
        for next in graph[current]:
            next_cost=cost+next[1]
            if(distance[start][next[0]]>next_cost):
                distance[start][next[0]]=next_cost
                heapq.heappush(heap,[next_cost,next[0]])

for i in range(n):
    dijk(i)

for i in range(n):
    if(i==x):
        continue
    students[i]=distance[i][x-1]+distance[x-1][i]
print(max(students))



    