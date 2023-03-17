def solution(distance, rocks, n):
    answer = 0
    left=0
    right=1000000000
    rocks.append(distance)
    rocks.sort()
    while(left<=right):
        mid=(left+right)//2
        current=0
        count=0
        shortest=1000000000
        for rock in rocks:
            if(rock-current>=mid):
                shortest=min(shortest,rock-current)
                current=rock
            else:
                count+=1
        if(count>n):          ## 2 9 3 3 4 4 
            right=mid-1


        else:
            left=mid+1
            answer=max(answer,shortest)


    return answer