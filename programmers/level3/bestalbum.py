

def solution(genres, plays):
    answer = []
    dic={}
    
    for i in range(len(plays)):
        if(genres[i] in dic):    
            dic[genres[i]].append([i,plays[i]])
        else:
            dic[genres[i]]=[[i,plays[i]]]
    
    arr=[]
    
    for dic_key in dic:
        dic[dic_key].sort(key=lambda x:(x[1],-x[0]))
        print(dic)
        if(len(dic[dic_key])>=2):
            arr.append([dic[dic_key][-1][1]+dic[dic_key][-2][1],dic[dic_key][-2][0],dic[dic_key][-1][0]])
        else:
            arr.append([dic[dic_key][-1][1],dic[dic_key][-1][0]])
    
    arr.sort(key=lambda x:x[0],reverse=True)
    print(arr)
    for i in arr:
        while(len(i)>1):
            answer.append(i.pop())
    return answer
g=["a","a","a","c","b","b","a"]
p=[200,300,200,1,300,150,500]

print(solution(g,p))