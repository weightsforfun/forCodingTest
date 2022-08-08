cases,boundary=map(int,input().split(" "))

stuffs=[[0,0]];

max_value=[[0]*(boundary+1) for _ in range(cases+1)]

for i in range(cases):
    stuff=[0,0]
    stuff[0],stuff[1]=map(int,input().split(" "))
    stuffs.append(stuff)

for i in range(cases+1):
    for j in range(boundary+1):
        weights=stuffs[i][0]
        value=stuffs[i][1]
        if(j>=weights):
            max_value[i][j]=max(max_value[i-1][j-weights]+value,max_value[i-1][j])
        else:
            max_value[i][j]=max_value[i-1][j]

print(max_value[cases][boundary])
        
    
