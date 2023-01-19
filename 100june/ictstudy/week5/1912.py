num=int(input())
sequences=list(map(int,input().split(" ")))
max_arr=[-1001]*(num+1)

max_arr[0]=sequences[0]

for i in range(1,len(sequences)):
    max_arr[i]=max(max_arr[i-1]+sequences[i],sequences[i])
print(max(max_arr))