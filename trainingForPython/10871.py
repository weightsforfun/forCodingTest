len,num=map(int,input().split())
arr=input().split()
arr2=[]
for i in arr:
    if(int(i)<num):
        arr2.append(int(i))
for i in arr2:
    print(i, end=" ")
    