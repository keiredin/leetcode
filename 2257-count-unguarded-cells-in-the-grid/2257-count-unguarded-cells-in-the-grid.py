class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        inbound = lambda row,col: 0 <= row < m and 0<= col < n
        dir_arr = [[-1,0],[1,0],[0,-1],[0,1]]
        grid = [[0]*n for _ in range(m)]
        
        for w in walls:
            grid[w[0]][w[1]] = 'W'
            
        for g in guards:
            grid[g[0]][g[1]] = 'G'
            
        for guard in guards:
            for d in dir_arr:
                new_row, new_col = guard[0] + d[0], guard[1] + d[1] 
                while inbound(new_row, new_col) and grid[new_row][new_col] != 'W' and grid[new_row][new_col] != 'G':
                    
                    grid[new_row][new_col] = 'GG'
                    new_row += d[0] 
                    new_col += d[1]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                    
        return count
        
                
                
        