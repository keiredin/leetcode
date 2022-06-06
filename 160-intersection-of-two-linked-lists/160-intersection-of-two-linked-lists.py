# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # approach 1 - space O(n)
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         sA = set()
        
#         while headA:
#             sA.add(headA)
#             headA = headA.next
            
        
#         while headB:
#             if headB in sA:
#                 return headB
#             headB = headB.next
#         return
    
    # approach 2 - two pointer - space O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one
            
        