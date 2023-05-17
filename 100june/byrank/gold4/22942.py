import sys
def input():
    return sys.stdin.readline().rstrip()

n=int(input())
circles=[]
for i in range(n):
    x,r=map(int,input().split())
    circles.append([x-r,i,0])
    circles.append([x+r,i,1])

circles.sort()

stack=[]
flag=1
stack.append(circles[0])

for i in range(1,n*2):
    
    x,index,position=circles[i]
    if(len(stack)==0):
        stack.append(circles[i])
    elif(position==stack[-1][2]):
        stack.append(circles[i])
    elif(position !=stack[-1][2] and index==stack[-1][1]):
        stack.pop()
    else:
        print("NO")
        flag=0
        break
    
if(flag):
    print("YES")