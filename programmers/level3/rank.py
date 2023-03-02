def solution(n, results):
    answer = 0
    arr=[[0]*n for _ in range(n)]
    for result in results:
        arr[result[0]-1][result[1]-1]=1
        arr[result[1]-1][result[0]-1]=-1
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(arr[j][i]==1 and arr[i][k]==1):
                    arr[j][k]==1
                    arr[k][j]==-1
                if(arr[j][i]==-1 and arr[i][k]==-1):
                    arr[j][k]=-1
                    arr[k][j]=1
    for i in arr:
        count=i.count(0)
        if(count==1):
            answer+=1
    return answer