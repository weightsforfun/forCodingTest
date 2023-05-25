import sys

def input():
    return sys.stdin.readline().rstrip()

h,w=map(int,input().split())

arr=list(map(int,input().split()))

max_height=max(arr)

block=[[0]* len(arr) for _ in range(max_height)]

for i in range(len(arr)):
    for j in range(arr[i]):
        block[j][i]=1
        


total_count=0

for i in range(max_height):
    turn=0
    temp_count=0
    for j in range(len(arr)):
        if(turn==0 and block[i][j]==1):
            turn=1
        elif(turn==1 and block[i][j]==0):
            temp_count+=1
        elif(turn==1 and block[i][j]==1):
            total_count+=temp_count
            turn=1
            temp_count=0
        else:
            continue

print(total_count)
