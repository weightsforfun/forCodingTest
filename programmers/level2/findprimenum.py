from itertools import permutations
import math
def is_it_prime(x):
    if(x==0 or x==1):
        return False
    for i in range(2,int(math.sqrt(x) + 1)):
        if x % i == 0:      
            return False
    return True
def solution(numbers):
    answer = 0
    number_list=list(numbers)
    dic={}

    for i in range(1,len(number_list)+1):
        temp=list(permutations(number_list,i))
        for tup in temp:
            string=''.join(tup)
            if(string not in dic):
                dic[int(string)]=int(string)

    for key in dic:
        if(is_it_prime(key)):
            answer+=1

    return answer