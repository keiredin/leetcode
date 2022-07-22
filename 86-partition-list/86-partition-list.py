# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    
        minimums = ListNode(0,head)
        maxs = ListNode(0,head)
        length = 0
        
        
        pl,pr = minimums,maxs
        while head:
            length += 1
            if head.val < x:
                pl.next = head
                pl = pl.next
            else:
                pr.next = head
                pr = pr.next
            head = head.next
            
        pl.next,pr.next = None,None
    
        pl.next = maxs.next
        
    
        return minimums.next
        
            
        
        
        
                