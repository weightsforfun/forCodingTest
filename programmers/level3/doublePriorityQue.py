import heapq
def solution(operations):
    answer = []
    current_len=0
    max_heap=[]
    min_heap=[]
    for operation in operations:
        command,num=operation.split(" ")
        if(command=="I"):
            if(current_len==0):
                max_heap=[]
                min_heap=[]
            heapq.heappush(min_heap,int(num))
            heapq.heappush(max_heap,(-1*int(num),int(num)))
            current_len+=1
        else:
            if(num=="-1"):
                if(current_len>0):
                    heapq.heappop(min_heap)
                    current_len-=1
                    
            else:
                if(current_len>0):
                    heapq.heappop(max_heap)
                    current_len-=1
        print(operation,max_heap,min_heap)
    if(current_len==0):
        return [0,0]
    elif(current_len==1):
        item=heapq.heappop(min_heap)
        return [item,item]
    else:
        return [heapq.heappop(max_heap)[1],heapq.heappop(min_heap)]
print(solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]))