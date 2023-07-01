def solution(scores):
    answer = 0
    wonho=scores[0]
    scores.sort(key=lambda x: (-x[0],-x[1]))
    new_scores=[]
    
    current_max=0
    next_max=0
    index=scores[0]
    for score in scores:
        if(score[0]!=index):
            current_max=next_max
            index=score[0]
        next_max=max(next_max,score[1])
        if(score[1]<current_max):
            continue
        else:
            new_scores.append(score)
    
    
    new_scores.sort(key=lambda x:(-(x[0]+x[1])))
    

    current_sum=sum(new_scores[0])
    index=1
    
    
    for i in range(len(new_scores)):
        if(current_sum!=sum(new_scores[i])):
            current_sum=sum(new_scores[i])
            index=i+1
        if(wonho==new_scores[i]):
            return index
    return -1
            
            
    
    
    return answer