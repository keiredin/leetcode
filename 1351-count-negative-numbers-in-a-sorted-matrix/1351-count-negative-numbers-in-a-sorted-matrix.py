class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row,col = len(grid)-1, 0
        count = 0
        
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                count += (len(grid[0])-col)
                row -= 1
            else:
                col += 1
        return count
        
        
        
#         count = 0
#         best = -1
#         for i in grid:
#             l,r = 0, best-1 if best >= 0 else len(i)-1
            
#             while l <= r:
#                 mid = (l + r) // 2
#                 if i[mid] < 0:
#                     best = mid
#                 if i[mid] < 0:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
                    
                    
#             count += (len(i) - best) if best >= 0 else 0
            
#         return count
                    
                
        