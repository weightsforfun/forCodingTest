num=input();
result=num;
count=1
if(len(num)==1):
    num="0"+num
plused_value=int(num[0])+int(num[1])
plused_value=str(plused_value);
if(len(plused_value)==1):
    plused_value="0"+ plused_value
num = num[1] + plused_value[1]


while(int(num)!=int(result)):
    if(len(num)==1):
        num="0"+num
    plused_value=int(num[0])+int(num[1])
    plused_value=str(plused_value);
    if(len(plused_value)==1):
        plused_value="0"+ plused_value
    num = num[1] + plused_value[1]
    count=count+1

print(count)
    
    
