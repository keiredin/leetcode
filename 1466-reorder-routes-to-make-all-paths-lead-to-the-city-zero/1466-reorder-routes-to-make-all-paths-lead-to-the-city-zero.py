class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        original_dir = set()
        graph = defaultdict(list)
        
        for a,b in connections:
            original_dir.add((a,b))
            graph[a].append(b)
            graph[b].append(a)
        
    
        visited = set()
        res = 0
        def dfs(node):
            nonlocal res
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    res += (nei,node) not in original_dir
                    dfs(nei)
                    
        dfs(0)
        return res
            
        