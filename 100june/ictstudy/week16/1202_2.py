import heapq
import sys
input=sys.stdin.readline
n,k=map(int,input().split(" "))
jewelsWeightsAndValue=[list(map(int,input().split(" "))) for _ in range(n)]
bagsWeight=[int(input()) for _ in range(k)]

jewelsWeightsAndValue.sort()
bagsWeight.sort()

answer=0
getMaxValueforBagWeight=[]


for bagWeight in bagsWeight:
    while(jewelsWeightsAndValue and jewelsWeightsAndValue[0][0]<=bagWeight):
        heapq.heappush(getMaxValueforBagWeight,-jewelsWeightsAndValue[0][1])
        heapq.heappop(jewelsWeightsAndValue)
    if(getMaxValueforBagWeight):
        answer+=heapq.heappop(getMaxValueforBagWeight)
    elif(not jewelsWeightsAndValue):
        break
print(-answer)
## 구글링함 이진탐색을 통해 가장 값비싼 보석을 담을수 있는 가방을 찾는 알고리즘만 생각했는데 
#이 알고리즘은 n^2logn이 최선인듯 구글링한 알고리즘은 가방무게마다 담을수 있는 보석을 우선순위 큐에 넣어서
## 가장 비싼 보석만 가방마다 담아주는 알고리즘임 nlogn정도 나오지 않을까