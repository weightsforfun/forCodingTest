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
        if(arr[index]>a2[-1]):   #스택에 넣는수가 수열의 수보다 작을경우 계속 넣어준다
            a2.append(i) 
            i+=1
            answer.append("+")
        elif(arr[index]==a2[-1]):    #스택의 마지막수와 수열수가 같다면 빼서 수열을 만들어 주는데ㅐ 쓴다
            a1.append(a2.pop())
            answer.append("-")
            index+=1
        else:     ## 그외경우는 스택으로 못만듬
            print("NO")
            break
if(arr==a1):
    for i in answer:
        print(i)
