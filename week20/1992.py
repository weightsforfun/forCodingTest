import sys
input=sys.stdin.readline
n=int(input())
arr=[list(input().strip()) for _ in range(n)]


    

def checkTile(size,startY,startX):
    if(size==2):
        if(arr[startY][startX]==arr[startY][startX+1] and arr[startY][startX]==arr[startY+1][startX] and  arr[startY][startX]==arr[startY+1][startX+1]):
            return arr[startY][startX]
        else:
            return "("+arr[startY][startX]+arr[startY][startX+1]+arr[startY+1][startX]+arr[startY+1][startX+1]+")"
    else:
        size=size//2
        if(checkTile(size,startY,startX)==checkTile(size,startY,startX+size) and checkTile(size,startY,startX)==checkTile(size,startY+size,startX) and checkTile(size,startY,startX)==checkTile(size,startY+size,startX+size) and (checkTile(size,startY,startX)=="1" or checkTile(size,startY,startX)=="0")):
            return checkTile(size,startY,startX)
        else:
            return "("+checkTile(size,startY,startX)+checkTile(size,startY,startX+size)+checkTile(size,startY+size,startX)+checkTile(size,startY+size,startX+size)+")"
    
print(checkTile(n,0,0))

#크게봤을때는 같지만 작게보면 다를수도있다
