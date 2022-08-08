import sys

n=int(sys.stdin.readline())

arr=list(map(int,(sys.stdin.readline().split())))

arr.sort()
answers={}
def recur(index,value):
    
    if(index==len(arr)-1):
        if(not value in answers):
            answers[value]=1
    else:
        recur(index+1,value+arr[index+1])
        recur(index+1,value)


recur(0,0)
recur(0,arr[0])
for i in range((10**6)*2):
    if(not i in answers):
        print(i)
        break;
