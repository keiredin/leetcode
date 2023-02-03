# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = defaultdict(list)
        
        queue = [ (root, 0, 0) ]
        
        while queue:
            node, col, depth = queue.pop(0)
            if not node: continue
            results[(col,depth)].append(node.val)
            results[(col,depth)].sort()
            queue.extend( [ (node.left, col-1, depth+1), (node.right, col+1, depth+1) ] )
            
            
        res = defaultdict(list)
        keys = sorted(list(results.keys()), key=lambda x: (x[0], x[1]))
        
        
        for k in keys:
            col, depth = k
            res[col].extend(results[k])

        return res.values()