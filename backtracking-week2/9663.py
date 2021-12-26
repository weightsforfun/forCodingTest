n=int(input())
col, slash, backSlash = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
count=0


def put_queen(column):
    global count
    for j in range(0,n):
          if not (col[j] or slash[column + j] or backSlash[column - j + n - 1]):
            if(column==n-1):
                count=count+1
            else:
                 col[j] = slash[column + j] = backSlash[column - j + n - 1] = True
                 put_queen(column + 1)
                 col[j] = slash[column + j] = backSlash[column - j + n - 1] = False

put_queen(0)
print(count)        
        