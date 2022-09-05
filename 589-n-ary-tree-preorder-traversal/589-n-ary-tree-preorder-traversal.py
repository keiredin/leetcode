"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return 
            res.append(node.val)
            for n in node.children:
                dfs(n)
        dfs(root)
        return res
        