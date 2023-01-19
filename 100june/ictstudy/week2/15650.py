n,m=map(int,input().split()) #내가했던거

def make_sequence(sequence):
    if(len(sequence)==m):
        for j in sequence:
            print(j, end=" ")
        print()
        return
    for i in range(1,n+1):
        if(i in sequence):
            continue
        elif(len(sequence)>=1):
            if(sequence[-1]>i):
                continue
            else:
                sequence.append(i)
                make_sequence(sequence)
                del sequence[-1]
        else:
            sequence.append(i)
            make_sequence(sequence)
            del sequence[-1]
            

arr=[]
make_sequence(arr)
#/////////////////////////////////////////////////////////////////////////////
# n,m=map(int,input().split()) # 다른 방범

# def make_sequence(sequence,start):
#     if(len(sequence)==m):
#         for j in sequence:
#             print(j, end=" ")
#         print()
#         return
#     for i in range(start,n+1):
#         if(i in sequence):
#             continue
#         else:
#             sequence.append(i)
#             make_sequence(sequence,i+1)
#             del sequence[-1]
            

# arr=[]
# make_sequence(arr,1)