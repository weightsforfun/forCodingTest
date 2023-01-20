n=int(input())
arr=[["*"]]
count=1
while(count!=n):
    temp=arr[::]
    if(count==n):
        break
    for i in range(count):
        arr[i]=temp[i]*3
    for i in range(count):
        arr.append(temp[i%3]+[" "]*count+temp[i%3])
    for i in range(count):
        arr.append(temp[i]*3)
    count*=3


for i in range(n):
    print(''.join(arr[i]))
    
            
        