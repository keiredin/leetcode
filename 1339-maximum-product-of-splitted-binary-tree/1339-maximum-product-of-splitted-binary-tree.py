# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tSum = 0
        
        def calSum(node):
            nonlocal tSum
            if not node:
                return 
            tSum += node.val
            calSum(node.left)
            calSum(node.right)
            
        calSum(root)
        
        return self.maxResult(tSum,root)[0]  % (10**9 + 7)
        
            
            
            
    def maxResult(self,tSum,node):
        if not node:
            return 0,0
        left = self.maxResult(tSum,node.left)
        right = self.maxResult(tSum,node.right)
        
        subtreeSum = left[1] + right[1] + node.val
        
        return max((tSum - subtreeSum) * subtreeSum, right[0],left[0]), subtreeSum
    
        
        