import sys
from collections import deque
def input():
    return sys.stdin.readline().strip()

n=int(input())

for i in range(n):
    a,b,c=input().split(" ")
    a+="@"
    b+="@"
    deq=deque()
    deq.append([0,0,0])
    flag=0
    visited=[[0]*(len(b)) for _ in range(len(a))]
    while(deq):
        la,lb,lc=deq.popleft()
        temp_check=0
        if(lc==len(c)):
            flag=1
            deq.clear()
            break
        if(la<len(a) and a[la]==c[lc] and visited[la][lb]==0):
            visited[la][lb]=1
            temp_check=1
            deq.append([la+1,lb,lc+1])
        if(lb<len(b) and b[lb]==c[lc] and (visited[la][lb]==0 or temp_check==1)):
            visited[la][lb]=1
            deq.append([la,lb+1,lc+1])
    if(flag==1):
        print("Data set %d: yes" %(i+1))
    else:
        print("Data set %d: no" %(i+1))
    