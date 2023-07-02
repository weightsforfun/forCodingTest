def solution(scores):
    answer = 0
    wonho=scores[0] ## 원호 배열 빼놓기


    scores.sort(key=lambda x: (-x[0],-x[1]))   ## 인센티브 받을 사람 구분하기 위해 미리 정렬
                                                                     ## [[6,3],[6,2],[5,7],[5,3],[5,1],[3,5],[3,1],[1,2]] 식으로 정렬됌
    new_scores=[] ## 인센티브 받을 사람만 모아놓을 배열 
   
    current_max=0   ## 현재 동료평가 점수 구간에서 비교할 근무 평가 점수
    next_max=0       ## 다음 동료평가 점수 구간에서 비교할 근무 평가 점수
    index=scores[0] ## 동료 평가 점수가 같은 사람들끼리는 근무 점수 비교를 안해도 된다. (둘 다 낮아야 제외하니까)
   
    for score in scores:       ## 인센티브 받을 사람 구분
        if(score[0]!=index):  ## 만약 동료 평가 점수 구간이 달라지면 
            current_max=next_max      ## 이전 동료평가 구간중 가장 높았던 근무 평가 점수를 current_max에 넣는다.
            index=score[0]
        next_max=max(next_max,score[1])   ## 현재 구간 점수는 다음 구간부터 적용 가능
        if(score[1]<current_max):  ## 근무 평가가 낮다면 인센티브 제외
            continue
        else:                                  ## 높다면 인센티브 인원에 포함
            new_scores.append(score)
   
   
    new_scores.sort(key=lambda x:(-(x[0]+x[1]))) ## 인센티브 총합으로 인원 정렬
   

    current_sum=sum(new_scores[0])
    index=1
   
   
    for i in range(len(new_scores)):          ## index 로 순위 부여
        if(current_sum!=sum(new_scores[i])):
            current_sum=sum(new_scores[i])
            index=i+1
        if(wonho==new_scores[i]):  ## 만약 원호 점수면 return 순위
            return index
    return -1  ## 없으면 return -1
           
           
   
   
    return answer
