from collections import deque
def solution(n, t, m, timetable):
    answer = ''
    timetable_num=[]
    
    for string in timetable:
        num=int(string[0:2])*60+int(string[3:5])
        timetable_num.append(num)
    timetable_num.sort(reverse=True)
    deq=deque(timetable_num)
    
    
    bus_arr=[]
    bus_arrived_time=540
    for i in range(n):
        bus_arr.append([bus_arrived_time])
        bus_arrived_time+=t
    
    
    
    for bus in bus_arr:
        while(len(bus)<=m and deq):
            target=deq[-1]
            if(target>bus[0]):
                break
            else:
                bus.append(deq.pop())
    
    if(len(bus_arr[-1])<m+1):
        a,b=divmod(bus_arr[-1][0],60)
    else:
        bus_arr[-1][-1]-=1
        a,b=divmod(bus_arr[-1][-1],60)   
    
    
    answer=str(a).zfill(2)+":"+str(b).zfill(2)
        
    return answer