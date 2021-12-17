n=int(input())
minus_arr=[]
zero_arr=[]
plus_arr=[]
total=0

for i in range(n):#수열을 음수 부분  0  양수부분으로 나누어서 저장한다
    num=int(input())
    if(num<0):
        minus_arr.append(num)
    elif(num>0):
        plus_arr.append(num)
    else:
        zero_arr.append(num)

minus_arr.sort()
plus_arr.sort(reverse=True)


while(len(minus_arr)>1):        #음수 수열을 각 원소끼리 곱해서 최대한 큰 양수로 만들어주고 하나가 남을경우 0있다면 0으로 만들고 없다면 총값에서 음수를 더해준다
    total+=minus_arr[0]*minus_arr[1]
    minus_arr.pop(0)
    minus_arr.pop(0)
if(len(minus_arr)==1 and len(zero_arr)==0):
    total+=minus_arr[0]

while(len(plus_arr)>1):     #양수수열을 내림차순으로 정렬한후 원소가 1이되어 더하는게 더 커지는 경우 전까지 수를 각각 곱해줘서 값을 최대로 만든다
    if(plus_arr[1]==1):
        total+=sum(plus_arr)
        break
    total+=plus_arr[0]*plus_arr[1]
    plus_arr.pop(0)
    plus_arr.pop(0)
if(len(plus_arr)==1):
    total+=plus_arr[0]
    
print(total)







