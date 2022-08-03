n,m=map(int,input().split())
chessboard=[]
answers=[]
for i in range(n):
    chessboard.append(list(list(input())))

def checkboard(arr):
    count=0
    count2=0
    default=arr[0][0]
    for i in range(0,8):
        for j in range(0,8):
            if((i+j)%2==0):
                if(arr[i][j]!=default):
                    count=count+1
            else:
                if(arr[i][j]==default):
                    count=count+1
    for i in range(0,8):
        for j in range(0,8):
            if((i+j)%2==0):
                if(arr[i][j]==default):
                    count2=count2+1
            else:
                if(arr[i][j]!=default):
                    count2=count2+1
    # print(arr)
    # print(count,count2)
    return min(count,count2)

def make8x8board():
    
    for i in range(0,n-7):
        for j in range(0,m-7):
            newarray=[[chessboard[a][b] for a in range(i,i+8)] for b in range(j,j+8)]
            answers.append(checkboard(newarray))
            
           
           
           

make8x8board()

print(min(answers))





     
