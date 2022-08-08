first=input()
second=input()
matrix=[[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(len(first)):
    for j in range(len(second)):
        if(first[i]==second[j]):
            matrix[i+1][j+1]=matrix[i][j]+1
        else:
            matrix[i+1][j+1]=max(matrix[i+1][j],matrix[i][j+1])
print(matrix[len(first)][len(second)])