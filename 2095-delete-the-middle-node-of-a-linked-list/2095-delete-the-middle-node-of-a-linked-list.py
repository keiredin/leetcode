# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0, head)
        fast,slow = head, head
        prev = dummy
        while fast and fast.next:
            fast = fast.next.next
            prev = prev.next
            slow = slow.next
        
        prev.next = slow.next
        return dummy.next
        