from collections import deque
def solution(queue1, queue2):
    answer = -2
    limit=len(queue1)*2
    total_len=(len(queue1)+len(queue2))
    total_sum=(sum(queue1)+sum(queue2))
    middle=0
    
    if(total_sum%2==1):
        return -1
    else:
        middle=int(total_sum/2)
    
    sum1=sum(queue1)
    sum2=sum(queue2)
    deq1=deque(queue1)
    deq2=deque(queue2)
    count=0
    while(True):
        if(sum1>sum2):
            pop_item=deq1.popleft()
            deq2.append(pop_item)
            sum1-=pop_item
            sum2+=pop_item
            count+=1
        elif(sum1<sum2):
            pop_item=deq2.popleft()
            deq1.append(pop_item)
            sum1+=pop_item
            sum2-=pop_item
            count+=1
        else:
            return count
        if(count>600000):
            return -1
