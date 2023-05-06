import sys
def input():
    return sys.stdin.readline().rstrip()

arr=[]
for i in range(19):
    arr.append(list(map(int,input().split())))

def check_mate():
    for i in range(19):
        for j in range(19):
            if(arr[i][j]==1 or arr[i][j]==2):
                
                # 가로
                count=0
                for k in range(1,6):
                    if(j+k>18 or arr[i][j]!=arr[i][j+k]):
                        break
                    count+=1
                for k in range(1,6):
                    if(j-k<0 or arr[i][j]!=arr[i][j-k]):
                        break
                    count+=1
                if(count==4):
                    return (i,j,arr[i][j])
                
                # 세로
                count=0
                for k in range(1,6):
                    if(i+k>18 or arr[i][j]!=arr[i+k][j]):
                        break
                    count+=1
                for k in range(1,6):
                    if(i-k<0 or arr[i][j]!=arr[i-k][j]):
                        break
                    count+=1
                if(count==4):
                    return (i,j,arr[i][j])
                
                #대각선 오른쪽
                count=0
                for k in range(1,6):
                    if((i+k>18 or j+k >18)  or arr[i][j]!=arr[i+k][j+k]):
                        break
                    count+=1
                for k in range(1,6):
                    if((i-k<0 or j-k<0)  or arr[i][j]!=arr[i-k][j-k]):
                        break
                    count+=1
                if(count==4):
                    return (i,j,arr[i][j])
                
                #대각선 왼쪽
                count=0
                last_i=0
                last_j=0
                for k in range(1,6):
                    if((i+k>18 or j-k<0)  or arr[i][j]!=arr[i+k][j-k]):
                        break
                    count+=1
                    last_i=i+k
                    last_j=j-k
                for k in range(1,6):
                    if((i-k<0 or j+k>18)  or arr[i][j]!=arr[i-k][j+k]):
                        break
                    count+=1
                if(count==4):
                    return (last_i,last_j,arr[i][j])
    return 0

if(check_mate()==0):
    print(0)
else:
    i,j,color=check_mate()
    print(color)
    print(i+1,j+1)
                
                
                
                
                