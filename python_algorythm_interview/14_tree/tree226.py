class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que=collections.deque([root])
        
        if(root is None):
            return root
        while(que):
            target=que.popleft()
            if(target):
                target.left,target.right=target.right,target.left
                que.append(target.left)
                que.append(target.right)
        return root
                
         
                