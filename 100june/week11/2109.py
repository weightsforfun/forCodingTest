import sys    #그리디 알고리즘 몇일안에 여서 3일이라 나와있었어도 1일에 할수있었다 그걸 생각 못함

n=int(sys.stdin.readline())
arr=[]
answer=0
dic={}
for i in range(n):
    p,d=map(int,sys.stdin.readline().split())
    arr.append([d,p])

arr.sort(key=lambda x:-x[1])   # day pay 다 받아와서 pay로 내림차순 wjdfuf

for i in range(n):                       #pay순으로 넣어주면서 만약 그 날에 이미 강의가있다면 그보다 저 전날들음 탐색하면서 빈날이 있으면 넣어준다
    if(not arr[i][0] in dic):
        dic[arr[i][0]]=arr[i][1]
    else:
        for j in range(arr[i][0],0,-1):
            if(not j in dic):
                dic[j]=arr[i][1]
                break;

print(sum(dic.values()))