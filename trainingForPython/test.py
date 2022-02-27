def binary_search(target,array):
    start=0
    end=len(array)-1
    while start<=end:
        mid=(start+end)//2
        if(array[mid][0]==target):
            while(array[mid][1]==1):
                mid+=1
                if(mid==len(array)):
                    return -1
            return mid
        elif(array[mid][0]<target):
            start=mid+1
        else:
            end=mid-1
    end+=1
    while(array[end][1]==1):
        end+=1
        if(end==len(array)):
            return -1
    return end
arr=[[2,0],[3,1],[5,1],[7,1],[9,1]]
print(binary_search(3,arr))