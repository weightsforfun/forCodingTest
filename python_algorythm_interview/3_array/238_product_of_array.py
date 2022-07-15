class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsa=nums[::]
        numsb=nums[::]
        mul=1
        for i in range(len(nums)):
            mul,numsa[i]=mul*numsa[i],mul
        mul=1
        for i in range(len(nums)-1,-1,-1):
            mul,numsb[i]=mul*numsb[i],mul
            
        answer = list(map(lambda x,y: x*y ,numsa,numsb))
        return answer
            
            
            