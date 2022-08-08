
import sys

string=sys.stdin.readline().strip()

bomb=sys.stdin.readline().strip()
index=0
stack=[]

for i in string:
    stack.append(i)
    if(stack[-1]==bomb[-1]):
        if(''.join(stack[-len(bomb):])==bomb):
            for _ in range(len(bomb)):
                stack.pop()
            
    
if(stack):
    for i in stack:
        print(i,end="")
else:
    print("FRULA")