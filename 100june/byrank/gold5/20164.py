import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

n=input()

max_answer=0
min_answer=float("INF")

def count_odd(count,num):
    global max_answer
    global min_answer
    if(len(num)==1):
        plus=0
        if(int(num)%2!=0):
            plus=1
        max_answer=max(max_answer,count+plus)
        min_answer=min(min_answer,count+plus)
    elif(len(num)==2):
        num_1=int(num[0])
        num_2=int(num[1])
        plus=0
        if(num_1%2!=0):
            plus +=1
        if(num_2%2!=0):
            plus +=1
        count_odd(count+plus,str(num_1+num_2))
    else:
        plus=0
        for i in range(len(num)):
            if(int(num[i])%2!=0):
                plus+=1
        index=[]
        for i in range(1,len(num)):
            index.append(i)
        nCr=combinations(index,2)
        for comb in nCr:
            new_num=int(num[:comb[0]])+int(num[comb[0]:comb[1]])+int(num[comb[1]:])
            count_odd(count+plus,str(new_num))
count_odd(0,n)
print(min_answer,max_answer)