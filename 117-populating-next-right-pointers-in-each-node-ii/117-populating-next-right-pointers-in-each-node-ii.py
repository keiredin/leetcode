"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# Time = O(N) - iterate through all the nodes
# Space = O(1) - No additional space 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr=root
        dummy=Node(-999)        
        head=root
        
        while head:
            curr = head   # initialize current level's head
            prev=dummy # init prev for next level linked list traversal
			# iterate through the linked-list of the current level and connect all the siblings in the next level
            while curr:  
                if curr.left:
                    prev.next=curr.left
                    prev=prev.next
                if curr.right:
                    prev.next=curr.right
                    prev=prev.next                                                
                curr=curr.next
            
            head=dummy.next # update head to the linked list of next level
            dummy.next=None # reset dummy node
        return root










# # Time = O(N) - iterate through all the nodes
# #Space=O(L) - As the code is using level order traversal, the maximum size of Queue is maximum number of nodes at any level.

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:
#             return None
#         q = deque()
#         q.append(root)
#         dummy=Node(-999) # to initialize with a not null prev
#         while q:
#             length=len(q) # find level length
            
#             prev=dummy
#             for _ in range(length): # iterate through all nodes in the same level
#                 popped=q.popleft()
#                 if popped.left:
#                     q.append(popped.left)
#                     prev.next=popped.left
#                     prev=prev.next
#                 if popped.right:
#                     q.append(popped.right)
#                     prev.next=popped.right
#                     prev=prev.next                
                 
#         return root

    
