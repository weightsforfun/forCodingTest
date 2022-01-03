import sys
from itertools import combinations

arr=[]

while(True):
    a=list(sys.stdin.readline().split())
    if(a[0]=="0"):
        break
    arr.append(a)
    
for i in arr:
    result=list(combinations(i[1:],6))
    for j in result:
        for k in j:
            print(k,end=" ")
        print()
    print()

