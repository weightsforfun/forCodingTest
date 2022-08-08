import sys
input=sys.stdin.readline
n,m=map(int,input().split(" "))
nodeList=[]
maximumWeight=0
for i in range(m):
    nodeList.append(input().strip("\n").split(" "))

node1,node2=input().strip("\n").split(" ")

for node in nodeList:
    if((node[0]==node1 and node[1]==node2) or (node[0]==node2 and node[1]==node1)):
        maximumWeight=max(maximumWeight,int(node[2]))
print(maximumWeight)

## 문제 설명이 애매함 한번에 이동할수있다는게 다리 하나만 쓰라는건줄 알았는데 이렇게 하니까 틀리네