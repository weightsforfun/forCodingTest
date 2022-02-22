import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split(" ")))
arr.sort()
m=int(input())

for i in range(arr[-1],0,-1):
    maximum_budget=i
    total_budgets=0
    for j in range(n):
        if(arr[j]<=maximum_budget):
            total_budgets+=arr[j]
        else:
            total_budgets+=(maximum_budget*(n-j))
            break
    if(total_budgets<=m):
        print(maximum_budget)
        break
## bruteforce로 풀어봤는데 시간 초과 뜸 예산중에서 가장 큰값부터 내려오면서 최대 예산 구해주는 알고리즘 
#3 나름 for문도 도중에 나오게 하고 했는데도 4퍼에서 시간초과 뜨네
## pypy 로 하니까 맞음 근데 bruteforce말고 뭔가 규칙으로도 충분히 더 빨리 할수있을거같은데
## 이분 탐색으로 하는게 훨씬더 빠르겠구나