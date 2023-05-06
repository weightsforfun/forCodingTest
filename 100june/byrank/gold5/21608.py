import sys
input=sys.stdin.readline

n=int(input())
arr=[]
seat=[[-1]*(n+2) for _ in range(n+2)]
moves=[[1,0],[-1,0],[0,1],[0,-1]]
dic={}
for i in range(1,n+1):
    for j in range(1,n+1):
        seat[i][j]=0

for i in range(n**2):
    arr.append(list(map(int,input().rstrip().split())))


def one(friends):
    global n
    result=[[0] * n for _ in range(n)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(seat[i][j]==0):
                for move in moves:
                    x=j+move[0]
                    y=i+move[1]
                    for friend in friends:
                        if(seat[y][x]==friend):
                            result[i-1][j-1]+=1
                            break

    maximum=0

    for i in range(n):
        maximum=max(max(result[i]),maximum)
    # print("max",maximum)
    answer=[]
    for i in range(n):
        for j in range(n):
            if(result[i][j]==maximum and seat[i+1][j+1]==0):
                answer.append((i,j))
    # print(answer)
    return answer
def two(nodes):
    global n
    result=[[0] * n for _ in range(n)]
    for node in nodes:
        i,j=node[0],node[1]
        if(seat[i+1][j+1]==0):
            for move in moves:
                x=j+move[0]+1
                y=i+move[1]+1
                if(seat[y][x]==0):
                    result[i][j]+=1
    maximum=0
    for i in range(n):
        maximum=max(max(result[i]),maximum)

    
    answer=[]
    for i in range(n):
        for j in range(n):
            if(result[i][j]==maximum and seat[i+1][j+1]==0):
                answer.append((i,j))
    return answer


for i in range(len(arr)):
    target=arr[i][0]
    friends=arr[i][1:5]
    # print(target)
    dic[target]=friends
    one_result=one(friends)

    if(len(one_result)>1):
        two_result=two(one_result)

        for y,x in two_result:
            seat[y+1][x+1]=target
            break
            
    else:
        y,x=one_result[0]
        seat[y+1][x+1]=target
    # print("----------------")
    # for i in seat:
    #     print(i)
    # print("----------------")
score=[[0]*(n+2) for _ in range(n+2)]



for i in range(1,n+1):
    for j in range(1,n+1):
        target=seat[i][j]
        friends=dic[target]
        for move in moves:
                x=j+move[0]
                y=i+move[1]
                for friend in friends:
                    if(seat[y][x]==friend):
                        score[i][j]+=1
                        break
answer=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if(score[i][j]==1):
            answer+=1
        elif(score[i][j]==2):
            answer+=10
        elif(score[i][j]==3):
            answer+=100
        elif(score[i][j]==4):
            answer+=1000
print(answer)
                        
        
             


