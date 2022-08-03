import sys
input=sys.stdin.readline()

n,k=map(int,input.split(" "))

dp=[100000]*100001
count=0
for i in range(n,-1,-1):
    dp[i]=count
    count+=1

for i in range(n+1,k+1):
    if(i%2==0):
        dp[i]=min(i-n,dp[i//2]+1)
    else:
        dp[i]=min(i-n,dp[(i+1)//2]+2,dp[(i-1)//2]+2)

print(dp[k])

## 이건 무조건  dp 로되겠다 생각해서 dp 로 접근했고 짝수일때는 그 해당하는 수의 //2 한숫자로 접근 혹은 직접 걸어서 접근
## 홀수일경우는 처음에는 +1한숫자에 //2 한숫자 접근 및 걸어서 접근을 비교했는데 -1한숫자고 생각했어야했다.
## 질문검색엣는 대부분 bfs dfs로 품 어떤사람들은 이게 dp로 불가능하다함 범위 나눠서 뒤로는 순간이동 못하니까
## 그렇게 나눠서 구하면 dp로도 가능