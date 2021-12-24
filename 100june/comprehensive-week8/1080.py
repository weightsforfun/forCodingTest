import sys
n,m=map(int,input().split())
before=[]
after=[]
count=0
no_answer=1
for i in range(n):
    before.append(list(map(int,sys.stdin.readline().strip())))
    for j in range(m):
        if(before[i][j]==0):
            before[i][j]=-1
for i in range(n):
    after.append(list(map(int,sys.stdin.readline().strip())))
    for j in range(m):
        if(after[i][j]==0):
            after[i][j]=-1


if(n<3 or m<3):   #바꿀수없을때
    if(before==after):
        print(0)
    else:
        print(-1)
else:       #바꿀수있을때
    for i in range(n-2):   #위에줄부터 3x3씩 바꿔준다
        for j in range(1,m-1):   #2번째부터 해당하는 행의 3x3배열을 바꿔주는데 전 행을 기준으로 다르면 바꿔주고 같으면 안바꿔준디
            if(before[i][j-1]!=after[i][j-1]):
                count+=1
                for k in range(3):
                    before[i+k][j-1]*=-1
                    before[i+k][j]*=-1
                    before[i+k][j+1]*=-1
                    if(before==after):
                        print(count)
                        no_answer=0
    if(no_answer):
        print(-1)
