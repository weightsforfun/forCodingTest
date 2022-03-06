import sys

input=sys.stdin.readline

n,m=map(int,input().split(" "))

requiredTimes={}

for _ in range(n):
    item=int(input())
    if(not item in requiredTimes):
        requiredTimes[item]=1
    else:
        requiredTimes[item]+=1

def maxPeoplePerTime(time):
    global requiredTimes
    totalPeople=0
    for requiredTime in requiredTimes:
        totalPeople+=((time//requiredTime)*requiredTimes[requiredTime])
    return totalPeople

def binarySearch(target):
    left=0
    right=10**18
    answer=0
    while(left<=right):
        mid=(right+left)//2
        if(maxPeoplePerTime(mid)>=target):
            right=mid-1
            answer=mid
        else:
            left=mid+1
    return answer

print(binarySearch(m))


## 얘도 10%에서 시간초과 뜸 시간복잡도 18*10^5인거 같은데 왜 시간초과뜨지
## 처음에는 그냥 배열로 모든 수 나눠줬었는데 시간초과 나서 딕셔너리로 바꿔서 중복되는 수는 그냥 한번 구하고 그 수만큼 곱해주는거로 바꿈
## 근데도 시간초과 나옴 심지어 5%에서 나네 이진 탐색에서 어느정도까지 시간 구해준다음에 마지막ㅇ while로 해주는거에서 시간초과뜨네
## mid 구하고 거기서 최솟값구하는 알고리즘 시간초과 나서 mid를 구하면 left부터 차례로 올리면서 구해주는 알고리즘도 해봤는데 실패
## 어자피 최소한의 시간만 구하면 되는거여서 굳이 일반 이진 탐색처럼 target에 맞게되면 멈출필요없이  left랑 right극한까지 밀어붙이면 됬었네 아쉽다
