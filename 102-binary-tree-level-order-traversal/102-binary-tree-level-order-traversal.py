# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        res = []
        
        while q:
            curLen = len(q)
            curRes = []
            
            for i in range(curLen):
                node = q.popleft()
                
                if node:
                    curRes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if curRes:
                res.append(curRes)
        
        return res
        