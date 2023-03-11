def solution(routes):
    answer=1
    routes.sort(key=lambda x : x[1])
    target=routes[0][1]
    index=0
    while(index<len(routes)-1):
        index+=1
        if(routes[index][0]<=target):
            continue
        else:
            answer+=1
            target=routes[index][1]

    return answer