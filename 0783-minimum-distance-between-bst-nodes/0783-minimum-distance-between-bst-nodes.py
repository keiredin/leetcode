# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            nonlocal min_diff,prev
            if node:
                inorder(node.left)
                min_diff = min(min_diff, node.val - prev)
                prev = node.val
                inorder(node.right)        
        prev = float(-inf)
        min_diff = float(inf)
        inorder(root)
        return min_diff
                
        