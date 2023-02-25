def solution(n, computers):
    answer = 0
    network_index=1
    visited=[0]*n
    for i in range(n):
        if(visited[i]==0):
            visited[i]=network_index
            stack=[i]
            while(stack):
                current=stack.pop()
                for j in computers[current]:
                    if(visited[j]==0):
                        visited[j]=network_index
                        stack.append(j)
            network_index+=1
    answer=max(visited)
    return answer
print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))