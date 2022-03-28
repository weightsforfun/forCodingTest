import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(" "))))


plan=list(map(int,input().split(" ")))

visited=[0]*n
flag=0
def dfs(start,destination):
    global flag
    if(flag):
        return 
    if(start==destination):
        flag=1
    for i in range(n):
        if(arr[start][i]==1):
            if(visited[i]==0):
                if(destination==i):
                    flag=1
                else:
                    visited[start]=1
                    dfs(i,destination)
                    visited[start]=0
            else:
                continue 
    

for i in range(m-1):
    flag=0
    dfs(plan[i]-1,plan[i+1]-1)
    if(flag==1):
        continue
    else:
        print("NO")
        exit(0)
print("YES")