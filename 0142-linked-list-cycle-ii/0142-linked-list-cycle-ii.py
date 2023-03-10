# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast:
            fast = fast.next and fast.next.next
            slow = slow.next
            if slow == fast:
                break
                
        if fast is None:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow