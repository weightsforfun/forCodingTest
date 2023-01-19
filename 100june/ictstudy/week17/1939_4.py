import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split(" "))

nodelist=[[] for _ in range(n+1)]
max_weight=0
for i in range(m):
    x,y,w,=map(int,input().split(" "))
    nodelist[x].append((y,w))
    nodelist[y].append((x,w))
    max_weight=max(max_weight,w)
startNode,endNode=map(int,input().split(" "))

def bfs(target):
    global startNode,endNode
    que=deque()
    visited=set()
    que.append(startNode)
    while(que):
        current=que.pop()
        for node in nodelist[current]:
            if(not node[0] in visited):
                if(node[1]>=target):
                    que.append(node[0])
                    visited.add(node[0])
    if(endNode in visited):
        return True
    else:
        False
    
def binarySearch(start,end):
    mid=(start+end)//2
    while(start<=end):
        mid=(start+end)//2
        if(bfs(mid)):
            start=mid+1
            answer=mid
        else:
            end=mid-1
    return answer

print(binarySearch(0,max_weight))

