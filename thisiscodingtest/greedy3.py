n=int(input())
arr=list(map(int,input().split()))
arr.sort()
limit=1
for i in arr:
    if(limit<i):
        print(limit)
        break
    else:
        limit+=i