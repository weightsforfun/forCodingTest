import sys
def input():
    return sys.stdin.readline().rstrip()

n,m=map(int,input().split())

trains=[0]*n

for i in range(m):
    commands=list(map(int,input().split()))
    command=commands[0]
    if(command==1):
        trains[commands[1]-1]=trains[commands[1]-1] | (1<<commands[2]-1)
    elif(command==2):
        trains[commands[1]-1]=trains[commands[1]-1] & ~(1<<commands[2]-1)
    elif(command == 3):
        trains[commands[1]-1]= trains[commands[1]-1] << 1
        trains[commands[1]-1] = trains[commands[1]-1] & ~(1<<20)
    else:
        trains[commands[1]-1]=trains[commands[1]-1] >> 1
print(len(set(trains)))