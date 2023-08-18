import sys

def input():
    return sys.stdin.readline()

n=int(input())
k=int(input())

div=1000000003

case=0

# 첫번째꺼 선택 == 마지막꺼 배제

dp=[[0]* (n) for _ in range(k+1)]
# 첫번째 무조건 선택 처리
for i in range(1,n):
    dp[1][i]=1

for i in range(2,k+1):
    for j in range(2,n):
        dp[i][j]=(dp[i][j-1]+dp[i-1][j-2])%div

case=dp[k][n-1]

# 첫번째꺼 선택 x 

case2=0

dp2=[[0]* (n+1) for _ in range(k+1)]

for i in range(2,n+1):
    dp2[1][i]=i-1

for i in range(2,k+1):
    for j in range(2,n+1):
        dp2[i][j]=(dp2[i][j-1]+dp2[i-1][j-2])%div

case2=dp2[k][n]


print((case+case2)%div)