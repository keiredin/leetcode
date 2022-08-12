# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (True,target)
            
            left, leftVal = dfs(node.left)
            right, rightVal = dfs(node.right)
            
    
            if left:
                if leftVal == target :
                    node.left = None
                else:
                    left = False
            
            if right:
                if rightVal == target:
                    node.right = None
                else:
                    right = False
            return (left and right, node.val)
            
        dfs(root) 
        root = None if root.val == target and (not root.left and not root.right) else root
        return root
        