# 큰거부터 시작해서 차례로 내려가면서 경우의수 다 조사하는 알고리즘 시간초과뜸
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def check_palindromic(arr):
            for i in range(len(arr)//2):
                if(arr[i]!=arr[len(arr)-i-1]):
                    return False
            return True
        answer=0
        answer_j=0
        answer_i=0
        for i in range(len(s),-1,-1):
            for j in range(len(s)-i+1):
                if(check_palindromic(s[j:j+i])):
                    return s[j:j+i]
        
    
            