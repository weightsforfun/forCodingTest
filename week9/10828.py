stack=[]
arr=[]
n=int(input())

for i in range(n):
    arr.append(input())

def push(n):
    stack.append(n)
def pop():
    if(len(stack)>=1):
        print(stack.pop())
    else:
        print(-1)
def size():
    print(len(stack))
def empty():
    if(len(stack)>=1):
        print(0)
    else:
        print(1)
def top():
    if(len(stack)>=1):
        print(stack[-1])
    else:
        print(-1)
for s in arr:
    if(s=="pop"):
        pop()
    elif(s=="size"):
        size()
    elif(s=="empty"):
        empty()
    elif(s=="top"):
        top()
    else:
        p,num=s.split(" ")
        push(num)
        