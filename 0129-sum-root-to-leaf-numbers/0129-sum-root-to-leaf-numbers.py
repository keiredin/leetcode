# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.findRootToLeafPathNumbers(root,0)
        
    def findRootToLeafPathNumbers(self,node, pathSum):
        if not node:
            return 0
        
        pathSum = pathSum * 10 + node.val
        
        if not node.left and not node.right:
            return pathSum
        
        left = self.findRootToLeafPathNumbers(node.left, pathSum)
        right = self.findRootToLeafPathNumbers(node.right, pathSum)
        
        return left + right
        