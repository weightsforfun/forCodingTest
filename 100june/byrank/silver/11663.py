n,m=map(int,input().split(" "))
arr=list(map(int,input().split(" ")))
lines=[]
for i in range(m):
    lines.append(list(map(int,input().split(" "))))

def binary_search_min(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right+1

def binary_search_max(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right
    
    


for line in lines:
    start=binary_search_min(arr,line[0])
    end=binary_search_max(arr,line[1])
    print(end-start+1)    

