# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node,depth):
            if not node:
                return (None,depth)
            
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
            
            if left[1] == right[1]:
                return (node, left[1])
            elif left[1] > right[1]:
                return left
            
            return right
        
        return dfs(root,0)[0]
                
        
        
        