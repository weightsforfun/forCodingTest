n=int(input())

arr=[0] * n
answer=0

def check(x):
    for i in range(x):
        if(arr[x]==arr[i] or abs())

def dfs(row):
    global answer
    global arr
    
    if(row==n):
        answer+=1
        return
    
    for i in range(n):
        if(arr[row][i]==0):
            #세로 0으로 만들기
            for j in range(row,n):
                arr[j][i]=1
            # 기울기가 양인 대각선
            temp_row=row
            temp_column=i
            while( 0<=temp_row<n and 0<=temp_column<n):
                arr[temp_row][temp_column]=1
                temp_row+=1
                temp_column-=1
            #기울기가 음인 대각선
            temp_row=row
            temp_column=i
            while( 0<=temp_row<n and 0<=temp_column<n):
                arr[temp_row][temp_column]=1
                temp_row+=1
                temp_column+=1
            
            dfs(row+1)
            
            for j in range(row,n):
                arr[j][i]=0
            # 기울기가 양인 대각선
            temp_row=row
            temp_column=i
            while( 0<=temp_row<n and 0<=temp_column<n):
                arr[temp_row][temp_column]=0
                temp_row+=1
                temp_column-=1
            #기울기가 음인 대각선
            temp_row=row
            temp_column=i
            while( 0<=temp_row<n and 0<=temp_column<n):
                arr[temp_row][temp_column]=0
                temp_row+=1
                temp_column+=1
        
dfs(1)
print(answer)
    