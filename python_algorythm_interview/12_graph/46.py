class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited=[0]*len(nums)
        answer=[]
        
        def dfs(current:list[int]):
            
            if(len(current)==len(nums)):
                answer_temp=current[:]
                answer.append(answer_temp)
                return 
            else:
                for i in range(len(nums)):
                    if(visited[i]==0):
                        current.append(nums[i])
                        visited[i]=1
                        dfs(current)
                        visited[i]=0
                        current.pop()
        
        start=[]
        dfs(start)
        return answer