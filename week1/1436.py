n=int(input())
count=0
answer=666
while(1):
    if "666" in str(answer):
        count=count+1
        if(count==n):
            print(answer)
            break
    answer=answer+1