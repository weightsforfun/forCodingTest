import sys
from itertools import combinations  ## 이분탐색으로 거리값을 계속해서 찾아가면서 그 값이 최소값이 될수있는지 확인한다

n,c=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
answer=0
def binary(arr,start,end):
    while(start<=end):
        mid=(start+end)//2
        current=arr[0]
        count=1
        for i in range(1,len(arr)):
            if(arr[i]>=current+mid):
                count+=1
                current=arr[i]
        if(count<c):
            end=mid-1
        else:
            global answer
            answer=max(answer,mid)
            start=mid+1

binary(arr,1,arr[-1]-arr[0])
print(answer)