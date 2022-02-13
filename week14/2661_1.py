import sys
input=sys.stdin.readline

n=int(input())
flag=0

def check(string):     ## 좋은 수열인지 아닌지 판별하는 함수
    limit=len(string)//2          ## 어자피 비교할수있는 최대 길이는 총길이의 절반이므로 //2로 최대값 정해줌
    for i in range(1,limit+1):  ##  길이가 1 2 3 4 ....n//2 까지 전부 비교
        for j in range(0,len(string)-i):    ## index돌려줌 0부터 끝에서 비교하는 수열의 길이만큼 빼준곳까지
            if(string[j:j+i]==string[j+i:j+(2*i)]):
                return False      ## 만약 같은게 나오면 바로 false
    return True
def dfs(string,index):         ##string은 수열 index는 길이를 나타내는 인자임
    global flag     ## 만약 최솟값을 찾게되면 나머지 dfs들은 들어갈 필요가 없으므로 flag=1이면 더이상 들어가지않음
    global n          ##인덱스랑 입력받은 n이랑 비교
    if(flag==0):        ## flag 0일때만 탐색  
        if(check(string)):     #3 여기서 좋은 수열인지 아닌지 탐색
            if(index==n):       ## 만약 길이가 n이면 그게 정답
                flag=1
                print(string)    ##아니면 dfs로 쭉 탐색
            dfs(string+"1",index+1)
            dfs(string+"2",index+1)
            dfs(string+"3",index+1)

dfs("",0)

## 그래서 일단 탐색을 끝가지 들어가봐야겠다고 생각했고 어자피 가장 작은수를 구하ㅣ는거라 dfs로 1,2,3 순서대로 들어가면서 만약 처음 n길이의 숫자가 나오면
## 그게 최솟값이므로 flag라는 변수로 최솟값을 찾으면 스택에 쌓여있는 다른 dfs들은 최대한 빠르게 탈출하게 해주었다.