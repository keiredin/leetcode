from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        all_keys = set()
        
        
        # Find the starting position and all keys
        start_r, start_c = -1,-1
        keys_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#':
                    if grid[i][j] == '@':
                        start_r, start_c = i,j

                    elif grid[i][j].isalpha():
                        if grid[i][j].islower():
                            keys_count += 1
                    all_keys.add((i,j))

                    
        
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inBound = lambda r,c: 0 <= r < m and 0 <= c < n
        queue = deque([(start_r, start_c, [], 0)])
        visited = set()
  
                
                     

        while queue:
            row, col, keys, moves = queue.popleft()
            moves += 1
          
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                curr_keys = keys.copy()
                     
                if inBound(new_row, new_col) and (new_row, new_col) in all_keys and (new_row,new_col, str(curr_keys)) not in visited:
                     
                    cell = grid[new_row][new_col]
                     
                    if cell.isalpha():
                        if cell.isupper() and cell.lower() not in keys:
                            continue
                        elif cell.islower() and cell not in curr_keys:
                            curr_keys.append(cell)
                     
                    if len(curr_keys) == keys_count:
                        return moves
                     
                    queue.append((new_row,new_col, curr_keys, moves))
                    visited.add((new_row,new_col,str(keys)))

        return -1
