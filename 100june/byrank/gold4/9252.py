str1=[""]+list(input())
str2=[""]+list(input())

dp=[[""] * len(str2) for _ in range(len(str1))]

for i in range(1,len(str1)):
    for j in range(1,len(str2)):
        if(str1[i]==str2[j]):
            dp[i][j]=dp[i-1][j-1]+str2[j]
        else:
            if(len(dp[i-1][j])>len(dp[i][j-1])):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]
print(len(dp[-1][-1]))
print(dp[-1][-1])