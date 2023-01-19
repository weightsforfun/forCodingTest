n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]


dic={}
temp_num=0
while(True):
    if(temp_num**2>int('9'*max(n,m))):
        break
    dic[str(temp_num**2)]=temp_num**2
    temp_num+=1

answer=-1

for i in range(n):
    for j in range(m):
        for x in range(-n,n):
            for y in range(-m,m):
                start=arr[i][j]
                next_x=x
                next_y=y
                while(0<=i+next_x<n and 0<=j+next_y<m):
                    if(next_x==0 and next_y==0):
                        if(start in dic):
                            answer=max(answer,dic[start])
                        break
                    start+=arr[i+next_x][j+next_y]
                    reverse_start=start[::-1]
                    if(start in dic):
                        answer=max(answer,dic[start])
                    if(reverse_start in dic):
                        answer=max(answer,dic[reverse_start])
                    next_x+=x
                    next_y+=y
print(answer)