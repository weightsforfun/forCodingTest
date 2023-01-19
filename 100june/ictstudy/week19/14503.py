import sys
input=sys.stdin.readline

n,m=map(int,input().split(" "))
r,c,d=map(int,input().split(" "))

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(" "))))

directions=[[-1,0,1,0],[0,1,0,-1]]
answer=1
def move(x,y,d):
    global answer
    for i in range(4):
        newY=y+directions[0][abs(d+3-i)%4]
        newX=x+directions[1][abs(d+3-i)%4]
        if(arr[newY][newX]==0):
            answer+=1
            arr[newY][newX]=2
            return move(newX,newY,(d+3-i)%4)
    backY=y+directions[0][abs(d+2)%4]
    backX=x+directions[1][abs(d+2)%4]
    if(arr[backY][backX]==1):
        return
    else:
        return move(backX,backY,d)
arr[r][c]=2
move(c,r,d)
print(answer)
## 예제는 맞는데 그냥 바로 틀렸습니다 뜸 왜지
## 처음 청소한곳 체크 안해줌