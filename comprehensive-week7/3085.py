n=int(input())
arr=[]
check=1
max_len=0
for i in range(n):
    arr.append(list(input()))

def checking(li):
    max_count=0
    count=0
    for i in range(len(li)):
        for j in range(i,len(li)):
            if(li[i]==li[j]):
                count+=1
        max_count=max(max_count,count)
        count=0;
    print(max_count)

for i in range(n):
    if(i==0):
        for j in range(j):
            


        
        