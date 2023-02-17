def solution(n, times):
    answer = 0
    max_time=times[-1]*n
    left=0
    right=max_time
    
    def count_people(value):
        count=0
        for time in times:
            count+=(value//time)
        return count
    
    while(left<=right):
        mid=(left+right)//2
        temp=count_people(mid)
        if(temp<n):
            left=mid+1
        else:
            max_time=min(mid,max_time)
            right=mid-1
    answer=max_time
    return answer