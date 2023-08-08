import sys

def input():
    return sys.stdin.readline()

n=int(input())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().split(" "))))

arr.sort(key=lambda x : (x[0],x[1]))
start=arr[0][0]
end=arr[0][1]
answer=0
for i in range(1,n):
    now=arr[i]
    if(now[0]<end and now[1]>end):
        end=now[1]
    elif(now[0]<end and now[1]<end):
        continue
    elif(now[0]>=end):
        answer+=(end-start)
        start=now[0]
        end=now[1]

answer+=(end-start)
print(answer)

