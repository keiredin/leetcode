# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = -inf
        
        def dfs(node):
            nonlocal maxx
            
            if not node:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            
            curSum = left + right + node.val
            maxx = max(maxx, curSum)
            
            curMax = max(left + node.val, right+node.val )
            
            return curMax
        dfs(root)
        return maxx
    
        