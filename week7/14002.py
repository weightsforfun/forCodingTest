cases=int(input())
sequences=list(map(int,input().split(" ")))
arr=[[] for i in range(cases)]

for i in range(cases):
    arr[i].append(sequences[i])

max_arr=arr[0]

for i in range(cases):
    for j in range(i+1,cases):
        if(sequences[j]>sequences[i]):
            if(len(arr[i])+1>len(arr[j])):
                arr[j]=[]+arr[i]
                arr[j].append(sequences[j])
                if(len(arr[j])>len(max_arr)):
                    max_arr=[]+arr[j]

print(len(max_arr))

for i in max_arr:
    print(i,end=" ")
    


