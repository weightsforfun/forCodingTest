class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        answer=[]
        list_digit=list(digits)
        
        def dfs(digs:List[str],original:str,index:int):
            if(len(digs)==index):
                answer.append(original)
                return
            else:
                current=dic[digs[index]]
                for i in current:
                    dfs(digs,original+i,index+1)
        
        if(digits==""):
            return []
        else:
            dfs(list_digit,"",0)
            return answer
                
        