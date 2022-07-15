def longestPalindrome(s: str) -> str:
        answer=""
        #odd
        for i in range(len(s)):
            if(len(s)==0):
                answer=s[i]
            l,r=i-1,i+1
            while(l>=0 and r<=len(s)-1):
                    print(l,r)
                    if(s[l]!=s[r]):
                        break
                    else:
                        if(len(answer)<r-l+1):
                            answer=s[l:r+1]
                    l-=1
                    r+=1
        #even
        for i in range(len(s)-1):
            if(s[i]==s[i+1]):
                l,r=i,i+1
                while(l>=0 and r<=len(s)-1):
                    if(s[l]!=s[r]):
                        break
                    else:
                        if(len(answer)<r-l+1):
                            answer=s[l:r+1]
                    l-=1
                    r+=1
                           
        return answer
