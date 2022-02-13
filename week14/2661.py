import sys
input=sys.stdin.readline

N=int(input())

flag=0
answer='1'
for i in range(1,N):
    if(answer[i-1]=='1'):
        if(flag):
            answer+='3'
            flag=0
        else:
            answer+='2'
            flag=1
    else:
        answer+='1'


 
print(answer)



## n=8 정도까지 직접 써보면서 구하니까 규칙이 있는거 같아서 /// 1다음 2혹은 3 2,3다음은 무조건 1 이고 2,3은 번갈아가면서 나오는 코드 짜봤는데 틀림 ㅋㅋ
## 나중에 다시보니까 이렇게 하면 좀 길어진상태로 나쁜수열이 되버림 ex) n=8 12131213