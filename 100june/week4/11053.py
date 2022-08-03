cases=int(input())
sequences=list(map(int,input().split(" ")))
lis=[1]*cases

for i in range(cases):
    for j in range(i+1,cases):
        if(sequences[j]>sequences[i]):
            lis[j]=max(lis[i]+1,lis[j])

print(max(lis))