import heapq
def solution(n, k, enemy):
    answer = 0
    passed_route=[]
    for i in enemy:
        heapq.heappush(passed_route,(-i,i))
        if(n-i<0):
            if(k>0):
                max_node=heapq.heappop(passed_route)[1]
                k-=1
                n+=max_node
            else:
                break
        n-=i
        answer+=1
    return answer