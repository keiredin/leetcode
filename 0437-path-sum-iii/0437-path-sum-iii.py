# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, target, curPath):
            
            
            if not node:
                return 0
            
            curPath.append(node.val)
            pathCount, pathSum = 0, 0 
            
            for i in range(len(curPath)-1,-1,-1):
                pathSum += curPath[i]
                
                if pathSum == target:
                    pathCount += 1
            
            
            
            pathCount += dfs(node.left, target, curPath) # left = dfs(node.left, target, curPath) # or 
            pathCount += dfs(node.right, target, curPath) # right = dfs(node.right, target, curPath) # or 
            
            curPath.pop()
            
            return pathCount # return pathCount + left + right

                        
        
        if root:
            return dfs(root, targetSum,[])
        else: return 0
        
        
        
        
        
        
#         pathCount = 0
        
#         def dfs(node, target, curPath):
#             nonlocal pathCount
            
#             if not node:
#                 return 0
            
#             curPath.append(node.val)
#             pathSum = 0
            
#             for i in range(len(curPath)-1,-1,-1):
#                 pathSum += curPath[i]
                
#                 if pathSum == target:
#                     pathCount += 1
            
            
            
#             left = dfs(node.left, target, curPath)
#             right = dfs(node.right, target, curPath)
            
#             curPath.pop()

                        
        
#         if root:
#             dfs(root, targetSum,[])
#         return pathCount
    
    
#         stack = [root]
#         self.count = 0
#         self.targetSum = targetSum
        
#         # iterate over all the nodes
#         while(stack):
#             top = stack.pop()
#             if top:
#                 stack.insert(0, top.left)
#                 stack.insert(0, top.right)
            
#             # traverse the tree using each node as root
#             self.traverseTree(top, 0)

#         return self.count

#     def traverseTree(self, curr, summ):
#         if not curr:
#             return

#         summ += curr.val
#         if summ == self.targetSum:
#             self.count += 1

#         self.traverseTree(curr.left, summ)
#         self.traverseTree(curr.right, summ)
        
        
        