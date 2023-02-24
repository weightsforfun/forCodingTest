from heapq import heappush,heappop

def solution(jobs):
    answer = 0
    count,current_time,start=0,0,-1
    heap=[]
    while(count<len(jobs)):
        for job in jobs:
            if(start<job[0]<=current_time):
                heappush(heap,[job[1],job[0]])
        
        if(len(heap)>0):
            current_job=heappop(heap)
            start=current_time
            current_time+=current_job[0]
            
            answer+=(current_time-current_job[1])
            count+=1
        else:
            current_time+=1
                
    return answer//len(jobs)