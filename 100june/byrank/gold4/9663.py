n=int(input())

arr=[0] * n
answer=0

def check(x):
    for i in range(x):
        if(arr[x]==arr[i] or abs(x-i)==abs(arr[x]-arr[i])):
            return False
    return True

def dfs(column):
    global answer
    global arr
    
    if(column==n):
        answer+=1
        return
    
    for i in range(n):
        arr[column]=i
        if(check(column)):
            dfs(column+1)
        
        
dfs(0)
print(answer)
    


##############################################################################################################    
 
n=int(input())
col, slash, backSlash = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
count=0


def put_queen(column):
    global count
    for j in range(0,n):
          if not (col[j] or slash[column + j] or backSlash[column - j + n - 1]):
            if(column==n-1):
                count=count+1
            else:
                 col[j] = slash[column + j] = backSlash[column - j + n - 1] = True
                 put_queen(column + 1)
                 col[j] = slash[column + j] = backSlash[column - j + n - 1] = False

put_queen(0)
print(count)