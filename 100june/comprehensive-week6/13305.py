n=int(input())
distances=list(map(int,input().split(" ")))
prices=list(map(int,input().split(" ")))

index=0
price=0
check_end_point=True

while(check_end_point):
    for j in range(index+1,len(prices)):
        if(prices[index]>=prices[j]):#현재 기름값보다 다음 기름값이 비싸면 현재 필요한 기름값만 계산하고 다음 스테이지로 넘어간다
            price+=(prices[index]*distances[index])
            index=j
            if(j==len(prices)-1):#마지막 노드의 기름값은 의미가 없으므로 그냥 끝낸다
                check_end_point=False
            break
        else:#다음 노드 기름값보다 현재 기름값이 싸므로 다음 노드가 필요하는 기름양을 현재 노드의 기름값으로 계산한다
            if(j==len(prices)-1):#그대로 끝나게 되면 지금까지 다음 노드 거리 기름값만 더했으르모 최종 현재 노드 기름값 마지막으로 더해주고 끝난다
                check_end_point=False
                price+=(prices[index]*distances[index])
                break
            price+=(prices[index]*distances[j])

print(price)