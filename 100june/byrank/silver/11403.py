n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if(arr[j][i]==1 and arr[i][k]==1):
                arr[j][k]=1
for i in arr:
    print(' '.join(list(map(str,i))))