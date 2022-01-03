import sys       #input 으로는 안되고 sys로는 통과함 개빡침

string_left=list(sys.stdin.readline().strip())
string_right=[]
n=int(sys.stdin.readline())



for i in range(n):
    command=sys.stdin.readline().strip()
    if(command[0]=="L"):
        if(string_left !=[]):
            string_right.append(string_left.pop())
    elif(command[0]=="D"):
        if(string_right !=[]):
            string_left.append(string_right.pop())
    elif(command[0]=="B"):
        if(string_left !=[]):
            string_left.pop()
    else:
        string_left.append(command[2])


print(''.join(string_left+list(reversed(string_right))))