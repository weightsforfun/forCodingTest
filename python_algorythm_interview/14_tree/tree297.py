# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        answer=[]
        que=collections.deque([root])
        depth=0
        while(que):
            depth+=1
            for i in range(len(que)):
                item=que.popleft()
                if(item is None):
                    answer.append("#")
                else:
                    answer.append(str(item.val))
                    que.append(item.left)
                    que.append(item.right)
       
                
        
        return ' '.join(answer)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='#':
            return None
        nodes=data.split()
        root=TreeNode(int(nodes[0]))
        que=collections.deque([root])
        index=1
        while(que):
            node=que.popleft()
            if(nodes[index] is not '#'):
                node.left=TreeNode(int(nodes[index]))
                que.append(node.left)
            index+=1
            if(nodes[index] is not '#'):
                node.right=TreeNode(int(nodes[index]))
                que.append(node.right)
            index+=1
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))