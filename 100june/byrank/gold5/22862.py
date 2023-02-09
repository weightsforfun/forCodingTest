n,k=map(int,input().split(" "))
arr=list(map(int, input().split(" ")))

start,end=0,0
answer=0
count=0
while(end<n):
    if(count>k):
        if(arr[start]%2 !=0):
            count-=1
        start+=1
    else:
        if(arr[end]%2!=0):
            count+=1
        end+=1
    answer=max(answer,end-start-count)
    
print(answer)

