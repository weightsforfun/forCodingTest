wabc=[0]*505050
answers=[]
def recur(a,b,c):
    if(a<=0 or b<=0 or c<=0):
        return 1
    elif(a > 20 or b > 20 or c > 20):
        return recur(20,20,20)
    elif(a < b and b < c):
        if(wabc[a*10000+b*100+c]!=0):
            return wabc[a*10000+b*100+c]
        else:
            wabc[a*10000+b*100+c]=recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
            return  wabc[a*10000+b*100+c]
    else:
        if(wabc[a*10000+b*100+c]!=0):
            return wabc[a*10000+b*100+c]
        else:
            wabc[a*10000+b*100+c]=recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)
        return wabc[a*10000+b*100+c]

while(1):
    li=list(map(int,input().split(" ")))
    if(li[0]==-1 and li[1]==-1 and li[2]==-1):
        break
    answers.append(li)
    

for i in answers:
    answer=recur(i[0],i[1],i[2])
    print(f'w({i[0]}, {i[1]}, {i[2]}) = {answer}')