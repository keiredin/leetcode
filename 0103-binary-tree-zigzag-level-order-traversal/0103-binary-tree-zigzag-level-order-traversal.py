# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root]) if root else deque()
        res = []
        
        leftToRight = True
        while queue:
            levelSize = len(queue)
            currentLevel = deque()
            
            for _ in range(levelSize):
                curNode = queue.popleft()
                
                if leftToRight:
                    currentLevel.append(curNode.val)
                else:
                    currentLevel.appendleft(curNode.val)
                
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                    
            res.append(list(currentLevel))
            # reverse the traversal direction
            leftToRight = not leftToRight
            
        return res
        
            
        
        