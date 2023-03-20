arr=[1,3,5,10,14,17,18,19,23]
def binary_search(start,end,target):
    global arr
    while(start<=end):
        mid=(start+end)//2
        print("start",start,"end:",end,"mid:",mid,"arr[mid]:",arr[mid])
        if(target==arr[mid]):
            return mid
        elif(target<arr[mid]):
            end=mid-1
        else:
            start=mid+1
    print(start,end,mid)
    return start
binary_search(0,len(arr)-1,11)
    