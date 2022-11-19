"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        queue = deque([root]) if root else deque()
        
        while queue:
            previousNode = None
            levelSize = len(queue)
            
            for _ in range(levelSize):
                curNode = queue.popleft()
                
                if previousNode:
                    previousNode.next = curNode
                previousNode = curNode
                
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
        return root
        