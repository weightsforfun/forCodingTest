import sys

def input():
    return sys.stdin.readline().strip()

message=input()
key=input()


dic={}
for i in range(26):
    dic[chr(i+ord('A'))]=1

arr=[[0]*5 for _ in range(5)]
index=0


for i in range(len(key)):
    if(dic[key[i]]==1):
        dic[key[i]]+=1
        arr[index//5][index%5]=key[i]
        index+=1


for i in range(26):
    if(dic[chr(i+ord('A'))]==1 and chr(i+ord('A'))!='J'):
        arr[index//5][index%5]=chr(i+ord('A'))
        index+=1


split_message=[]
count=0
while(True):
    if(count>len(message)-1):
        break
    elif(count==len(message)-1):
        split_message.append(message[count]+"X")
        break
    else:
        if(message[count]==message[count+1]):
            if(message[count]=="X"):
                split_message.append(message[count]+"Q")
            else:    
                split_message.append(message[count]+"X")
            count+=1
        else:
            split_message.append(message[count]+message[count+1])
            count+=2
answer=[]        
for i in range(len(split_message)):
    word=split_message[i]
    start=word[0]
    s_y=0
    s_x=0
    end=word[1]
    e_y=0
    e_x=0
    for i in range(5):
        for j in range(5):
            if(arr[i][j]==start):
                s_y=i
                s_x=j
    for i in range(5):
        for j in range(5):
            if(arr[i][j]==end):
                e_y=i
                e_x=j
    if(s_y==e_y):
        start=arr[s_y][(s_x+1)%5]
        end=arr[e_y][(e_x+1)%5]
    elif(s_x==e_x):
        start=arr[(s_y+1)%5][s_x]
        end=arr[(e_y+1)%5][e_x]
    else:
        start=arr[s_y][e_x]
        end=arr[e_y][s_x]
    
    answer.append(start+end)

for i in answer:
    print(i,end='')


