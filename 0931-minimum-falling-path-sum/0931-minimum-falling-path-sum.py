class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        inBound = lambda r,c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        
        memo = {}
        def dfs(row,col):
            if (row,col) in memo:
                return memo[row,col]
            
            if row == len(matrix)-1:
                return matrix[row][col]
            
            minSum = inf
            for newC in range(-1,2):
                if inBound(row+1,newC+col):
                    minSum = min(minSum, dfs(row+1,newC+col))
            
            memo[row,col] = matrix[row][col] + minSum if minSum != inf else matrix[row][col]
            
            return memo[row,col]
        
        minSum = inf
        for col in range(len(matrix[0])):
            minSum = min( minSum, dfs(0, col))
        
        return minSum