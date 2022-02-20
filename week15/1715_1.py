import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()

init_que=deque()       ## 초기 값들 받아주는 que 여기서 benchmark보다 작은수를 뽑으면서 sum_que에 넣어줌
sum_que=deque()        ## bechmark보다 작은수들은 여기에 넣어서 여기서 가장 작은수 2개를 더해 새로운 becnhmark를 만들어줌
if(n==1):           ## benchmark는 현재 더해진 값으로 이것을 기준으로 정렬을 함
    benchmark=0
else:
    benchmark=arr[0]+arr[1]  ## 처음값 미리 빼줘서 benchmark만들어 놓음
answer=benchmark  

for i in range(2,len(arr)):
    init_que.append(arr[i]) 

for i in range(n-2):
    while(init_que):  ## 현재 더해진 값보다(benchmark) 작은값들 전부 sum que 에 넣어줌
        if(init_que[0]<=benchmark):
            sum_que.append(init_que.popleft())
        else:
            break
    sum_que.append(benchmark)   #brnchmark보다 적으수들 다 넣은후에 benchmark도 넣어줌
    if(len(sum_que)>=2):                  ## 경우에따라 각각의 que에서 숫자를 빼준후 새로운 기준을 만들어준다
        benchmark=sum_que.popleft()+sum_que.popleft()   ## summ_que에 2개 이상이면 그 둘이 가장 작은수니까 더해줌
    elif(len(sum_que)==1):          ## 1이라는건 benchmark하나이고 나머지는 다 크다는것이므로 initque에서 가장 작은수랑 더해줌
        benchmark=sum_que.popleft()+init_que.popleft()
    answer+=benchmark  ##answer에 더해줌
print(answer)
    

