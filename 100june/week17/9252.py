import sys
input=sys.stdin.readline

first=input().strip("\n")
second=input().strip("\n")

arr=[[[0,""] for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(len(first)):
    for j in range(len(second)):
        if(first[i]==second[j]):
            arr[i+1][j+1][0]=arr[i][j][0]+1
            arr[i+1][j+1][1]=arr[i][j][1]+first[i]
        else:
            arr[i+1][j+1][0]=max(arr[i+1][j][0],arr[i][j+1][0])
            if (arr[i+1][j][0]>arr[i][j+1][0]):
                arr[i+1][j+1][1]=arr[i+1][j][1]
            else: 
                arr[i+1][j+1][1]=arr[i][j+1][1]
print(arr[-1][-1][0])
if(arr[-1][-1][0]!=0):
    print(arr[-1][-1][1])

## sys.stdin.readline 으로 받으면 뒤에 \n 있는거 기억하기
## 배열에 통채로 넣으려 했는데 알파벳이 한개씩 밖에 저장이 안됌 왜지
