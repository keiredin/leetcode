"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = collections.deque([root])
        res = []
        
        while q:
            curLen = len(q)
            curRes = []
            
            for i in range(curLen):
                node = q.popleft()
                
                if node:
                    curRes.append(node.val)
                    for n in node.children:
                        q.append(n)
                    
            if curRes:
                res.append(curRes)
        
        return res
        