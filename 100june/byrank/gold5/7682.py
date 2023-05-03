import sys
input=sys.stdin.readline

def bingo(arr,str):
    for i in range(3):
        if(arr[3*i]==arr[(3*i)+1]==arr[(3*i)+2] and arr[3*i]==str):
            return True
        elif(arr[i]==arr[i+3]==arr[i+6] and arr[i]==str):
            return True
    if(arr[0]==arr[4]==arr[8]==str):
        return True
    if(arr[2]==arr[4]==arr[6]==str):
        return True
    return 0
    

def checkTTT(arr):
    count_o=0
    count_x=0
    for i in arr:
        if(i=="O"):
            count_o+=1
        elif(i=="X"):
            count_x+=1
    bingo_x=bingo(arr,"X")
    bingo_o=bingo(arr,"O")
    if(bingo_x and not bingo_o):
        return count_o+1==count_x
    elif(bingo_o and not bingo_x):
        return count_o==count_x
    elif(not bingo_x and not bingo_o and count_o+count_x==9):
        return count_o+1==count_x
    else:
        return 0
    
 
while(True):
    ttt=input().rstrip()
    if(ttt=="end"):
        break
    else:
        if(checkTTT(ttt)):
            print("valid")
        else:
            print("invalid")