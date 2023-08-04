import sys

def input():
    return sys.stdin.readline()
flag=0
def dfs(a,b,c,a_index,b_index,c_index):
    
    global flag
    if(c_index==len(c)-1):
        flag=1
        return
    if(flag==1):
        return 
    # print(a[a_index],b[b_index],c[c_index])
     
    if(a[a_index]==c[c_index] and b[b_index]!=c[c_index]):
        dfs(a,b,c,a_index+1,b_index,c_index+1)
    elif(a[a_index]!=c[c_index] and b[b_index]==c[c_index]):
        dfs(a,b,c,a_index,b_index+1,c_index+1)
    elif(a[a_index]==c[c_index] and b[b_index]==c[c_index]):
        dfs(a,b,c,a_index+1,b_index,c_index+1)
        dfs(a,b,c,a_index,b_index+1,c_index+1)
    

n=int(input())


for i in range(n):
    a,b,c=input().split(" ")
    flag=0
    a=a+"@"
    b=b+"@"
    dfs(a,b,c,0,0,0)
    if(flag):
        print("Data Set ",i+1,": Yes")
    else:
        print("Data Set ",i+1,": No")
