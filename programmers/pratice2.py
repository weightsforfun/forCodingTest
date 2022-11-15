def solution(arrayA, arrayB):
    answer = 0
    
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    
    def arr_gcd(arr):
        if(len(arr)>=2):
            temp=gcd(arr[0],arr[1])
            for i in range(2,len(arr)):
                temp=gcd(temp,arr[i]) 
            return temp
        else:
            return arr[0]
    
    
    
    stop=0
    max_a=arr_gcd(arrayA)
    max_b=arr_gcd(arrayB)
    
    for i in arrayB:
        if(i%max_a==0):
            break
    else:
        answer=max(answer,max_a)
    
    for i in arrayA:
        if(i%max_b==0):
            break
    else:
        answer=max(answer,max_b)        
    
    return answer