from collections import deque
import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())

total=sum([a,b,c])

visited=[[0]* total for _ in range(total)]

def bfs(a,b,total):
    deq=deque()
    deq.append((a,b))
    visited[a][b]=1
    while(deq):
        a,b=deq.popleft()
        c=total-a-b
        if(a == b == c):
            return 1
        else:
            for x,y in (a,b),(a,c),(b,c):
                if(x<y):
                    y=y-x
                    x=x*2
                elif(x>y):
                    x=x-y
                    y=y*2
                else:
                    continue
                z=total-x-y
                new_a=min(x,y,z)
                new_b=max(x,y,z)
                if(not visited[new_a][new_b]):
                    deq.append((new_a,new_b))
                    visited[new_a][new_b]=1
    return 0

if(total%3!=0):
    print(0)
else:
    print(bfs(a,b,total))
        
        
        
        
    

