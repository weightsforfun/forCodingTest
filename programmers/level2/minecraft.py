def solution(picks, minerals):
    answer = 0
    count=sum(picks)
    new_minerals=[]
    total=[]
    if(len(minerals)>count*5):
        new_minerals=minerals[:count*5]
        for i in range((len(new_minerals)//5)):
            total.append([0,0,0])
    else:
        new_minerals=minerals[:]
        for i in range((len(new_minerals)//5)+1):
            total.append([0,0,0]) 

    for i in range(len(new_minerals)):
        if(new_minerals[i]=="diamond"):
            total[i//5][0]+=1
        elif(new_minerals[i]=="iron"):
            total[i//5][1]+=1
        else:
            total[i//5][2]+=1

    total.sort(key=lambda x: (x[0],x[1],x[2]))

    index=0
    while(total and sum(picks)!=0):
        if(picks[index]==0):
            index+=1
        else:
            current=total[-1]
            if(index==0):
                answer+=sum(current)
            elif(index==1):
                answer+=current[0]*5
                answer+=current[1]+current[2]
            else:
                answer+=current[0]*25
                answer+=current[1]*5
                answer+=current[2]
            total.pop()
            picks[index]-=1


    return answer