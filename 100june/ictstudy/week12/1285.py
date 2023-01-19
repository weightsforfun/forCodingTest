# import sys
# import copy
# n=int(sys.stdin.readline())

# coins=[]
# answer=400
# for i in range(n):
#     coins.append(list(sys.stdin.readline().strip()))    

# for i in range(n):             #연산할때 편하려고 1,-1로 앞뒤 표시해줌
#     for j in range(n):
#         if(coins[i][j]=="H"):
#             coins[i][j]=1
#         else:
#             coins[i][j]=-1
# def dfs(row,count):
#     global answer
#     plus=0
#     minus=0
#     if(row<n):
#         for i in range(n):
#             if(coins[row][i]==1):
#                 plus+=1
#             else:
#                 minus+=1
#             coins[row][i]*=-1
#         dfs(row+1,column,count+plus-minus)
#         for i in range(n):
#             coins[row][i]*=-1
#         dfs(row+1,column,count)
#     else:
#         for i in range(n):
            
# count=0
# for i in range(n):
#     for j in range(n):
#         if(coins[i][j]==-1):
#             count+=1
# dfs(0,0,count)
# print(answer)



