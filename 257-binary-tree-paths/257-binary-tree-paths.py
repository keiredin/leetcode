# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.dfs(root, "", res)
        return res
        
    def dfs(self, root, ls, res):
        if root:
            if (not root.left and not root.right):
                ls += (str(root.val))
                res.append(ls)

            self.dfs(root.left, ls + str(root.val) + "->", res)
            self.dfs(root.right, ls + str(root.val) +"->" , res)
        