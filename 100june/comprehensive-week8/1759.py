import itertools
l,c=map(int,input().split(" "))
arr=list(input().split(" "))
a=[]
b=[]
answers=[]
for i in  arr:
    if(i=="a" or i=="i" or i=="e" or i=="o" or i=="u" ):
        a.append((i))
    else:
        b.append(i)
for i in range(1,len(a)+1):
    result_a=list(itertools.combinations(a,i))
    result_b=list(itertools.combinations(b,l-i))
    if(l-i<2):
        break
    for j in result_a:
        for k in result_b:
            answer=''.join(j)+''.join(k)
            answers.append(''.join(sorted(answer)))

if(len(answers)>=1):
    answers.sort()
    for i in answers:
        print(i)