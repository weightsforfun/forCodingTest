cases=int(input())
sequences=list(map(int,input().split(" ")))
lbis=[[1 for i in range(cases)] for i in range(2) ]

for i in range(len(sequences)):
    for j in range(i):
        if(sequences[i]>sequences[j]):
            lbis[0][i]=max(lbis[0][i],lbis[0][j]+1)

for i in range(len(sequences)-1,-1,-1):
    for j in range(i,len(sequences)):
        if(sequences[i]>sequences[j]):
            lbis[1][i]=max(lbis[1][i],lbis[1][j]+1)
maximum=0
for i in range(len(sequences)):
    maximum=max(lbis[0][i]+lbis[1][i],maximum)
print(maximum-1)
