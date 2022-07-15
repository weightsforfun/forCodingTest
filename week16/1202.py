import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split(" "))
jewelsWeightsAndValue=[]
bagsLimitWeight=[]
bagsLimitWeightDeque=deque()
answer=0

for i in range(n):
    jewelsWeightsAndValue.append(list(map(int,input().split(" "))))

for i in range(k):
    bagsLimitWeight.append(int(input()))

jewelsWeightsAndValue.sort(key=lambda x:(-x[1],-x[0]))
bagsLimitWeight.sort()

for i in bagsLimitWeight:
    bagsLimitWeightDeque.append(i)

    
def binary_search(target,array):
    start=0
    end=len(array)-1
    while start<=end:
        mid=(start+end)//2
        if(array[mid]==target):
            return mid
        elif(array[mid]<target):
            start=mid+1
        else:
            end=mid-1
    return end+1

for i in range(n):
    if(not bagsLimitWeightDeque):
        break
    if(jewelsWeightsAndValue[i][0]<=bagsLimitWeightDeque[-1]):
        indexOfBag=binary_search(jewelsWeightsAndValue[i][0],bagsLimitWeightDeque)
        answer+=jewelsWeightsAndValue[i][1]
        bagsLimitWeightDeque.rotate(-1*indexOfBag)
        bagsLimitWeightDeque.popleft()
        bagsLimitWeightDeque.rotate(indexOfBag)

print(answer)

##시간초과뜸 이진탐색하고 그 해당하는 index뻬주는거라 nlogn정도라 생각했는데 더걸리나
## 다시 생각해보니까 이진탐색 index해당하는 가방 제거를 보석마다 해주는 거니까 n^2logn이구니