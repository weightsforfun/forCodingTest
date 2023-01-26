import copy
import collections
import sys
d,p=map(int,(input().split(" ")))

pipes=[]
distance_dic=collections.OrderedDict()

for i in range(p):
    pipes.append(list(map(int,input().split(" "))))

pipes.sort(reverse=True)

distance_dic[0]=sys.maxsize


while(pipes):
    if(pipes[-1][0]>d):
        break
    temp_dic=copy.deepcopy(distance_dic)
    
    current=pipes.pop()
    
    for key in temp_dic:
        print(key)
        if(current[0]+key>d):
            break
        if(current[0]+key in temp_dic):
            distance_dic[key+current[0]]=max(temp_dic[current[0]+key],min(current[1],temp_dic[key]))
        else:
            distance_dic[key+current[0]]=min(current[1],temp_dic[key])
    print(temp_dic,current)
    
print(distance_dic[d])
# for pipe in pipes:
#     for i in range(d,pipe[0]-1,-1):
#         dp[i]=max(dp[i],min(dp[i-pipe[0]],pipe[1]))
#         print(i,pipe,dp)
# print(dp[d])