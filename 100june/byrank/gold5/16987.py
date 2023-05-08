import sys

def input():
    return sys.stdin.readline().rstrip()

n=int(input())
eggs=[]
answer=0
for i in range(n):
    eggs.append(list(map(int,input().split())))

def dfs(index):
    # print(index,eggs)
    global answer
    if(index==n):
        count=0
        for i in range(n):
            if(eggs[i][0]<=0):
                count+=1
        answer=max(answer,count)
    else:
        if(eggs[index][0]>0):
            check=0
            for i in range(n):
                if(eggs[i][0]>0 and  i!=index):
                    check=1
                    eggs[index][0]=eggs[index][0]-eggs[i][1]
                    eggs[i][0]=eggs[i][0]-eggs[index][1]
                    dfs(index+1)
                    eggs[index][0]=eggs[index][0]+eggs[i][1]
                    eggs[i][0]=eggs[i][0]+eggs[index][1]
            if(not check):
                dfs(n)
        else:
            dfs(index+1)
dfs(0)
print(answer)