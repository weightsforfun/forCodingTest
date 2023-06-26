from collections import deque
def solution(board):
    answer = 0
    start=[0,0]
    end=[0,0]
    moves=[[1,0],[-1,0],[0,1],[0,-1]]
    
    visited=[[0]* len(board[0]) for _ in range(len(board))] #방문여부 배열
    
    
    for i in range(len(board)):     # 시작점, 도착점 찾기
        for j in range(len(board[0])):
            if(board[i][j]=="R"):
                start[0],start[1]=i,j
            elif(board[i][j]=="G"):
                end[0],end[1]=i,j

    deq=deque()
    
    deq.append([start[0],start[1],0]) # 시작점 deq에 넣기
    visited[start[0]][start[1]]=1 # 방문처리
    
    flag=0
    while(deq):
        current=deq.popleft()
        y=current[0]
        x=current[1]
        count=current[2]

        if(y==end[0] and x==end[1]):  # 도착점일 경우 끝내기
            flag=1
            answer=count
            break
        else:
            for move in moves:
                dy=y+move[0]
                dx=x+move[1]
                while(True):
                    if(0>dy or dy>=len(board) or 0>dx or dx>=len(board[0])): ## 벽에 닿았을 경우 이전 칸을 deq에 넣어준다 그 후 방문처리
                        if(not visited[dy-move[0]][dx-move[1]]):
                            deq.append([dy-move[0],dx-move[1],count+1])
                            visited[dy-move[0]][dx-move[1]]=1
                        break
                    elif(board[dy][dx]=="D"):    ## 장애물에 닿을 경우 이전 칸을 deq에 넣어준다.
                        if(not visited[dy-move[0]][dx-move[1]]):
                            deq.append([dy-move[0],dx-move[1],count+1])
                            visited[dy-move[0]][dx-move[1]]=1
                        break
                    dy+=move[0]
                    dx+=move[1]
    if(not flag):
        return -1
    else:
        return answer 