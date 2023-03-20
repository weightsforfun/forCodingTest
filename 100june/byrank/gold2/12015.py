n=int(input())
arr=list(map(int,input().split()))
lsp=[]
answer=0
def binary_search(left,right,target,lsp):
    while(left<=right):
        mid=(left+right)//2
        if(target==lsp[mid]):
            return mid
        elif(target<lsp[mid]):
            right=mid-1
        else:
            left=mid+1
    return left

lsp.append(arr[0])

for i in range(1,n):
    if(lsp[-1]<arr[i]):
        lsp.append(arr[i])
    else:
        lsp[binary_search(0,len(lsp)-1,arr[i],lsp)]=arr[i]
        
    
print(len(lsp))