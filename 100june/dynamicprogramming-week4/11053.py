cases=int(input())
sequences=list(map(int,input().split(" ")))
lis=[1]*cases

for i in range(1,cases):
    for j in range(i):
        if(sequences[j]<sequences[i]):
            lis[i]=max(lis[i],lis[j]+1)
print(max(lis))