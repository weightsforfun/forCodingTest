n=int(input())
conferences=[[0,0]]
for i in range(n):
    start,end=map(int,input().split(" "))
    conferences.append([start,end])

conferences.sort(key=lambda x: (x[1], x[0]))

count=1
endtime=conferences[1][1]

for i in range(2,len(conferences)):
    if(conferences[i][0]>=endtime):
        endtime=conferences[i][1]
        count+=1

print(count)


    
