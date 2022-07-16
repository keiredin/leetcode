class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        inbound = lambda row,col: 0 <= row < m and 0 <= col < n
       
        @lru_cache(None)
        def dfs(row,col,move):
            # if (row,col) in memo:
            #     return memo[row,col]
            if not inbound(row,col) and move <= maxMove:
                return 1
            if not inbound(row,col) or move > maxMove:
                return 0
            
        
            return (dfs(row-1,col,move+1) + dfs(row+1,col,move+1) + dfs(row,col-1,move+1) + dfs(row,col+1,move+1)) %((10**9)+7)
      
        return dfs(startRow,startColumn,0)
        