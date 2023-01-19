height_of_triangle=int(input())
triangle_lines=[]
max_sum_of_lines=[]
for i in range(height_of_triangle):
    triangle_lines.append(list(map(int, input().split())))
for i in range(height_of_triangle):
    arr=[0]*(i+1)
    max_sum_of_lines.append(arr)
# print(triangle_lines)
# print(max_sum_of_lines)
max_sum_of_lines[0][0]=triangle_lines[0][0]


for i in range(1,height_of_triangle):
    for j in range(len(triangle_lines[i])):
        if(j==0):
            max_sum_of_lines[i][j]=triangle_lines[i][j]+max_sum_of_lines[i-1][j]
        elif(j==len(triangle_lines[i])-1):
             max_sum_of_lines[i][j]=triangle_lines[i][j]+max_sum_of_lines[i-1][j-1]
        else:
            max_sum_of_lines[i][j]=triangle_lines[i][j]+max(max_sum_of_lines[i-1][j-1],max_sum_of_lines[i-1][j])

print(max(max_sum_of_lines[height_of_triangle-1]))