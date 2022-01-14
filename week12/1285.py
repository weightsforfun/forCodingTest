import sys
import copy
n=int(sys.stdin.readline())

coins=[]

for i in range(n):
    coins.append(list(sys.stdin.readline().strip()))    

for i in range(n):             #연산할때 편하려고 1,-1로 앞뒤 표시해줌
    for j in range(n):
        if(coins[i][j]=="H"):
            coins[i][j]=1
        else:
            coins[i][j]=-1

start_row=copy.deepcopy(coins)
start_colunn=copy.deepcopy(coins)

def reverse_coin(i,is_row,arr):
    plus=0
    minus=0
    if(is_row==1):
        for j in range(n):
            if(arr[i][j]==1):
                plus+=1
            else:
                minus+=1
        return plus<minus
    else:
        for j in range(n):
            if(arr[j][i]==1):
                plus+=1
            else:
                minus+=1
        return plus<minus

for i in range(n):
    if(reverse_coin(i,1,start_row)):
        for j in range(n):
            start_row[i][j]*=-1
for i in range(n):
    if(reverse_coin(i,0,start_row)):
        for j in range(n):
            start_row[j][i]*=-1

for i in range(n):
    if(reverse_coin(i,0,start_colunn)):
        for j in range(n):
            start_colunn[j][i]*=-1
for i in range(n):
    if(reverse_coin(i,1,start_colunn)):
        for j in range(n):
            start_colunn[i][j]*=-1

sr_count=0
sc_count=0


for i in range(n):
    for j in range(n):
        if(start_colunn[i][j]==-1):
            sc_count+=1
for i in range(n):
    for j in range(n):
        if(start_row[i][j]==-1):
            sr_count+=1
print(min(sr_count,sc_count))