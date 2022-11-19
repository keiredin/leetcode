# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        queue = deque([root]) 
        minDepth = 1
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                curNode = queue.popleft()
                
                if not curNode.left and not curNode.right:
                    return minDepth
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                    
            minDepth += 1
        
        return minDepth
        