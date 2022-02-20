import sys
input=sys.stdin.readline

n=int(input())

arr=[]

for i in range(n):
    arr.append(int(input()))
    
arr.sort()

if(len(arr)==2):
    print(sum(arr))
elif(len(arr)==1):
    print(0)
else:
    answer=(arr[0]+arr[1])*(n-1)
    for i in range(2,n):
        answer+=(arr[i]*(n-i))
    print(answer)
    
##8%에서 틀림
## n=1일때 0이나라서 그런줄 알았는데 고쳐도 틀림 하지만 n=1일때 0처리 해줘야하는건 맞는듯
## 작은거부터 더하는게 무조건 좋은게 아닌 이유는 작은거 2개합이 뒤에 숫자보다 크다면 뒤에 숫자를 중복시켜주는게 이득이라