n,k=map(int,input().split(" "))
weights_kits=list(map(int,input().split(" ")))
weight_now=500
answers=0
check_weights_kit=[]
for i in range(n):
    check_weights_kit.append(0)
    
    
def do_weights(index,n,k):
    global weight_now
    global answers
    if(index==n): #다됐을경우 결과+1
        answers=answers+1
        return ;
    else:
        for i in range(n):
            if(check_weights_kit[i]==0): #이미 사용했는지 안했는지 여부 조사
                if(weight_now+weights_kits[i]-k>=500): #이 키트로 운동을 했을때 500아래로 내려가는지 안내려가는지 여부 조사
                    weight_now=weight_now+weights_kits[i]-k
                    check_weights_kit[i]=1
                    do_weights(index+1,n,k) # 이 날은 통과 다음날로 감
                    weight_now=weight_now-weights_kits[i]+k
                    check_weights_kit[i]=0 #전 날로 돌아가 다른경우의 수를 보기위해 위 코드로 설정했던것들 롤백
                else:
                    continue

do_weights(0,n,k)
print(answers)
