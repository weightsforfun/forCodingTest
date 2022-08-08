class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        move=[[1,0],[-1,0],[0,1],[0,-1]]
        answer=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    temp=[]
                    temp.append([i,j])
                    while(temp):
                        current_node=temp.pop()
                        grid[current_node[0]][current_node[1]]="-1"
                        for k in range(4):
                            new_y=current_node[0]+move[k][0]
                            new_x=current_node[1]+move[k][1]
                            if(0<=new_y<len(grid) and 0<=new_x<len(grid[0]) and grid[new_y][new_x]=="1"):
                                temp.append([new_y,new_x])
                                
                    answer+=1
        return answer