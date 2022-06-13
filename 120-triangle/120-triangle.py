class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle) - 1
        memo = {}
        def dp(row,col):
            nonlocal m
            if row > m or col > len(triangle[m])-1:
                return 0
            if (row,col) in memo:
                return memo[(row,col)]
            
            memo[(row,col)] = triangle[row][col] + min(dp(row+1,col), dp(row+1,col+1))
            return memo[(row,col)]
        
        return dp(0,0)