length=int(input())
stair_number=[[0 for i in range(9)] for i in range(length)]

for i in range(9):
    stair_number[0][i]=1
if(length>=2):
    for i in range(9):
        stair_number[1][i]=2
    stair_number[1][8]=1

for i in range(2,length):
    for j in range(9):
        if(j==0):
            stair_number[i][j]=(stair_number[i-2][j]+stair_number[i-1][j+1])
        elif(j==8):
            stair_number[i][j]=(stair_number[i-1][j-1])
        else:
            stair_number[i][j]=(stair_number[i-1][j-1]+stair_number[i-1][j+1])
print(sum(stair_number[length-1])%1000000000)
    