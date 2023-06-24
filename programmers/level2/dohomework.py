from collections import deque
def solution(plans):
    answer = []
    for plan in plans:
        h,m=map(int,plan[1].split(":"))
        plan[1]=h*60+m
        plan[2]=int(plan[2])
    plans.sort(key=lambda x : -x[1])
    
    stack=[]
    current_time=0
    while(plans):
        # print("stack: ",stack)
        # print("plans: ",plans)
        print()
        if(not stack):
            stack.append(plans.pop())
        else:
            extra_time=plans[-1][1]-stack[-1][1]
            if(extra_time<stack[-1][2]):
                stack[-1][2]-=extra_time
                stack.append(plans.pop())
            else:
                while(stack):
                    # print("extra_time ",extra_time)
                    if(extra_time>=stack[-1][2]):
                        extra_time-=stack[-1][2]
                        temp=stack.pop()
                        answer.append(temp[0])
                    else:
                        stack[-1][2]-=extra_time
                        stack.append(plans.pop())
                        break
    while(stack):
        item=stack.pop()
        answer.append(item[0])
    return answer