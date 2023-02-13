class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # check if source and target are not clear cells
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        N = len(grid)            
        dir_arr = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        q = deque([(1, 0, 0)])
        visited = set([1, 0, 0])
        
        inBound = lambda row,col: 0<= row < N and 0 <= col < N and (row,col) not in visited
        
        while q:
            dist, row, col = q.popleft()
            if (row, col) == (N-1, N-1):
                return dist
            for r,c in dir_arr:
                new_r, new_c = row+r, col + c
                if inBound(new_r,new_c) and grid[new_r][new_c] == 0:
                    q.append((dist+1, new_r, new_c))
                    visited.add((new_r, new_c))
        
        return -1  
