class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque([])
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    visited.add((r,c))
                    queue.append((r,c,0))
                    
        
        
        distance = 0
        direction_arr = [[1,0],[-1,0],[0,1],[0,-1]]
        inBound = lambda r,c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        while queue:
            curR,curC,curDistance = queue.popleft()
            distance = max(distance, curDistance)
            
            for d in direction_arr:
                newR,newC = curR + d[0], curC + d[1]
                
                if inBound(newR,newC) and (newR,newC) not in visited and grid[newR][newC] == 0:
                    visited.add((newR,newC))
                    queue.append((newR,newC,curDistance + 1))
                    
        return distance if distance else -1
            
                
        