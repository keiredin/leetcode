import heapq as hq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newList = []
        dummy = ListNode(0)
        for node in lists:
            while node:
                newList.append(-1 * node.val)
                node = node.next
        
        print(newList)
        hq.heapify(newList)
        head = None
        while newList:
            item = hq.heappop(newList) * -1
            head = self.insert(head, item)
            
        return head
            
            
    def insert(self,root, item):
        temp = ListNode(0)
        temp.val = item
        temp.next = root
        root = temp
        return root
            