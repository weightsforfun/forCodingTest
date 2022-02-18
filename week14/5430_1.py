import sys
from collections import deque


input=sys.stdin.readline

def ac(command,arr):
    que=deque()
    is_reversed=False  ## R로인해 뒤집혀있다면 오른쪽에서 숫자를 빼고 아니라면 왼쪽에서 숫자를 빼서 맨 마지막에만 R에따라 배열을 뒤집을지 안뒤집을지 결정한다
    for i in arr:        ## 여기서 이렇게 안하면 시간초과 뜸
        if(i!=''):  ## 만약 배열에 숫자가 없이 들어오면 '' 이런식으로 들어옴 빈배열인지 아닌지 if로 구분함
            que.append(int(i))
    for i in command[:-1]:
        if(i=="R"):         ## R 이 뭐냐에 따라 is_reversed 로 체크해서 D일때 오른쪽에서 뺄지 왼쪽에서 뺄지 결정함
            if(is_reversed):
                is_reversed=False
            else:
                is_reversed=True
        elif(i=="D"):     ## D이면 숫자를 빼줘야하므로 뺘주는데 R에따라 어디서 뺄지 결정함
            if(not que):
                print("error")
                return
            if(is_reversed):
                que.pop()
            else:
                que.popleft()
    if(is_reversed):           ########전체 부분이 출력하는 부분임 배열로 그대로 출력하면 틀려서 이렇게 하나하나 문자열로 만들어서 출력함
        print("[",end='')      ######### 이때도 is_reversed에 따라 정방향으로 출략할지 거꾸로 출력할지 결정을함
        if(que):   ###만약 배열에 아무것도 없으면 그냥 []만 출력하기위해 if로 que안에 숫자가 있는지 없는지 파악 R 0 []이 케이스때문에 계속 틀렸었고
            print(que.pop(),end='')      #####이 케이스 때문에 if(que)사용함 입력 받을때 좀더 예쁘게 받으면 이렇게 할필요 없을듯
            while(que):
                print(",",end='')
                print(que.pop(),end='')
        print("]")
    else:
        print("[",end='')
        if(que):
            print(que.popleft(),end='')
            while(que):
                print(",",end='')
                print(que.popleft(),end='')
        print("]")
    

t=int(input())

for i in range(t):
    command=(input())
    n=int(input())
    arr=input()[1:-2].split(",") #### 문자열이 [1,2,3,4,]\n 이런식으로 들엉호므로 앞에 1 뒤에 2 제거하고 1,2,3,4이런 상태에서 split(,)으로 리스트 만듬
    ac(command,arr)
    
    



## 이번 코드에서는 arr 문자열 조작을 하지않고 str 로 받은 다음에 deque하는 과정에서 처리를 해줄꺼임
## 그리고 que.reverse의 시간 복잡도가 n이니까 reverse는 맨 마지막에 해주고 그냥 여부만 생각해주면서 수를 오른족에서 뺄지 왼쪽에서 뺄지만 체크할꺼임
## 이결과 시간초과는 안떴으나 틀림 혼자서 못찾고 반례 검색하닥 발견했는데 [] 에다가 R 할때는 error가 아니라 그냥 [] 를 출력해야했음