import sys
                     # 탐욕으로 풀었으나 dp bfs둘다 가능했었음
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split(" ")))
count=0
def dojump(index,jump):
    global count
    if(index==n-1):
        print(count)
        return ;
    highest=0
    check_index=0
    if(index+jump<n-1):
        count+=1
        if(jump==0 and index!=n-1):
            print(-1)
            return ;
        for i in range(index+1,index+jump+1):
            if(highest<=arr[i]+i):
                check_index=i
                highest=arr[check_index]+check_index
        dojump(check_index,arr[check_index])
    else:
        count+=1
        print(count)    

dojump(0,arr[0])