class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answ = []
        
        # define boundaries
        left,right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        # edge case is if boundaries met
        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left,right):
                answ.append(matrix[top][i])
            top += 1
            
            # get every i in the right column
            for i in range(top,bottom):
                answ.append(matrix[i][right-1])
            right -= 1
            
            # incase a given matrix is a single colum or a single row
            if not (left < right and top < bottom):
                break
            
            # get every i in the bottom row
            for i in range(right-1, left-1, -1):
                answ.append(matrix[bottom-1][i])
            bottom -= 1
            
            #get every i in the left col
            for i in range(bottom-1, top-1, -1):
                answ.append(matrix[i][left])
            left += 1
                
        return answ
        
        
        
        