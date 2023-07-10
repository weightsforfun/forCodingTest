import copy
diff=0
def dfs(depth,left,sum_a,sum_l,info,arrows,answer):
    global diff
    if(depth==11):
        if(diff<sum_l-sum_a):
            diff=sum_l-sum_a
            for i in range(len(arrows)):
                answer[i]=arrows[i]
        elif(diff>0 and diff==(sum_l-sum_a)):
            flag=0
            for i in range(10,-1,-1):
                if(answer[i]<arrows[i]):
                    flag=1
                    break
                elif(answer[i]==arrows[i]):
                    continue
                else:
                    break
            if(flag):
                for i in range(len(arrows)):
                    answer[i]=arrows[i]

        return 
    for i in range(left+1):
        arrows[depth]=i
        if(info[depth]>=i):
            if(info[depth]!=0):
                sum_a+=(10-depth)
        else:
            sum_l+=(10-depth)

        dfs(depth+1,left-i,sum_a,sum_l,info,arrows,answer)

        if(info[depth]>=i):
            if(info[depth]!=0):
                sum_a-=(10-depth)
        else:
            sum_l-=(10-depth)

def solution(n, info):
    answer = [0]*11
    dfs(0,n,0,0,info,[0]*11,answer)
    if(sum(answer)==0):
        return [-1]
    return answer
