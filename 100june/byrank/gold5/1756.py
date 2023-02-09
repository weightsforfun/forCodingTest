import sys
n,d=map(int,input().split(" "))

oven=list(map(int,input().split(" ")))

pizzas=list(map(int,input().split(" ")))

for i in range(1,len(oven)):
    if(oven[i]>oven[i-1]):
        oven[i]=oven[i-1]

top=0
for i in range(len(oven)-1,-1,-1):
    if(oven[i]<pizzas[top]):
        continue
    top+=1
    if(top>=len(pizzas)):
        print(i+1)
        sys.exit(0)

print(0)
    