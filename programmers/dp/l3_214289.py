def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    start=0
    end=0
    
    for i in range(len(onboard)):
        if(onboard[i]==1):
            end=i
    current_time=0
    
    init=0
    if(temperature<t1):
        init=abs(t1-temperature)
    else:
        init=abs(temperature-t2)
    
    start=init
    answer+=(init*a)
    
    if(a>2*b):
        cost=b
        answer+=(cost*(end-start))
    else:
        cost=a
        if(a>b):
            if((end-start)%2!=0):
                answer+=b
                answer+=(cost*((end-start-1)//2))
            else:
                answer+=(cost*((end-start+1)//2))
        else:
            answer+=(cost*((end-start+1)//2))            
    
    return answer