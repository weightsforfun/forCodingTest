# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total_sum=0
        que=collections.deque([root])
        while(que):
            item=que.popleft()
            if(item==None):
                continue
            else:
                if(low<=item.val<=high):
                    self.total_sum+=item.val
                if(item.right and item.val<=high):
                    que.append(item.right)
                if(item.left and item.val>=low):
                    que.append(item.left)
        return self.total_sum