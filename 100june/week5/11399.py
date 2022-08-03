n=int(input())
times=list(map(int,input().split()))

times.sort()

total_time=0
prev_time=0
for i in range(len(times)):
    prev_time+=times[i]
    total_time+=prev_time

print(total_time)