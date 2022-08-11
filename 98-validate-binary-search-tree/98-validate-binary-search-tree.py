# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        answ = []
        def dfs(node):
            if node == None:
                return
            if node.left:
                dfs(node.left)
                
            answ.append(node.val)

            if node.right:
                dfs(node.right)
                
        dfs(root)
        prev = float("-inf")
        for i in answ:
            if prev >= i:
                return False
            prev = i
        return True