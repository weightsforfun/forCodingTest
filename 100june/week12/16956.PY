import sys

r,c=map(int,sys.stdin.readline().split())

fence=[["."]*(c+2)]     #울타리 검색을 편의를 위해 주어진 울타리 밖으로 .만듬
for i in range(r):
    new_arr=(list("."+sys.stdin.readline().strip()+"."))
    fence.append(new_arr)
fence.append(["."]*(c+2))


def check_fence():
    for i in range(1,r+1):
        for j in range(1,c+1):
            if(fence[i][j]=="."):
                fence[i][j]="D"
            if(fence[i][j]=="S"):
                if(fence[i-1][j]=="W"  or fence[i][j-1]=="W"  or fence[i+1][j]=="W"  or fence[i][j+1]=="W"):
                    print(0)
                    return
    print(1)
    for i in range(1,r+1):
        for j in range(1,c+1):
            print(fence[i][j], end="")
        print()


check_fence()

                                 