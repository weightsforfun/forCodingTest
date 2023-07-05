def solution(board, skill):
    answer = 0
    prefix_sum=[[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    
    for tp,y1,x1,y2,x2,degree in skill:
        if(tp==1):
            degree*=-1
        
        prefix_sum[y1][x1]+=degree
        prefix_sum[y2+1][x2+1]+=degree
        prefix_sum[y2+1][x1]+=-1*degree
        prefix_sum[y1][x2+1]+=-1*degree
    
    for i in range(len(prefix_sum)-1):
        for j in range(len(prefix_sum[0])):
            prefix_sum[i+1][j]+=prefix_sum[i][j]
    
    for j in range(len(prefix_sum[0])-1):
        for i in range(len(prefix_sum)):
            prefix_sum[i][j+1]+=prefix_sum[i][j]    
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+=prefix_sum[i][j]
            if(board[i][j]>0):
                answer+=1
        
    return answer