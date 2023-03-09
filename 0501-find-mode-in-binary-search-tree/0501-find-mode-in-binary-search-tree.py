# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cur = [0,0]
        mode = [0, []] # mode = [frequency , [ list of node.val with this frequency]]
        
        def inorder(node):
            nonlocal mode,cur
            if not node:
                return
            
            inorder(node.left)
            
            
            if node.val == cur[1]:
                cur[0] += 1
            else:
                cur = [1, node.val]
                
            if cur[0] > mode[0]:
                mode[0] = cur[0]
                mode[1] = [node.val]
                
            elif cur[0] == mode[0]:
                mode[1].append(node.val)
                
            
            inorder(node.right)
            
        inorder(root)
        return mode[1]
        
        
        