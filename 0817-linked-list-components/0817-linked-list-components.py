# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        uniqueNums = set(nums)
        
        connected = 0
    
        while head:
            if head.val in uniqueNums and (not head.next or head.next.val not in uniqueNums):
                connected += 1
            head = head.next
            
        return connected
        