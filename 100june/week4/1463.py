number=int(input())
count_calculate=[0]*1000001
count_calculate[1]=0
count_calculate[2]=1
count_calculate[3]=1

for i in range(4,number+1):
    case1=0
    case2=0
    case3=0
    if(i%3==0 and i%2==0):
        case1=count_calculate[int(i//3)]+1
        case2=count_calculate[int(i//2)]+1
        case3=count_calculate[i-1]+1
        count_calculate[i]=min(case1,case2,case3)
    elif(i%3==0):
        case1=count_calculate[int(i//3)]+1
        case3=count_calculate[i-1]+1
        count_calculate[i]=min(case1,case3)
    elif(i%2==0):
        case2=count_calculate[int(i//2)]+1
        case3=count_calculate[i-1]+1
        count_calculate[i]=min(case2,case3)
    else:
        case3=count_calculate[i-1]+1
        count_calculate[i]=case3

print(count_calculate[number])