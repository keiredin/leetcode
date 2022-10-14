# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        answ = []
        def dfs(node):
            if not node:
                return 
            
            answ.append(str(node.val))
            if node.left:
                answ.append('(')
                dfs(node.left)
                answ.append(')')
                
            if node.right:
                if not node.left:
                    answ.append('()')
                answ.append('(')
                dfs(node.right)
                answ.append(')')
        dfs(root)
        return "".join(answ)
    

    def deserialize(self, s: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        
        def dfs(i):
            if i >= len(s):
                return None, i

            cur = ""
            while i < len(s) and s[i] not in '()':
                cur += s[i]
                i += 1
           
            node = TreeNode(cur) if cur else None
            if i < len(s) and s[i] == '(':
                i += 1
                node.left, i = dfs(i)

                i += 1
                if i < len(s) and s[i] == '(':
                    i += 1
                    node.right, i = dfs(i)
                    i += 1

            return node, i

        a, i = dfs(0)
        return a
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans