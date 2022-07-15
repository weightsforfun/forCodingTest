num=int(input())
answers=[]

def made_sum(num):
    num_list=list(str(num))
    sum_of_list=0
    for i in num_list:
        sum_of_list=sum_of_list+int(i)
    return sum_of_list

def find_num():
    for i in range(0,num):
        if(i+made_sum(i)==num):
            print(i)
            return
    print(0)

find_num()