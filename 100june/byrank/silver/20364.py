import sys
input=sys.stdin.readline
n,q=map(int,input().split())

arr=[]

for _ in range(q):
    arr.append(int(input()))


tree=[0]*(n+1)

for i in arr:
    target=i
    block=0
    while(target>1):
        if(tree[target]==1):
            block=target
        target=target//2
    if(block==0):
        tree[i]=1
        print(block)
    else:
        print(block)