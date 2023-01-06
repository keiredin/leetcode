class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for road in roads:
            a,b,dist = road
            graph[a].append([b,dist])
            graph[b].append([a,dist])
            
        queue = deque([[1,inf]])
        minPath = inf
        visited = set()
        visited.add(1)
      
        
        
        while queue:
            curCity,dist = queue.popleft()
            minPath = min(minPath, dist)
            
            for neighbor in graph[curCity]:
                if neighbor[0] not in visited:
                    visited.add(neighbor[0])
                    queue.append(neighbor)
                else:
                    minPath = min(minPath, neighbor[1])
                    
                
        return minPath
                