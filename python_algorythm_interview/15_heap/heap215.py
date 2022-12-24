class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        answer=0
        for i in nums:
            heapq.heappush(heap,-1*i)
        for i in range(k):
            answer=-1*heapq.heappop(heap)
        return answer