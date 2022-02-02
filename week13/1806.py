from operator import index
import sys

n,s=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))

sum_arr=[0]
m=0
for i in arr:
    m+=i
    sum_arr.append(m)

start=0
end=0

ans=100001
while(start<n):
    if(sum_arr[end]-sum_arr[start]>=s):
        ans=min(ans,end-start)
        start+=1
    else:
        if(end==n):
            start+=1
        else:
            end+=1
print(ans) if ans!=100001 else print(0)


## 처음에는 dp 그리디 dfs bfs 다 아니라고 판단해서 브루트 포스로 그냥 한번 시도해봤는데 예상대로 시간초과가 떴고
## 계속 시간 줄이는 방법 고민해보고 시도해봤는데 다 시간초과 떠서 질문검색 들어가보니까 이중 포인터를 사용한다해서
## 거기서 힌트얻고 이중 포인터로 풀음 이중포인터 알고리즘이 따로 있을 정도로 제법 이러한 문제에 사용하기 좋은듯