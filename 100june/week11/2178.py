import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
maze=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visited=[[0 for _ in range(m)] for _ in range(n)]


queue=deque([[0,0]])
visited[0][0]=1

direction=[[0,0,-1,1],[1,-1,0,0]]

while queue:
    now=queue.popleft()
    for i in range(4):
        ud=now[0]+direction[0][i]
        lr=now[1]+direction[1][i]
        if(0<=ud<n and 0<=lr<m):
            if(visited[ud][lr]==0 and maze[ud][lr]==1):
                visited[ud][lr]=visited[now[0]][now[1]]+1
                queue.append([ud,lr])

print(visited[-1][-1])
