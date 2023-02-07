n=int(input())

arr=[0] * n
answer=0

def check(x):
    for i in range(x):
        if(arr[x]==arr[i] or abs(x-i)==abs(arr[x]-arr[i])):
            return False
    return True

def dfs(row):
    global answer
    global arr
    
    if(row==n):
        answer+=1
        return
    
    for i in range(n):
        arr[row]=i
        if(check(row)):
            dfs(row+1)
        
        
dfs(0)
print(answer)
    