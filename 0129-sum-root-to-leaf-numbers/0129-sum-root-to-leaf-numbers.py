# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #bfs
        queue = deque([(root,0)])
        
        res = 0
        while queue:
            curNode,pathSum = queue.popleft()
            
            pathSum = pathSum * 10 + curNode.val
            
            if not curNode.left and not curNode.right:
                res += pathSum
            
            if curNode.left:
                queue.append((curNode.left, pathSum))
            
            if curNode.right:
                queue.append((curNode.right, pathSum))
        
        return res
            
            
            
        return self.findRootToLeafPathNumbers(root,0)
        
    def findRootToLeafPathNumbers(self,node, pathSum):
        if not node:
            return 0
        
        pathSum = pathSum * 10 + node.val
        
        if not node.left and not node.right:
            return pathSum
        
        left = self.findRootToLeafPathNumbers(node.left, pathSum)
        right = self.findRootToLeafPathNumbers(node.right, pathSum)
        
        return left + right
        