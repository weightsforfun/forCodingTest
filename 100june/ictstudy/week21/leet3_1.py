class Solution:  #모든 경우의수 다 도는 알고리즘 시간초과뜸
    def longestPalindrome(self, s: str) -> str:
        
        def check_palindromic(arr):
            for i in range(len(arr)//2):
                if(arr[i]!=arr[len(arr)-i-1]):
                    return False
            return True
        answer=0
        answer_j=0
        answer_i=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if(check_palindromic(s[i:j])):
                    if(answer<=j-i+1):
                        answer_j=j
                        answer_i=i
                        answer=j-i+1
        return s[answer_i:answer_j]
    
            