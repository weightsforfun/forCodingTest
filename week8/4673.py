arr=[]

checked=[0]*10001
for i in range(0,10001):
    arr.append(i)

for i in range(1,10001):
    num=i
    for j in str(i):
        num+=int(j)
    if(num<=10000):
        if(not checked[num]):
            arr[num]=-1
            checked[num]=1
for i in arr:
    if(i!=-1 and i!=0):
        print(i)


