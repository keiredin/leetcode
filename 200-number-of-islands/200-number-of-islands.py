class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction_arr = [[-1,0],[1,0],[0,1],[0,-1]]
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j,direction_arr)
                    count += 1
        return count
    
    def dfs(self, grid, i, j,direction_arr):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1'):
            return 1
            
        grid[i][j] = '#'
            
        for x,y in direction_arr:
            self.dfs(grid,i+x,j+y,direction_arr)
            
        