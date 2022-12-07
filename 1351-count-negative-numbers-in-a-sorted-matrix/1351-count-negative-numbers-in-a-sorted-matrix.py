class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
#         row,col = len(grid)-1, 0
#         count = 0
        
#         while row >= 0 and col < len(grid[0]):
#             if grid[row][col] < 0:
#                 count += (len(grid[0])-col)
#                 row -= 1
#             else:
#                 col += 1
#         return count
        
        
        
        count = 0
        for row in grid:
            l,r = 0, len(row)-1
            best = -1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] < 0:
                    best = mid
                    r = mid - 1
                else:
                    l = mid + 1
                    
                    
            count += (len(row) - best) if best >= 0 else 0
            
        return count
                    
                
        