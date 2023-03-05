import sys
input=sys.stdin.readline
tc=int(input())

def check(start):
    n,m,w=map(int,input().split())
    edges=[]
    distance=[10001]*(n+1)
    distance[start]=0
    for _ in range(m):
        s,e,t=map(int,input().split())
        s-=1
        e-=1
        edges.append((s,e,t))
        edges.append((e,s,t))

    for _ in range(w):
        s,e,t=map(int,input().split())
        s-=1
        e-=1
        edges.append((s,e,-t))
        
            
    for i in range(n):
        for edge in edges:
            s,e,t=edge
            if(distance[s]+t<distance[e]):
                distance[e]=distance[s]+t
                if(i==n-1):
                    print("YES")
                    return ;
    print("NO")
    return ;

   

for i in range(tc):
    check(1)




