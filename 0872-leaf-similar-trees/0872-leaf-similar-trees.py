# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        res = []
        def inorder(node):
            if not node:
                return 
            if not node.left and not node.right:
                res.append(node.val)
            inorder(node.left)
            inorder(node.right)
            
        inorder(root1)
        inorder(root2)
        
        l,r = 0, len(res)// 2
        while r < len(res):
            if res[l] != res[r]:
                return False
            l += 1
            r += 1
        return True
    
            
            
        