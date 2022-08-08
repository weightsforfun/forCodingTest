import sys

n=int(sys.stdin.readline())

arr=[0,1,2,3,4,5,6]

for i in range(7,101):
    num=max(arr[i-4]*3,arr[i-5]*4,arr[i-3]*2)
    arr.append(num)
print(arr[n])



##처음에 dfs로 완전탐색으로 시도 n의 개수가 적어서 한번 해봄 하지만 못해도 2^100 이므로 시간초과가 날거같았음 
## 시간초과가 났고 예시에서 규칙을 찾아보니 acvv acvv 이런식으로 진행된다고 생각했는데 틀렸고 다시 보니까 아님 
## 4로 딱딱 나눠 떨어지는게 아닌 최대 숫자 4칸전까지 간다음 복사하는게 이득인듯
## 처음부터 dp라 판단하고 접근했으면 좀 더 수월했을듯 한동안 dp  안했더니 감 많이 잃음
# def dfs(index,copy,key,count):
#     global answer
#     if(index==n):
#         answer=max(answer,count)
#     else:
#         if(key==2):
#             if(index+2<=n):
#                 dfs(index+2,count,3,count)
#         else:
#             dfs(index+1,copy,2,count+copy)
#             dfs(index+1,copy,3,count+copy)


# for i in range(7,101):
#     num=arr[i-1]+(3**((i-3)//4))
#     arr.append(num)
# print(arr[n],type(arr[n]))
