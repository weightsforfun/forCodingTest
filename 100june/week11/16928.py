import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

ladder={}
snakes={}
board=[0]*101
checked=[0]*101

for i in range(n):
    k,v=map(int,sys.stdin.readline().split())
    ladder[k]=v

for i in range(m):
    k,v=map(int,sys.stdin.readline().split())
    snakes[k]=v

queue=deque([1])
checked[1]=1

while(queue):
    now=queue.popleft()
    for i in range(1,7):
        move=now+i
        if(move<=100 and checked[move]==0):
            if(move in ladder):
                move=ladder[move]
            elif(move in snakes):
                move=snakes[move]
            if(checked[move]==0):
                queue.append(move)
                checked[move]=1
                board[move]=board[now]+1

print(board[-1])
        
