n,s=map(int,input().split())
arr=list(map(int,input().split()))

start=0
end=0
total=0
answer=100001
flag=0
while(start<n):
    # print("start:" ,start,"end: ",end)
    if(end==n and total<s):
        break
    if(total<s and end<n):
        # print("total<s",total)                       ## 5 1 3 5 10 7 4 9 2 8
        total+=arr[end]
        end+=1
    elif(total>=s):
        total-=arr[start]
        start+=1
        answer=min(answer,end-start+1)
        flag=1
if(flag):
    print(answer)
else:
    print(0)