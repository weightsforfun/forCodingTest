t=int(input())
for i in range(t):
    n=int(input())
    dic={}
    for i in range(n-1):
        parent,child=map(int,input().split())
        dic[child]=parent
    nodeA,nodeB=map(int,input().split(" "))
    nodeA_arr=[nodeA]
    temp=nodeA
    while(True):
        if(temp not in dic):
            break
        else:
            temp=dic[temp]
            nodeA_arr.append(temp)
            
    
    nodeB_arr=[nodeB]
    temp=nodeB
    while(True):
        if(temp not in dic):
            break
        else:
            temp=dic[temp]
            nodeB_arr.append(temp)
            
    flag=0        
    for A in nodeA_arr:
        if(flag):
            break
        for B in nodeB_arr:
            if(A==B):
                print(A)
                flag=1
                break
    
    