a=0
b=0
answer_arr=[]
while(type(a)==int and type(b)==int):
    try:
        a,b=map(int,input().split())
        answer_arr.append(a+b)
    except:
        break
for answer in answer_arr:
    print(answer)