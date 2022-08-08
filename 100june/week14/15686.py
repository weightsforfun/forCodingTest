import sys
from itertools import combinations


input=sys.stdin.readline

n,m=map(int,input().split(" "))

arr=[list(map(int,input().split(" "))) for _ in range(n)]  ## 입력받는 배열 배열을 입력받고 한번 쭉 돌리면서 일반 집과 치킨집 index를 배열에 넣어준다

chicken_store=[]  ## 치킨집 index저장

houses=[] ## 일반집 index저장

answer=2500  ##치킨 거리중 가장 최소값 고르라해서 그냥 초기값으로 50*50 으로 넣어놓음

for i in range(n):   ## 각각 index들 저장
    for j in range(n):
        if(arr[i][j]==1):
            houses.append([i,j])
        elif(arr[i][j]==2):
            chicken_store.append([i,j])

combs=list(combinations(chicken_store,m))  # 치킨집 어디가 폐업하냐에따라 각 집의 치킨거리가 달라지므로 조합 라이브러리를 통해 경우의수 배열을 만듬
 

for comb in combs:  ##  조합들 배열에서 조합 하나씩 돌리면서 그때마다 answer 과 값비교해서 작은값이면 넣어줌
    sum_distance=0  ## answer 과 비교될 값으로 도시의 치킨거리임
    for house in houses:  ## 집들 인덱스를 다 뽑아서 돌려주면서 한집마다 조합상에 있는(폐업하지않은) 치킨집들과의 거리를 구해주면서 
        distance=100      ##제일 작은값을 distance에 넣어주고 sum_distance에 더해줌 100은 그냥 나올수 없는 제일 큰값
        for i in comb:
            distance=min(distance,abs(house[0]-i[0])+abs(house[1]-i[1]))
        sum_distance+=distance
    answer=min(answer,sum_distance)

print(answer) 


## 처음에 무슨 알고리즘으로 풀리 고민하면서 전에 풀었던 문제인 벽부수기를 떠올리며 치킨거리를 미리 구해버리고 나중에 구한 값들로 최소값을 구하는
## dfs bfs도 고민해봤는데 나오는 치킨집 하나가 사라지게 되면 다른 치킨집들이 영향을 받기때문에 단순히 bfs나 dfs로 못풀겠다 생각해서 브루트 포스일거라 추측하고 시간복잡도를 계산했더니
## 가능해서 바로 구함 미리 index를 추출해서 그냥 브루트 포스로 돌릴때보다 시간을 조금 줄여줌