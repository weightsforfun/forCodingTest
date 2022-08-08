cases=int(input())
arr=[]
fibo=[0] *41
fibo[0]=0
fibo[1]=1
for i in range(cases):
    a=int(input())
    arr.append(a)

def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1): 
        return 1
    elif(fibo[n]!=0):
        return fibo[n]
    else: 
        fibo[n]=fibonacci(n-1)+fibonacci(n-2)
        return fibo[n]
for i in (arr):
    if(i==0):
        print(1, 0)
    elif(i==1):
        print(0, 1)
    else:
        print(fibonacci(i-1),fibonacci(i))
