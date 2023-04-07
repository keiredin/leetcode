class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited_1 = set()
        
        def dfs(row,col):
            if grid[row][col] == 1:
                visited_1.add((row,col))
                
            for d in direction_arr:
                newR = row + d[0]
                newC = col + d[1]
                if in_bound(newR,newC) and grid[newR][newC] == 1 and (newR,newC) not in visited_1:
                    dfs(newR,newC)
            return
          
        direction_arr = [[1,0],[-1,0],[0,1],[0,-1]]    
        in_bound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        for col in range(n):
            if grid[0][col] == 1:
                dfs(0,col)
                
        for col in range(n):
            if grid[m-1][col] == 1:
                dfs(m-1,col)
                
        for row in range(m):
            if grid[row][0] == 1:
                dfs(row,0)
                
        for row in range(m):
            if grid[row][n-1] == 1:
                dfs(row,n-1)
        
        count = 0       
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row,col) not in visited_1:
                   count += 1
        return count
        