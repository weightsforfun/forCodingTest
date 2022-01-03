n=int(input())
answer=[]
def check(n):
    closed=0
    for i in range(len(n)):
        if(n[i]=="("):
            closed+=1
        else:
            closed-=1
        if(closed<0):
            return -1
    if(closed!=0):
        return -1
    else:
        return 1

for i in range(n):
    a=input()
    answer.append(check(a))

for i in range(n):
    if(answer[i]==-1):
        print("NO")
    else:
        print("YES")