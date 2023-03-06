n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,list(input()))))

a1=0
a2=0
for i in range(n):
    num=10**(m-1)
    for j in range(m):
        a1+=arr[i][j]*num
        num//=10

for i in range(m):
    num=10**(n-1)
    for j in range(n):
         a2+=arr[j][i]*num
         num//=10
print(max(a1,a2))