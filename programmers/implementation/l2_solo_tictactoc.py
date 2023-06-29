def solution(board):
    count_o=0
    count_x=0


    for i in range(3):
        for j in range(3):
            if(board[i][j]=="O"):
                count_o+=1
            elif(board[i][j]=="X"):
                count_x+=1

    if(count_o<count_x):
        return 0
    elif (count_o==count_x):
        bingo=0
        #세로
        for i in range(3):
            count=0
            for j in range(3):
                if(board[i][j]=="O"):
                    count+=1
                else:
                    break
            if(count==3):
                bingo=1
        #가로
        for i in range(3):
            count=0
            for j in range(3):
                if(board[j][i]=="O"):
                    count+=1
                else:
                    break
            if(count==3):
                bingo=1
        #대각선
        if(board[0][0]==board[1][1]==board[2][2]=="O"
          or board[0][2]==board[1][1]==board[2][0]=="O"):
            bingo=1
        if(bingo):
            return 0
    elif(count_o>count_x):
        bingo=0
        #세로
        for i in range(3):
            count=0
            for j in range(3):
                if(board[i][j]=="X"):
                    count+=1
                else:
                    break
            if(count==3):
                bingo=1
        #가로
        for i in range(3):
            count=0
            for j in range(3):
                if(board[j][i]=="X"):
                    count+=1
                else:
                    break
            if(count==3):
                bingo=1
        #대각선
        if(board[0][0]==board[1][1]==board[2][2]=="X"
          or board[0][2]==board[1][1]==board[2][0]=="X"):
            bingo=1
        if(not count_o-count_x==1 or (count_o-count_x==1 and bingo)):
            return 0

    return 1