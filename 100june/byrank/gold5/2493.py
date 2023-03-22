n=int(input())
tower=list(map(int,input().split()))
answer=[0]*n
stack=[n-1]
count=n-1
while(count>0):
    if(tower[stack[-1]]<tower[count-1]):
        while(stack and tower[stack[-1]]<tower[count-1]):
            index=stack.pop()
            answer[index]=count
        count-=1
        stack.append(count)
    else:
        count-=1
        stack.append(count)
        
for i in answer:
    print(i ,end=" ")