from collections import deque
def solution(n, wires):

    answer = 101
    wires.sort()
    arr=[[0]*n for _ in range(n)]


    for s,e in wires:
        s-=1
        e-=1
        arr[s][e]=1
        arr[e][s]=1

    for s,e in wires:
        s-=1
        e-=1
        arr[s][e]=0
        arr[e][s]=0
        count_s=0
        count_e=0
        visited=[0]*n
        visited[s]=1
        visited[e]=1

        deq=deque([s])
        while(deq):
            current=deq.popleft()
            for i in range(n):
                if(arr[current][i]==1 and visited[i]==0):
                    deq.append(i)
                    count_s+=1
                    visited[i]=1

        deq=deque([e])
        while(deq):
            current=deq.popleft()
            for i in range(n):
                if(arr[current][i]==1 and visited[i]==0):
                    deq.append(i)
                    count_e+=1
                    visited[i]=1

        answer=min(answer,abs(count_s-count_e))
        arr[s][e]=1
        arr[e][s]=1


    return answer