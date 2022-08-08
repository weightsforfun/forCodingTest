n=int(input())
arr=[]
max_len=0
for i in range(n):
    arr.append(list(input()))

arr_rev=[[]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        arr_rev[i].append(arr[j][i])


def checking(li):  # 행 하나 주어졌을때 연속되는 길이 최대값 구해주는 함수
    max_count=0
    count=1
    for i in range(len(li)):
        for j in range(i,len(li)-1):
            if(li[j]==li[j+1]):
                count+=1
            else:
                max_count=max(max_count,count)
                count=0;
                break;
        max_count=max(max_count,count)
        count=1;
    return max_count


for i in range(n):            #가로부분 체크
    for j in range(n-1):    #각 행마다 옆에 사탕들 바꿔주면서 체크
        ar=[]+arr[i]
        ar[j],ar[j+1]=ar[j+1],ar[j]
        max_len=max(max_len,checking(ar))
    if(i==0):       #맨 위에 행 아래 행이랑 바꿔가면서 체크
        for j in range(n):
            ar=[]+arr[i]
            ar[j]=arr[i+1][j]
            max_len=max(max_len,checking(ar))
    elif(i==n-1):      # 가장 아래행 맨 위에 행이랑 바꿔가면서 최댓값 체크
        for j in range(n):
            ar=[]+arr[i]
            ar[j]=arr[i-1][j]
            max_len=max(max_len,checking(ar))
    else:     #중간행들 위아래 행이랑 값 바꿔주면서 최댓값체크
        for j in range(n):
            ar=[]+arr[i]
            ar[j]=arr[i+1][j]
            max_len=max(max_len,checking(ar))
            ar[j]=arr[i-1][j]
            max_len=max(max_len,checking(ar))

for i in range(n):         # 세로도 체크해야하므로 그냥 원래 사탕 배열 뒤집어서 똑같은 알고리즘으로 돌림
    for j in range(n-1):
        ar=[]+arr_rev[i]
        ar[j],ar[j+1]=ar[j+1],ar[j]
        max_len=max(max_len,checking(ar))
    if(i==0):
        for j in range(n):
            ar=[]+arr_rev[i]
            ar[j]=arr_rev[i+1][j]
            max_len=max(max_len,checking(ar))
    elif(i==n-1):
        for j in range(n):
            ar=[]+arr_rev[i]
            ar[j]=arr_rev[i-1][j]
            max_len=max(max_len,checking(ar))
    else:
        for j in range(n):
            ar=[]+arr_rev[i]
            ar[j]=arr_rev[i+1][j]
            max_len=max(max_len,checking(ar))
            ar[j]=arr_rev[i-1][j]
            max_len=max(max_len,checking(ar))
        
print(max_len)