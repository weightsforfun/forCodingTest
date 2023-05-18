import sys
def input():
    return sys.stdin.readline().rstrip()

n=int(input())
dic={}
stack=[]
visited=[0]*(n+1)
move=0
for i in range(n):
    a,b,c=map(int,input().split())
    dic[a]=[b,c]
final_node=1
while(True):
    if(dic[final_node][1]==-1):
        break
    final_node=dic[final_node][1]

stack.append(1)

while(True):
    current=stack[-1]
    left,right=dic[current]
    if(left!=-1 and visited[left]==0):
        stack.append(left)
        move+=1
        visited[left]=1
    elif(right!= -1 and visited[right]==0):
        stack.append(right)
        move+=1
        visited[right]=1
    elif(current==final_node):
        break
    elif(right==-1 and left==-1):
        stack.pop()
        move+=1
    
    else:
        stack.pop()
        move+=1
print(move)
        
    