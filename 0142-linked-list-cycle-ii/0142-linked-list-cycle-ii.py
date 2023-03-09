# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sett = set()
        
        while head:
            if head.next in sett:
                return head.next
            
            sett.add(head)
            head = head.next
            
        return None
        