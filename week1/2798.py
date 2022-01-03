amount,maximum=map(int,input().split())
numbers=list(map(int, input().split(" ")))
numbers=sorted(numbers, reverse=True)
sumofnumbers=[]

def findNumber(sumofnumbers):
    for i in range(0,len(numbers)-2):
        for j in range(i+1,len(numbers)-1):
            for k in range(j+1,len(numbers)):
               sumofnumbers.append(numbers[i]+numbers[j]+numbers[k])
    sumofnumbers=sorted(sumofnumbers,reverse=True)
    for i in sumofnumbers:
        if(i<=maximum):
            print(i) 
            return          

findNumber(sumofnumbers)