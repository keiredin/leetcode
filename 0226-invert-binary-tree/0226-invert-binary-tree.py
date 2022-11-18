# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
    
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             node.left, node.right = node.right, node.left
    #             stack.extend([node.right, node.left])
    #     return root
            
                    
                