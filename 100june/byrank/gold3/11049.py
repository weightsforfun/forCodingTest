n=int(input())
arr=[]
dp=[[0]*n for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(0,n-1):
    dp[i][i+1]=arr[i][0]*arr[i][1]*arr[i+1][1]



for i in range(2,n): # 길이가 3 ,4,5,....n 의 최대값 bottom up 으로 올라가기
    for j in range(0,n-i):# 각 줄은 3줄이면 dp가 n-2칸 4줄은 n-3 마지막은  n-(n-1)=1 칸 (최종 행렬)
        dp[j][j+i] = 2**32
        for k in range(j,j+i):#각 dp min값 구하기 어디서 묶을건지 3줄짜리는 경우의 수 2 4줄은 3 5줄은 4...
            dp[j][j+i]=min(dp[j][j+i],dp[j][k]+dp[k+1][j+i]+arr[j][0]*arr[k][1]*arr[j+i][1])

print(dp[0][n-1])
        
