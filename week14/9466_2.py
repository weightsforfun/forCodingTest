import sys
input=sys.stdin.readline

t=int(input())



def dfs(index):
    dic={}   ## index마다 안겹치고 각각 값이 있으므로 dictionary를 썼고 해당하는 값을 쭉 따라가다가 dic안에 값이 있으면 어디선가 팀이 만들어 진것이므로 
    while(True):    ## 그 루틴이 생긴것부터 시작해서 쭉 따라가먄서 팀을 만들어준다 
        if(valid[index]==-1 or valid[index]==1):  ## 만약 따라들어갈 사람이 이미 팀을 이뤘거나 아님 이미 팀이루기를 실패한경우
            for i in dic:                          ## 1이 팀을이룸 -1은 팀 절대 못이룸 0은 아직 모름
                valid[i]=-1
            break
        if(index==arr[index]):    ## 여기서 자기 자신을 고른 사람을 발견하면 valid에 1을 넣어준다  팀이라는거니까
            valid[index]=1
            for i in dic: 
                valid[i]=-1
            break  
        if(index in dic):  ## 이곳은 만약 쭉 따라가다가 중복되는 인원이 발견 됬다는것은 어딘가에서 팀이 만들어진 것이므로 그 중복이 시작한 사람부터
            while(True):    ## 하나씩 돌면서 valid에 1을 넣어준다
                if(valid[index]==1):    ## 돌다가 valid에 1을 넣은 index가 나왔다는것은 한바퀴 돌았다는것이므로 나와준다
                    break
                del dic[index]   ## 팀만들어진 애들은 dic에서 빼준다 나중에 dic남아있는 애들 다 -1 넣어줄거임
                valid[index]=1
                index=arr[index]
            for i in dic:       ## 남은 애들은 루틴에 못들어간 애들이므로 절대 팀 못만듬 -1
                valid[i]=-1    
            break
        dic[index]=arr[index]   ## 여기는 그냥 쭉 따라가는 함수이다 만약 여기서 따라가던 사람들이 이미 팀을 만든 사람들을 따라갔거나 자기 자신을 고른 사람들을 따라간거면
        index=arr[index]        ## -1 됐다가 경우에 따라 1로 바뀔거임
        
        

for i in range(t):
    n=int(input())
    answer=0 
    valid=[0]*(n+1)       ## valid에 1이 들어가는 경우는 팀이 완성된 사람들한테 넣어준다 이 사람들은 더이상 돌려볼 이유가 없으므로 걸러줄거임
    arr=[0]+list(map(int,input().split(" ")))
    for j in range(1,len(arr)):    ## 1부터 하나씩 돌린다 하지만 전에 돌리면서 이미 팀이 완성되어 그팀에 포함된 사람은 돌릴 이유가 없으므로 거른다
        if(valid[j]==0):   ## 1이나 -1은 이미 결과를 아므로 들어갈 필요없음
            dfs(j)   
    for j in range(1,len(arr)):  ## 팀에 포함되지 않은 사람 체크해서 총합 print
        if(valid[j]==-1):
            answer+=1
    print(answer)
    
    
##틀렸습니다 떴었음 알고리즘은 맞는데 구현 과정에서 문제가 있었음 반례 넣어보고 어디 구현다시해서 맞음
## 전 알고리즘이랑 다른 부분은 수 따라 들어가기전에 이미 가망이 없는 수거나 팀이 있는수면 안들어가고 -1 넣는거 
## 전 알고리즘은 그걸 고려안했어서 거기서 중복이 일어난듯