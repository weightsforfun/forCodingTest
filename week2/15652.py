n,m=map(int,input().split())

def make_sequence(sequence,start):
    if(len(sequence)==m):
        for j in sequence:
            print(j, end=" ")
        print()
        return
    for i in range(start,n+1):
        sequence.append(i)
        make_sequence(sequence,i)
        del sequence[-1]
            

arr=[]
make_sequence(arr,1)