# from collections import Counter
# n,k=map(int,input().split(" "))
# arr=list(map(int,input().split(" ")))

# start,end=0,0
# answer=0
# while(end<n):
#     answer=max(answer,end-start)
#     temp_counter=Counter(arr[start:end+1])
#     max_count=max(temp_counter.values())
#     if(max_count>k):
#         start+=1
#     else:
#         end+=1

# print(answer)
#########################################
n,k=map(int,input().split(" "))
arr=list(map(int,input().split(" ")))
count=[0]*(max(arr)+1)

start,end=0,0
answer=0
while(end<n):
    if(count[arr[end]]>=k):
        count[arr[start]]-=1
        start+=1
    else:
        count[arr[end]]+=1
        end+=1
    answer=max(answer,end-start)
print(answer)

