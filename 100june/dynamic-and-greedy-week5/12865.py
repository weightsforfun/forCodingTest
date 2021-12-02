cases,boundary=map(int,input().split(" "))

stuffs=[];

max_value=[0]*100000

for i in range(cases):
    stuff=[0,0]
    stuff[0],stuff[1]=map(int,input().split(" "))
    stuffs.append(stuff)
    
stuffs.sort()

for i in range(len(stuffs)):
    for j in range(i+1,len(stuffs)):
        if(stuffs[i][0]+stuffs[j][0]<=boundary):
            max_value[stuffs[i][0]+stuffs[j][0]]=max(max_value[stuffs[i][0]+stuffs[j][0]],stuffs[i][1]+stuffs[j][1])
            

print(max(max_value[0:boundary+1]))
        


