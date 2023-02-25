from collections import deque,defaultdict
import sys
input=sys.stdin.readline
n,m=map(int,input().split(" "))
answer=[1]*(n+1)
answer[0]=0
dic=defaultdict(list)
deq=deque()
indegree=[0]*(n+1)


for _ in range(m):
    a,b=map(int,input().split(" "))
    answer[b]=0
    indegree[b]+=1
    if(a in dic):
        dic[a].append(b)
    else:
        dic[a]=[b]

for i in range(n+1):
    if(answer[i]==1):
        deq.append(i)

while(deq):
    current=deq.popleft()
    for i in dic[current]:
        indegree[i]-=1
        if(indegree[i]==0):
            answer[i]=max(answer[i],answer[current]+1)
            deq.append(i)

print(*answer[1:])

        
    
