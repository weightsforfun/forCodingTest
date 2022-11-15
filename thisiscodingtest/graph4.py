n=int(input())
class_own_time=[0]*(n+1)
pre_class_time=[[]*(n+1)]
for i in range(1,n+1):
    data=list(map(int,input().split()))
    pre_class_time.append(data[:-1])
    