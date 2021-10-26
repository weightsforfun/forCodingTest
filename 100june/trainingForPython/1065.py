num=input()

def conclude(value):
    value=str(value)
    diff=int(value[1])-int(value[0])
    for i in range(2,len(str(value))):
        if(int(value[i])-int(value[i-1])!=diff):
            return 0;
    return 1;
def find(num):
    if(int(num)<=99):
        return num
    elif(int(num)<=110):
        return 99
    count=0
    for i in range(111,int(num)+1):
        if(conclude(i)):
            count=count+1
    return 99+count

print(find(num))