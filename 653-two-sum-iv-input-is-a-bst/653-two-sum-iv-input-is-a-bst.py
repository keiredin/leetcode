# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        l,r = 0, len(res)-1
        
        while l < r:
            summ = res[l] + res[r]
            if summ == k:
                return True
            elif summ > k:
                r -= 1
            else:
                l += 1
        return False
            
        
        