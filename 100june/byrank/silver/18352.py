from collections import defaultdict,deque
import sys
input=sys.stdin.readline
n,m,k,x=map(int,input().split())
distance=[-1]*(n+1)
distance[x]=0
dic=defaultdict(list)
que=deque([x])
for _ in range(m):
    start,end=map(int, input().split())
    dic[start].append(end)

while(que):
    current=que.popleft()
    for node in dic[current]:
        if(distance[node]==-1 and distance[current]<k):
            distance[node]=distance[current]+1
            que.append(node)

flag=1
for i in range(len(distance)):
    if(distance[i]==k):
        print(i)
        flag=0
if(flag):
    print(-1)
