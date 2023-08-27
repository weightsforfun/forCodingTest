2.
import sys
si = sys.stdin.readline
S = si().strip()
n = int(si())
words = dict()
for _ in range(n):
    word, score = si().split()
    words[word] = int(score)
L = len(S)
dy = [0 for _ in range(L + 1)]
dy[0] = 0
for i in range(1, L + 1):
    # i 번째 글자를 아무 단어에도 포함시키지 않는 경우
    dy[i] = dy[i - 1] + 1
    # 마지막에 길이가 last_length 만큼을 단어로 나누는 경우
    for last_length in range(1, i + 1):1
        # 마지막 단어 확인
        suffix = S[i - last_length: i]
        # 해당 단어가 입력으로 존재한다면,
        if suffix in words:
            dy[i] = max(dy[i], dy[i - last_length] + words[suffix])
print(dy[L])
3.
import sys
si = sys.stdin.readline
n, m, S, E = map(int, si().split())
visited = [False for _ in range(n)]
con = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, si().split())
    con[x].append(y)
    con[y].append(x)
def backtracking(x, path):
    if x == E:
        print(*path)
        return
    visited[x] = True
    for y in con[x]:
        if visited[y]: continue
        backtracking(y, path + [y])
    visited[x] = False  ####################
backtracking(S, [S])
'''
5 6 0 4
0 1
0 2
1 3
1 4
2 4
3 4
'''



