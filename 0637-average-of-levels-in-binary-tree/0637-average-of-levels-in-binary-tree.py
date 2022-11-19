# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []
        while queue:
            l = len(queue)
            curSum = 0
            for _ in range(l):
                curNode = queue.popleft()
                curSum += curNode.val
                if curNode.left:
                    queue.append(curNode.left)
                    
                if curNode.right:
                    queue.append(curNode.right)
                
            
            ans.append(curSum / l)      
        return ans
        