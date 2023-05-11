import sys
def input():
    return sys.stdin.readline().rstrip()
n,d,k,c=map(int,input().split())

ate=[0]*(d+1)
sushi=[]
for _ in range(n):
    sushi.append(int(input()))
sushi=sushi+sushi[:k-1]

start=0
end=0
count=0
answer=0
while(end<len(sushi) and start<=end):
    if(end-start<k):
        if(ate[sushi[end]]==0 and sushi[end]!=c):
            count+=1
        ate[sushi[end]]+=1
        end+=1
        answer=max(answer,count)
    else:
        if(sushi[start]!=c):
            if(ate[sushi[start]]==1):
                count-=1
                ate[sushi[start]]=0
            else:
                ate[sushi[start]]-=1
        start+=1
print(answer+1)
