n,m=map(int,input().split())

def make_sequence(sequence):
    if(len(sequence)==m):
        for j in sequence:
            print(j, end=" ")
        print()
        return
    for i in range(1,n+1):
        if(i in sequence):
            continue
        else:
            sequence.append(i)
            make_sequence(sequence)
            del sequence[-1]
            

arr=[]
make_sequence(arr)