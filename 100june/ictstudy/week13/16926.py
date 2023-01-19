import sys
from collections import deque
n,m,r=map(int,sys.stdin.readline().split(" "))

arr=[list(map(int,sys.stdin.readline().split(" "))) for _ in range(n)]

deq=deque()

index=0
shorter=min(n,m)
while(shorter-(2*index)>=2):
    for i in range(index,m-1-index):
        deq.append(arr[index][i])
    for i in range(index,n-1-index):
        deq.append(arr[i][m-index-1])
    for i in range(m-1-index,index,-1):
        deq.append(arr[n-index-1][i])
    for i in range(n-1-index,index,-1):
        deq.append(arr[i][index])
    
    
    deq.rotate(-r)
    
    
    for i in range(index,m-1-index):
        arr[index][i]=deq.popleft()
    for i in range(index,n-1-index):
        arr[i][m-index-1]=deq.popleft()
    for i in range(m-1-index,index,-1):
        arr[n-index-1][i]=deq.popleft()
    for i in range(n-1-index,index,-1):
        arr[i][index]=deq.popleft()
    index+=1
    deq.clear()

for i in arr:
    for j in i:
        print(j, end=" ")
    print()


## 일단 한겹씩 한겹씩 안으로 들ㅇ가면서 바꿔줘야한다는 생각부터 시작해서 접근했고 돌리는 부분에 있어서 어떻게 할지 고민하다가
## 배열로 할경우 꺾일때도 생각해야해서 너무 복잡하므로 그건 아니라 생각했고 고민하다가 얘를 일렬로 펴줘서 끝에것을 앞에 넣어주면 되겠다 생각해서 deque사용