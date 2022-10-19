# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head 
        slow = head
        temp = head
        length = 0
        
        if not head:
            return head
        
        
        while temp:
            length += 1
            temp = temp.next
            
        k %= length
        if k == 0:
            return head
            
        
        
        while  k:
            fast = fast.next
            k -= 1
            
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        newHead = slow.next
        slow.next = None
        fast.next = head
        
        return newHead 
        