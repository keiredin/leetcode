# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        answ = 0
        def dfs(node, dirr):
            nonlocal answ
            if not node:
                return 0
            if not node.left and not node.right and dirr == 'left':
                answ += node.val
           
            dfs(node.left, 'left')
            dfs(node.right, 'right')
            
        dfs(root, 'right')
        return answ
            
        