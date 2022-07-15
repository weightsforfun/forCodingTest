start,end=map(int,input().split())
answers=[]

def check(num):
    if(num==1):
        return 0
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            return 0
    return 1

for i in range(start,end+1):
    if(check(i)):
        answers.append(i)

for i in answers:
    print(i)
