import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

n=int(input())
arr=[]
last_num=0
for i in range(n):
    start,end=map(int,input().split())
    last_num=max([last_num,start,end])
    arr.append([start,end])

arr.sort(key=lambda x : x[0])


dp=defaultdict(int)

for i in range(n):
    start,end=arr[i]
    max_count=0
    for j in range(i-1,-1,-1):
        low_start,low_end=arr[j]
        if(low_end<end):
            max_count=max(max_count,dp[low_start])
    dp[start]=1+max_count

print(n-max(dp.values()))



