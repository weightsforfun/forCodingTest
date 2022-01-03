from itertools import combinations

arr=[]
answer=[]

for i in range(9):
    arr.append(int(input()))

arr_7=list(combinations(arr, 7))

for i in arr_7:
    if(sum(i)==100):
        answer=list(i)
        answer.sort()
        break
for i in answer:
    print(i)

