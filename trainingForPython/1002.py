import math

case_count=int(input())
answers=[]

def checkcase(x1,y1,r1,x2,y2,r2):
    distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if(x1==x2 and y1==y2 and r1==r2):
        return -1
    elif(max(r1,r2)>distance):
        # print('inner')
        if(distance+min(r1,r2)==max(r1,r2)):
            # print("1")
            return 1
        elif(distance+min(r1,r2)>max(r1,r2)):
            return 2
        else:
            # print("0")
            return 0
    else:
        # print("outside")
        if(distance<r1+r2):
            # print("0")
            return 2
        elif(distance==r1+r2):
            # print("1")
            return 1
        else:
            # print("2")
            return 0
for i in range(0,case_count):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    answers.append(checkcase(x1,y1,r1,x2,y2,r2))
for i in answers:
    print(i)