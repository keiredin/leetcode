class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        memo = {}
        
        def dp(row,col):
            nonlocal m,n
            if row == m and col == n:
                return grid[row][col]
            if row > m or col > n:
                return inf
            if (row,col) in memo:
                return memo[(row,col)]
            
            memo[(row,col)] = grid[row][col] + min(dp(row+1,col), dp(row,col+1))
            return memo[(row,col)]
        
        return dp(0,0)
        