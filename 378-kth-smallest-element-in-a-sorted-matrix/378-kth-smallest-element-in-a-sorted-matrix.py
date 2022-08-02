class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row,col = 0,0
        min_heap = []
        n = len(matrix)
        while row < n:
            heappush(min_heap, (matrix[row][col],row,col))
            row += 1
            
                     
        while k > 0:
            val,row,col = heappop(min_heap)
            if col < n-1:
                heappush(min_heap, (matrix[row][col+1],row,col+1))
                
            k -= 1
                                       
                         
        return val
                
                     
                     
                     
                     
                     
                     
                     
                     
                     
    
    
    

                
        