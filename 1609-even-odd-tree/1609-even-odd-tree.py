# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0
        
        while queue:
            curLen = len(queue)
            if level % 2 == 0:
                prev = 0
            else:
                prev = inf
        
            for _ in range(curLen):
                curNode = queue.popleft()
                
                if level % 2 == 0 and (curNode.val <= prev or curNode.val % 2 == 0):
                    return False
                elif level % 2 == 1 and (curNode.val >= prev or curNode.val % 2 == 1):
                    return False
                
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
                
                prev = curNode.val         
            level += 1
            
            
        return True
                
                
                