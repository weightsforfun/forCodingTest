cases=int(input())
lines=[[0 for i in range(2)] for i in range(cases)]
lis=[1]*cases
for i in range(cases):
    a,b=input().split(" ")
    lines[i][0]=int(a)
    lines[i][1]=int(b)
lines.sort()
print(lines)
for i in range(len(lines)):
    for j in range(i):
        if(lines[j][1]<lines[i][1]):
            lis[i]=max(lis[i],lis[j]+1)
        print("i:",i,"j:",j,"list:",lis)
print(cases-max(lis))