n,b=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        arr[i][j]%=1000

def matrix_square(matrix):
    new_matrix=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j]+=(matrix[i][k]*matrix[k][j])
            new_matrix[i][j]%=1000
    return new_matrix

def matrix_mul(matrix1,matrix2):
    new_matrix=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j]+=(matrix1[i][k]*matrix2[k][j])
            new_matrix[i][j]%=1000
    return new_matrix

def dac(count):
    if(count==1):
        return arr
    elif(count==2):
        return matrix_square(arr)
    if(count%2==0):
        return matrix_square(dac(count//2))
    elif(count%2==1):
        return matrix_mul(dac((count-1)),arr)

answer=dac(b)
for i in range(n):
    for j in range(n):
        print(answer[i][j],end=" ")
    print("")


    