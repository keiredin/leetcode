# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            temp.append(node)
            dfs(node.right)
            
        dfs(root)
        srted = sorted(node.val for node in temp)
        for i in range(len(srted)):
            temp[i].val = srted[i]

        return temp[0]
            