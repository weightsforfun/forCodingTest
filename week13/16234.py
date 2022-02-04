import sys
from tabnanny import check

n,l,s=map(int,sys.stdin.readline().split(" "))

arr=[[-1]*(n+2)]

total=0
countries=0
countries_index=[]
answer=0
changed=0

checked=[[0]*(n+2) for _ in range(n+2)]

for i in range(n):
    li=list(map(int,sys.stdin.readline().split(" ")))
    arr.append([-1]+li+[-1])
    
arr.append([-1]*(n+2))

def bfs(r,c):
    global flag
    global countries
    global total
    global countries_index
    global changed
    if(r<=n and c<=n):
        if(arr[r-1][c]!=-1 and checked[r-1][c]==0 and l<=abs(arr[r][c]-arr[r-1][c]) and abs(arr[r][c]-arr[r-1][c])<=s):
            checked[r-1][c]=1
            countries+=1
            total+=arr[r][c]
            countries_index.append([r,c])
            changed=1
            bfs(r-1,c)
        if(arr[r][c-1]!=-1 and checked[r][c-1]==0 and l<=abs(arr[r][c]-arr[r][c-1]) and abs(arr[r][c]-arr[r][c-1])<=s):
            checked[r][c-1]=1
            countries+=1
            total+=arr[r][c]
            countries_index.append([r,c])
            changed=1
            bfs(r,c-1)
        if(arr[r+1][c]!=-1 and checked[r+1][c]==0 and l<=abs(arr[r][c]-arr[r+1][c]) and abs(arr[r][c]-arr[r+1][c])<=s):
            checked[r+1][c]=1
            countries+=1
            total+=arr[r][c]
            countries_index.append([r,c])
            changed=1
            bfs(r+1,c)
        if(arr[r][c+1]!=-1 and checked[r][c+1]==0 and l<=abs(arr[r][c]-arr[r][c+1]) and abs(arr[r][c]-arr[r][c+1])<=s):
            checked[r][c+1]=1
            countries+=1
            total+=arr[r][c]
            countries_index.append([r,c])
            changed=1
            bfs(r,c+1)
while(True):
    for i in range(1,n):
        for j in range(1,n):
            checked[1][1]=1
            bfs(i,j)
            if(countries>=1):
                for k in countries_index:
                    arr[k[0]][k[1]]=total//countries
                total=0
                countries=0
                countries_index=[]
    if(changed==0):
        break
    else:
        answer+=1
        changed=0
        checked=[[0]*(n+2) for _ in range(n+2)]
print(answer)