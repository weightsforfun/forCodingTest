from collections import defaultdict,deque
def check_word(wordA,wordB):
    count=0
    for i in range(len(wordA)):
        if(wordA[i]!=wordB[i]):
            count+=1
    if(count==1):
        return True
    else:
        return False
            
def solution(begin, target, words):
    answer = 0
    dic=defaultdict(list)
    que=deque([[begin,0]])
    visited_dic={}
    visited_dic[begin]=1
    
    for word in words:
        if(check_word(begin,word)):
            dic[begin].append(word)
        visited_dic[word]=0
    
    for wordA in words:
        for wordB in words:
            if(check_word(wordA,wordB)):
                dic[wordA].append(wordB)
    
    
    # if(target not in words):
    #     return 0
    
    while(que):
        current,count=que.popleft()
        for word in words:
            if(word in dic[current]):
                if(word==target):
                    return count+1
                else:
                    que.append([word,count+1])
    return answer