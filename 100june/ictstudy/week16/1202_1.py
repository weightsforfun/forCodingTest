import sys

input=sys.stdin.readline

n,k=map(int,input().split(" "))
jewelsWeightsAndValue=[]
bagsLimitWeight=[]
countFullBag=0
answer=0

for i in range(n):
    jewelsWeightsAndValue.append(list(map(int,input().split(" "))))

for i in range(k):
    bagsLimitWeight.append([int(input()),0])

jewelsWeightsAndValue.sort(key=lambda x:(-x[1],-x[0]))
bagsLimitWeight.sort()



    
def binary_search(target,array):
    start=0
    end=len(array)-1
    while start<=end:
        mid=(start+end)//2
        if(array[mid][0]==target):
            while(array[mid][1]==1):
                mid+=1
                if(mid==len(array)):
                    return -1
            return mid
        elif(array[mid][0]<target):
            start=mid+1
        else:
            end=mid-1
    end+=1
    while(array[end][1]==1):
        end+=1
        if(end==len(array)):
            return -1
    return end

for i in range(n):
    if(countFullBag==k):
        break
    if(jewelsWeightsAndValue[i][0]<=bagsLimitWeight[-1][0]):
        indexOfBag=binary_search(jewelsWeightsAndValue[i][0],bagsLimitWeight)
        if(indexOfBag>=0):
            answer+=jewelsWeightsAndValue[i][1]
            bagsLimitWeight[indexOfBag][1]=1
            countFullBag+=1

print(answer)

##시간초과뜸 이진탐색하고 그 해당하는 index뻬주는거라 nlogn정도라 생각했는데 더걸리나
## 다시 생각해보니까 이진탐색 index해당하는 가방 제거를 보석마다 해주는 거니까 n^2logn이구니
##del 로 바꿨는데도 시간초과뜨네 del도 n임 ㅋㅋ 
##우선순위 큐로 만들어서 index만 구하고 가방무게를 0으로 만들어서 맨아래로 보낸다음 pop으로
##빼주는걸 생각해봤는데 이러면 우선순위 큐는 정렬된것이 아니야서 이진탐색이 불가능해지고 우선순위큐 index접근도 막아놓은듯
## 가방무게 배열을 가방 사용여부까지 체크하는 2중배열로 만들어줬는데 indexerror났음 이진탐색에서 값보다 큰가
## 이진탐색에서 해당하는 배낭을 사용해 다음으로 넘어가다가 끝까지 가면 break해줘야히는데 이때 mid==len() end==len()
##해줘야했는데 mid=len()부분에 end=len()을써서 indexerror뜸 이거 고쳤더니 14%에서 시간초과나옴