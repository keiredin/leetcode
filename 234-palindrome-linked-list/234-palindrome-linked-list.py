# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def helper(node):
            nonlocal head
            if not node.next:
                return node.val == head.val
            temp = helper(node.next)
            head = head.next
            return temp and (node.val == head.val)
        
        return helper(head)
        