if __name__ == '__main__':
    T, W = map(int, input().split())

    # dp[T][W][위치] : T 시간에 W번 이동했을 때 1번(또는 2번)나무에 있을 때 받을 수 있는 자두의 최대 개수 
    dp = [[[0 for _ in range(T)] for _ in range(W+2)] for _ in range(T+1)]
    trees = [] # 자두가 떨어지는 나무 위치 리스트 

    for _ in range(T):
        trees.append(int(input()))

    # 첫 번째 떨어지는 자두에 대한 처리 
    if trees[0] == 1: # 1번 나무일 경우 한 번도 이동하지 않아도 받을 수 있다.
        dp[1][0][1] = 1
    else: # 2번 나무일 경우 한 번 이동해야 받을 수 있다.
        dp[1][1][2] = 1

    # 첫 번째 자두는 처리했으므로 두 번째 자두부터 처리 
    for t in range(2, T+1):
        tree = trees[t-1] 
        
        for w in range(W+1):
            if tree == 1: # 1번 나무일 경우 
                # 1번에 있을 때: max(t-1에 1번에서 움직이지 않은 경우와 t-1에 2번에서 1번으로 이동한 경우)에 +1을 해준다.
                # 2번에 있을 때: max(t-1에 1번에서 2번으로 이동한 경우와 t-1에 2번에서 움직이지 않은 경우)
                dp[t][w][1] = max(dp[t-1][w][1], dp[t-1][w-1][2]) + 1
                dp[t][w][2] = max(dp[t-1][w-1][1], dp[t-1][w][2])
            else: # 2번 나무일 경우 
                # 1번에 있을 때: max(t-1에 1번에서 움직이지 않은 경우와 t-1에 2번에서 1번으로 이동한 경우)
                # 2번에 있을 때: max(t-1에 1번에서 2번으로 이동한 경우와 t-1에 2번에서 움직이지 않은 경우)에 +1을 해준다.
                dp[t][w][1] = max(dp[t-1][w][1], dp[t-1][w-1][2])
                dp[t][w][2] = max(dp[t-1][w-1][1], dp[t-1][w][2]) + 1

    res = -1
    for w in range(W+1):
        res = max(res, max(dp[T][w][1], dp[T][w][2]))

    print(res)