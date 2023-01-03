import sys
sys.setrecursionlimit(20000)

def solution(n, lighthouse):

    answer = 0
    light=[0 for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]

    for i,j in lighthouse:
        graph[i].append(j)
        graph[j].append(i)

    def dfs(cur):
        if not graph[cur]:
            return

        for next in graph[cur]:
            if light[next]==0:
                light[next]=1
                dfs(next)
                if light[next]==1:
                    light[cur]=2

    dfs(1)
    for i in light:
        if i==2:
            answer+=1


    return answer

lighthouse=[[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]

solution(10,lighthouse)