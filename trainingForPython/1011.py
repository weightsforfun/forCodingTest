num=int(input())
distances=[]
answer=[]

for i in range(0,num):
    start,end=map(int,input().split())
    distances.append(end-start)


for distance in distances:
    count=0
    sumofnums=0
    addednum=1
    nextnum=0
    
    while(distance>sumofnums):
        if(nextnum==0):
            sumofnums=sumofnums+addednum
            count=count+1
            nextnum=1
        else:
            sumofnums=sumofnums+addednum
            addednum=addednum+1
            count=count+1
            nextnum=0
    print(count)