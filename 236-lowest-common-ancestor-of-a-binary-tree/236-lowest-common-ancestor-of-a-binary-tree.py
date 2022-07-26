# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        def dfs(node):
            nonlocal result
            if not node:
                return False,False
            left = dfs(node.left)
            right = dfs(node.right)
           
            l_answ, r_answ = False,False
            l_answ = left[0] or node.val == p.val or right[0] 
            r_answ = right[1] or node.val == q.val or left[1] 

            if l_answ == True and r_answ == True and result == None:
                result = node
  
            return l_answ,r_answ
            
        dfs(root)
        return result
            
            
        