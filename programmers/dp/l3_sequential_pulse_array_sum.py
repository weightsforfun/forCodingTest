def solution(sequence):
    answer = 0
    sequence_1=[]
    sequence_2=[]

    for i in range(len(sequence)):
        if(i%2==0):
            sequence_1.append(sequence[i]*1)
            sequence_2.append(sequence[i]*-1)
        else:
            sequence_1.append(sequence[i]*-1)
            sequence_2.append(sequence[i]*1)

    end=0
    temp_sum=0
    while(end<len(sequence)):
        temp_sum+=sequence_1[end]
        if(temp_sum<0):
            temp_sum=0
            end+=1
        else:
            answer=max(answer,temp_sum)
            end+=1
    end=0
    temp_sum=0
    while(end<len(sequence)):
        temp_sum+=sequence_2[end]
        if(temp_sum<0):
            temp_sum=0
            end+=1
        else:
            answer=max(answer,temp_sum)
            end+=1


    return answer