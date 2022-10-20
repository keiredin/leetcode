class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        reachableNodes = 0
        restricted = set(restricted)
        visited = set()
        answ = 0
        
        graph = defaultdict(list)
        
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        def dfs(node):
            nonlocal answ
            if node in restricted:
                return
            
            answ += 1
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            
                    
        dfs(0)
        return answ