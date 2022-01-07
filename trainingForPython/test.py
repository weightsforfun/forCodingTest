input() 
a=0 
for i in [*sorted(map(int,input().split()))]: 
    if a+1<i:break 
    a+=i 
print(a+1)

