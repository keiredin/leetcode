# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0,head)
        
        prev = temp
        while head:
            nex = head.next
            if head.val == val:
                prev.next = nex
                head = nex
            else:
                prev = head
                head = head.next
        
                
        return temp.next
        
                
        
        