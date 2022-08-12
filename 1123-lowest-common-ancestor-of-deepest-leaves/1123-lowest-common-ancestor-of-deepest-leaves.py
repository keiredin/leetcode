# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node,depth):
            if not node:
                return (None,depth-1)
            
            if not node.left and not node.right:
                return (node,depth)
            
            leftNode,leftDepth = dfs(node.left,depth+1)
            rightNode,rightDepth = dfs(node.right,depth+1)
            
            if leftDepth > rightDepth:
                return (leftNode,leftDepth)
            elif rightDepth > leftDepth:
                return (rightNode,rightDepth)
            else:
                return (node,leftDepth)
            
             
        return dfs(root,1)[0]
        
        
        
        
        
        
    
        