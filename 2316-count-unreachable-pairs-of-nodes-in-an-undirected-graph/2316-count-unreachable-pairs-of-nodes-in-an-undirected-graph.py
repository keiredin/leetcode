class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
            
        
        def dfs(root, cur_node):
            visited.add(cur_node)
            groups[root].append(cur_node)
            
            for nei in graph[cur_node]:
                if nei not in visited:
                    dfs(root, nei)
          
        
        
        groups = defaultdict(list)
        visited = set()           
        for i in range(n):
            if i not in visited:
                dfs(i,i)
        
        res = 0
        for group in groups:
            n -= len(groups[group])
            res += len(groups[group]) * n
            
        return res
        