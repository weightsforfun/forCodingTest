import sys
input=sys.stdin.readline
n=int(input())
m=int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(" "))))
for i in range(n):
    arr[i][i]=1

plan=list(map(int,input().split(" ")))

route=[]
visited=[0]*n
def dfs(start,destination):
    if(arr[start][destination]==1):
        route.append(destination)
        return 
    else:
        for i in range(n):
            if(arr[start][i]==1):
                if(visited[i]==0):
                    route.append(i)
                    visited[i]=1
                    dfs(i,destination)
                    
                    

for i in range(m-1):
    route=[]
    visited=[0]*n
    if(arr[plan[i]-1][plan[i+1]-1]):
        continue
    else:
        visited[plan[i]-1]=1
        route.append(plan[i]-1)
        dfs(plan[i]-1,plan[i+1]-1)
        for i in route:
            for j in route:
                arr[i][j]=1
    if(arr[plan[i]-1][plan[i+1]-1]):
        continue
    else:
        print("NO")
        exit(0)
print("YES")
# 36%에서 틀림 visit 초기화 해주니까 28%에서 틀림