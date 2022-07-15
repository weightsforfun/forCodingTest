import sys
# arr=[0]*20000001
dic={}

n=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

# for i in cards:
#     arr[i+10000000]+=1

# for i in nums:
#     print(arr[i+10000000],end=" ")

for i in cards:
    if(i in dic):
        dic[i]+=1
    else:
        dic[i]=1

for i in nums:
    if(i in dic):
        print(dic[i],end=" ")
    else:
        print(0,end=" ")