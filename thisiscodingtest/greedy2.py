target=list(map(int,list(input())))
fixed_target=[]

while(target):
    item=target.pop()
    if(item==0):
        continue
    elif(item==1):
        if(target):
            fixed_target.append(item+target.pop())
        else:
            fixed_target[-1]+=1
    else:
        fixed_target.append(item)
answer=1
for i in fixed_target:
    answer*=i
print(answer)

