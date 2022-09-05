# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def maxZigZag(node,direction,maxx):
            if not node:
                return maxx-1
            if direction == 'left':
                return max(maxZigZag(node.right, 'right', maxx+1), maxZigZag(node.left, 'right', 0))
            else:
                return max(maxZigZag(node.left, 'left', maxx+1), maxZigZag(node.right, 'left', 0))
            
        return max(maxZigZag(root,'left',0),maxZigZag(root,'right',0) ,)