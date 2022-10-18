class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        left,right = 0, n
        top,bottom = 0, n
        
        curVal = 1
        
        while curVal <= n**2:
            
            # fill top
            for col in range(left,right):
                matrix[top][col] = curVal
                curVal += 1
                
            top += 1
            
            # fill right side
            for row in range(top, bottom):
                matrix[row][right-1] = curVal
                curVal += 1
                
            right -= 1
            
            # fill bottom side
            for col in range(right-1, left-1, -1):
                matrix[bottom-1][col] = curVal
                curVal += 1
                
            bottom -= 1
            
            # fill left side
            for row in range(bottom-1, top-1, -1):
                matrix[row][left] = curVal
                curVal += 1
                
            left += 1 
            
        return matrix