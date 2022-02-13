import sys
input=sys.stdin.readline

t=int(input())



def dfs(arr,index):
    dic={}   ## index마다 안겹치고 각각 값이 있으므로 dictionary를 썼고 해당하는 값을 쭉 따라가다가 dic안에 값이 있으면 어디선가 팀이 만들어 진것이므로 
    while(True):    ## 그 루틴이 생긴것부터 시작해서 쭉 따라가먄서 팀을 만들어준다 
        if(index==arr[index]):    ## 여기서 자기 자신을 고른 사람을 발견하면 valid에 1을 넣어준다 
            valid[index]=1
            break
        if(index in dic):  ## 이곳은 만약 쭉 따라가다가 중복되는 인원이 발견 됬다는것은 어딘가에서 팀이 만들어진 것이므로 그 중복이 시작한 사람부터
            while(True):    ## 하나씩 돌면서 valid에 1을 넣어준다
                if(valid[index]==1):    ## 돌다가 valid에 1을 넣은 index가 나왔다는것은 한바퀴 돌았다는것이므로 나와준다
                    break
                valid[index]=1
                index=arr[index]
            break
        valid[index]=-1
        dic[index]=arr[index]   ## 여기는 그냥 쭉 따라가는 함수이다 만약 여기서 따라가던 사람들이 이미 팀을 만든 사람들을 따라갔거나 자기 자신을 고른 사람들을 따라간거면
        index=arr[index]        
        

for i in range(t):
    n=int(input())
    answer=0 
    valid=[0]*(n+1)       ## valid에 1이 들어가는 경우는 팀이 완성된 사람들한테 넣어준다 이 사람들은 더이상 돌려볼 이유가 없으므로 걸러줄거임
    arr=[0]+list(map(int,input().split(" ")))
    for j in range(1,len(arr)):    ## 1부터 하나씩 돌린다 하지만 전에 돌리면서 이미 팀이 완성되어 그팀에 포함된 사람은 돌릴 이유가 없으므로 거른다
        if(valid[j]==0):
            dfs(arr,j)   
    for j in range(1,len(arr)):  ## 팀에 포함되지 않은 사람 체크해서 총합 print
        if(valid[j]==-1):
            answer+=1
    print(answer)
    
    
##82퍼 가자마자 갑자기 시간초과 뜸