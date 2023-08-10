import sys

def input():
    return sys.stdin.readline()

t,w=map(int,input().split(" "))

dp=[[[0]*(t+1) for _ in range(w+2)] for _ in range(2)]
arr=[0]

for i in range(t):
    arr.append(int(input()))

if arr[1] == 1: # 1번 나무일 경우 한 번도 이동하지 않아도 받을 수 있다.
    dp[0][0][1] = 1
else: # 2번 나무일 경우 한 번 이동해야 받을 수 있다.
    dp[1][1][1] = 1


for i in range(2,t+1):
    for j in range(w+1):
        if(arr[i]==1):
            dp[0][j][i]=max(dp[1][j-1][i-1],dp[0][j][i-1])+1
            dp[1][j][i]=max(dp[1][j][i-1],dp[0][j-1][i-1])
        if(arr[i]==2):
            dp[0][j][i]=max(dp[1][j-1][i-1],dp[0][j][i-1])
            dp[1][j][i]=max(dp[1][j][i-1],dp[0][j-1][i-1])+1

# for i in range(2):
#     for j in range(w+2):
#         print(dp[i][j])
#     print("-------------")

answer=0
for i in range(w+1):
    for j in range(t+1):
        answer=max(answer,max(dp[0][i][j],dp[1][i][j]))
print(answer)
