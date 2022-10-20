# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.dfs(root)
        return max(res)
    
    
    def dfs(self, node):
        if not node:
            return 0,0
        
        l_child, l_gchild = self.dfs(node.left)
        r_child, r_gchild = self.dfs(node.right)
        
        return (max(l_child + r_child,l_gchild + r_gchild + node.val), l_child + r_child )
    
    
        