# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isStartPath(node, head):
            if not head:
                return True
            if not node:
                return False
            
            return node.val == head.val and (isStartPath(node.left, head.next) or isStartPath(node.right, head.next))
        
        def isSubPath(node, head):
            if not head:
                return True
            if not node:
                return False
            
            return node.val == head.val and isStartPath(node, head) or isSubPath(node.right, head) or isSubPath(node.left, head)
        
        return isSubPath(root,head)
        
            