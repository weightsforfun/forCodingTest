n=int(input())
k=int(input())
arr=list(map(int,input().split()))
arr.sort()
distance=[]
for i in range(len(arr)-1):
    distance.append(arr[i+1]-arr[i])
distance.sort()

for _ in range(k-1):
    if(distance):
        distance.pop()
print(sum(distance))
