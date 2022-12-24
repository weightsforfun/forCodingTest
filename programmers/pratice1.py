def solution(k, m, score):
    answer = 0
    score.sort()
    for i in range(len(score)//m):
        for j in range(m):
            min_item=score.pop()
        answer+=(min_item*m)
    return answer