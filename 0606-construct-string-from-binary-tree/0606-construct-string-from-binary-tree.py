# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answ = []
        
        def dfs(node):
            if not node:
                return 
            
            answ.append(str(node.val))
            if node.left:
                answ.append('(')
                dfs(node.left)
                answ.append(')')
                
            if node.right:
                if not node.left:
                    answ.append('()')
                answ.append('(')
                dfs(node.right)
                answ.append(')')
                
                
        dfs(root)
        return "".join(answ)