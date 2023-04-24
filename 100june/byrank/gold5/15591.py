from collections import deque
n,q=map(int,input().split())
arr=[[] for _ in range(n)]

for i in range(n-1):
    start,end,r=map(int,input().split())
    arr[start-1].append([end-1,r])
    arr[end-1].append([start-1,r])

for i in range(q):
    k,v=map(int,input().split())
    deq=deque()
    deq.append([float("inf"),v-1])
    result=0
    visited=[0]*n
    while(deq):
        current=deq.popleft()
        value,node=current[0],current[1]
        visited[node]=1
        for new_node,new_value in arr[node]:
            min_value=min(new_value,value)
            if(min_value>=k and visited[new_node]==0):
                visited[new_node]=1
                deq.append([min_value,new_node])
                result+=1
    print(result)