# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if(root is None):
                return 0
            q=deque()
            depth=1
            q.append([root,depth])
            answer=0
            while(q):
                item,depth=q.popleft()
                if(item is not None and item.left is not None):
                    q.append([item.left,depth+1])
                if(item is not None and item.right is not None):
                    q.append([item.right,depth+1])
                answer=max(answer,depth)
            return answer
                    
            
            