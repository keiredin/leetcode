# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # using bfs - aka level-order-traversal
        answ = []
        q = collections.deque([root])
        
        while q:
            rightMostEle = None
            curqLen = len(q)
            
            for i in range(curqLen):
                node = q.popleft()
                
                # since the queue may contain null
                if node:
                    rightMostEle = node
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightMostEle:
                answ.append(rightMostEle.val)
                
        return answ
            