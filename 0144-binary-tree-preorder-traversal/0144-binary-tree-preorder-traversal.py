# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root] if root else []
        answ = []
        visitedParent = set()
        
        while stack:
            curr = stack.pop()
            
            if curr.left or curr.right:
                if curr in visitedParent:
                    answ.append(curr.val)
                    visitedParent.remove(curr)
                    continue
                else:                             
                    if curr.right:
                        stack.append(curr.right)
                    if curr.left:
                        stack.append(curr.left)
                    # since preorder is (root -> left -> right)
                    if curr not in visitedParent:
                        visitedParent.add(curr)
                        stack.append(curr)
            else:
                answ.append(curr.val)
        return answ
        