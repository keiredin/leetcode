# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        def build_graph(parent, node):
            if not node: return 
            
            if parent:
                graph[parent.val].append(node)
                graph[node.val].append(parent)
            
            build_graph(node, node.left)
            build_graph(node, node.right)
        
        build_graph(None, root)
        
        vis = set()
        max_infection = 0
        queue = deque([(start, 0)])
        vis.add(start)
        
        while queue:
            node_val, time = queue.popleft()
            max_infection = max(max_infection, time)
            
            for nei in graph[node_val]:
                if nei.val not in vis:
                    vis.add(nei.val)
                    queue.append((nei.val, time + 1))
        
        return max_infection