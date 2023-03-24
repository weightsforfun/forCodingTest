import copy
from collections import defaultdict
n,k=map(int,input().split())
items=[[0,0]]

dic={}
dic[0]=0

for i in range(n):
    items.append(list(map(int,input().split())))

items.sort()

for i in range(n+1):
    temp={}
    for j in dic:
        if(j+items[i][0]<=k):
            temp[j+items[i][0]]=max(dic.get(j+items[i][0],0),dic[j]+items[i][1])
    dic.update(temp)
answer=0       
for i in dic:
    answer=max(answer,dic[i])
print(answer)

