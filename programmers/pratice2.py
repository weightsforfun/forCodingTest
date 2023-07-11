T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,r=map(int,input().split(" "))
    coins=list(map(int,input().split(" ")))
    
    total=sum(coins)
    avg=(total)//len(coins)
    coins.sort(reverse=True)
    
    
    right=len(coins)-1
    left=0
	
    while(True):
        
        if(left==right):
            if(left==len(coins)-1):
            	
                break
            
            else:
                left+=1
                right=len(coins)-1
        else:
            count=0
            moveLeft=0
            while(count<r):
                coins[left]-=1
                coins[right]+=1
                count+=1
                if(coins[left]==avg):
                    moveLeft=1
                    break
            if(moveLeft):
                right=len(coins)-1
                left+=1
            else:
                right-=1

    print("#"+str(test_case),min(coins))
        		
    # ///////////////////////////////////////////////////////////////////////////////////