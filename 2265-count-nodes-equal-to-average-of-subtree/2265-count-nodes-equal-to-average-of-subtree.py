# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0,0
            leftSum,leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)
            if (leftSum + rightSum + node.val) // (leftCount + rightCount + 1) == node.val:
                res += 1
            return ((leftSum + rightSum + node.val), (leftCount + rightCount + 1))
        
        dfs(root)
        return res
            
        