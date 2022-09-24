# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        stack = [root]
        self.count = 0
        self.targetSum = targetSum
        
        # iterate over all the nodes
        while(stack):
            top = stack.pop()
            if top:
                stack.insert(0, top.left)
                stack.insert(0, top.right)
            
            # traverse the tree using each node as root
            self.traverseTree(top, 0)

        return self.count

    def traverseTree(self, curr, summ):
        if not curr:
            return

        summ += curr.val
        if summ == self.targetSum:
            self.count += 1

        self.traverseTree(curr.left, summ)
        self.traverseTree(curr.right, summ)
        
        
#         def dfs(node, target):
#             if node:
#                 return int(node.val == target) + dfs(node.left, target-node.val) + dfs(node.right, target-  node.val)                    
#             return 0
        
#         if root:
#             return dfs(root, targetSum) + dfs(root.left, targetSum) + dfs(root.right, targetSum)
#         return 0
        