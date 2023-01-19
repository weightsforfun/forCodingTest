import sys
from itertools import combinations
input=sys.stdin.readline
n=int(input())
statsArray=[list(map(int,input().split(" "))) for _ in range(n)]

arr=[]
for i in range(n):
    arr.append(i)

TeamCaseCanBeMade=list(combinations(arr,n//2))

def getSumOfStat(teamMember):  ## 조합으로 만든 팀 구성원 넣어주면 그 팀의 시너지값을 return함
    global statsArray
    SumofStat=0
    for i in range(0,len(teamMember)):
        for j in range(i+1,len(teamMember)):  
            SumofStat+=(statsArray[teamMember[i]][teamMember[j]]+statsArray[teamMember[j]][teamMember[i]])
    return SumofStat


diff=1001  # 나올수있는 차의 최대값+1
for i in range(len(TeamCaseCanBeMade)//2): ## 만들어진 모든 조합중 반만 해도 상태딤이 그 절반이니까 반만돌린다 i우리팀 -1-i반대편부터 상대팀으로 차이구해줌
    diff=min(diff,abs(getSumOfStat(TeamCaseCanBeMade[i])-getSumOfStat(TeamCaseCanBeMade[-i-1])))
                        
print(diff)
## 팀 누구 선택하냐에 따라 다 달라지기때문에 브루트포스라 생각함 예시도 너무 적었고 그다음부터는 그냥 구현 문제