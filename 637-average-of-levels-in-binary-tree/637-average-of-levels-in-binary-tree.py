# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = [queue[0].val / 1]
        while queue:
            l = len(queue)
            for i in range(l):
                curr = queue.popleft()
                if curr.left and curr.right:
                    queue.append(curr.left)
                    queue.append(curr.right)
                elif curr.left:
                    queue.append(curr.left)
                elif curr.right:
                    queue.append(curr.right)
                else:
                    continue
            if queue:
                ans.append(sum([node.val for node in queue if node]) / len(queue))
            
                
        return ans
        