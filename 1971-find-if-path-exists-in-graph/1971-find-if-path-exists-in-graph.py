class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        queue = deque([source])
        visited = set()
        
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            if cur == destination:
                return True
            
            for neighbour in graph[cur]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    
        return False
                
        