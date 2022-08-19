class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer=[]
        nums=[]
        visited=[0]*(n+1)
        
        
        
        def dfs(current:list[int],index:int):
            if(len(current)==k):
                answer.append(current[:])
                return
            else:
                for i in range(index,n+1):
                    if(visited[i]==0):
                        current.append(i)
                        visited[i]=1
                        dfs(current,i+1)
                        visited[i]=0
                        current.pop()
        dfs([],1)
        return answer