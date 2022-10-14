# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtreeCount = defaultdict(int)
        answ = []
        def dfs(node):
            if not node:
                return [None]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            res = tuple([node.val, *left, *right])
            
            if subtreeCount[res] == 1:
                answ.append(node)
                
            subtreeCount[res] += 1
            
            return res
            
            
            
        dfs(root)
        return answ
        
        