class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        inbound = lambda r,c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        dir_arr = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        answ = 0
        def dfs(r,c):
            nonlocal answ
            if not inbound(r,c) or grid[r][c] == 0:
                answ += 1
                return
            if (r,c) not in visited:
                visited.add((r,c))
                for d in dir_arr:
                    newR,newC = d
                    dfs(r+newR, c+ newC)
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if (r,c) not in visited:
                        dfs(r,c)
        return answ
                    
        