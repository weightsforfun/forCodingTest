def solution(k, tangerine):
    answer = 0
    dic={}
    for i in tangerine:
        if(i in dic):
            dic[i]+=1
        else:
            dic[i]=1
    sorted_dict = sorted(dic.items(), key = lambda item: item[1], reverse = True)
    while(k>0):
        k-=sorted_dict[answer][1]
        answer+=1
    return answer