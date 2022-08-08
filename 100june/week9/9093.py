n=int(input())
prev=[]
for i in range(n):
    prev.append(input().split(" "))

for i in range(n):
    for j in range(len(prev[i])):
        prev[i][j]=''.join(reversed(prev[i][j]))

for i in range(n):
    for j in prev[i]:
        print(j,end=" ")
    print()