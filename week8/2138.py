n=int(input())
before=list(map(int,input()))
after=list(map(int,input()))

def check(before,after,count):
    for i in range(1,n): 
        if(i==n-1):   #마지막 전구  // 마지막 전구가 원하는 전구가 아닐경우 그 전 전구와 바꿔준다
            if(before[i]!=after[i]):     
                count+=1
                before[i-1]=int(not before[i-1])
                before[i]=int(not before[i])
        else:
            if(before[i-1]!=after[i-1]):    # 마지막 전구가 아닌경우 // 전 전구가 원하는 전구가 아닐때  옆에있는 현재 전구를 건들여서 전 전구를 바꿔준다
                count+=1
                before[i-1]=int(not before[i-1])
                before[i]=int(not before[i])
                before[i+1]=int(not before[i+1])  
        if(before==after):
            print(count)
            return 1
    return 0
before_a=[]+before   #첫 전구를 키지 않은상태로 시작한다
before_b=[]+before    # 첫 전구를 한번 켰다고 생각하고 시작한다
before_b[0]=int(not before_b[0])
before_b[1]=int(not before_b[1]) 



if(not check(before_a,after,0) and not check(before_b,after,1)):  # 만약 두가지 경우중 하나라도 성공하면 그 수를 출력해주고 아니면 -1을 출력해준다
    print(-1)         