# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self,head: 'ListNode', n: int) -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        # fast runner moves n step first
        for i in range(n):
            fast = fast.next
        # slow and fast moves together
        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return dummy.next
    
    
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         prevNode = ""
#         node = head
#         count = 1
#         while node and node.next:
#             count += 1
#             node = node.next
#         if (count==n):
#             head = head.next
#             return head

#         value = count - n + 1
#         node = head
#         while value > 1:
#             prevNode = node
#             node = node.next
#             value -= 1
#         prevNode.next = node.next
#         node = None
#         return head