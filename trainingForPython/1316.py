num=int(input())
count=0
words=[]
def discern(word):
    word=list(word.strip(" "))
    for i in range(1,len(word)):
        if(word[i]!=word[i-1]):
            for j in range(i,len(word)):
                if(word[i-1]==word[j]):
                    return 0
    return 1

    


for i in range(0,num):
    word=input()
    words.append(word)


for word in words:
    count=discern(word)+count
print(count)

