from importlib_metadata import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        answer=0
        
        if(len(prices)==0):
            return 0
        else:
            while(right<len(prices)):
                answer=max(answer,prices[right]-prices[left])
                if(prices[left]>prices[right]):
                    left,right=right,right+1
                else:
                    right+=1
            return answer
        