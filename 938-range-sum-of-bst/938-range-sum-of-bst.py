# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        inc_order = []
        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
                
            inc_order.append(node.val)

            dfs(node.right)
                
        dfs(root)
        answ = 0
        for i in range(len(inc_order)):
            if inc_order[i] >= low and inc_order[i] <= high:
                answ += inc_order[i]
        return answ
            
        