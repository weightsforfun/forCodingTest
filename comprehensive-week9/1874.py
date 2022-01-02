import sys
arr=[]
a1=[]
a2=[]
answer=[]
index=0
n=int(sys.stdin.readline())

for i in range(n):
    arr.append(int(sys.stdin.readline()))
i=1
while(len(a1)<len(arr)):
    if(len(a2)==0):
        a2.append(i)
        answer.append("+")
        i+=1
    else:
        if(arr[index]>a2[-1]):
            a2.append(i)
            i+=1
            answer.append("+")
        elif(arr[index]==a2[-1]):
            a1.append(a2.pop())
            answer.append("-")
            index+=1
        else:
            a1.append(a2.pop())
            answer.append("-")
            index+=1
if(arr==a1):
    for i in answer:
        print(i)
else:
    print("NO")
