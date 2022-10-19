class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        left,right = cStart, cStart + 1
        top,bottom = rStart, rStart + 1
        leftOffset = 0
        
        answ = []
        end = 1
        
        while end <= rows * cols:
            
            # fill top
            for col in range(left + leftOffset, right+1):
                if self.inBound(top,col, rows, cols):
                    answ.append([top,col])
                    end += 1
            left -= 1
            
            # fill right side
            for row in range(top+1, bottom+1):
                if self.inBound(row, right, rows, cols):
                    answ.append([row,right])
                    end += 1
            top -= 1
            # fill bottom side
            for col in range(right-1, left-1, -1):
                if self.inBound(bottom, col, rows, cols):
                    answ.append([bottom,col])
                    end += 1

            right += 1
            
            # fill left side
            for row in range(bottom-1, top-1, -1):
                if self.inBound(row, left,rows, cols):
                    answ.append([row,left])
                    end += 1
                
            bottom += 1 
            
            leftOffset = 1
        return answ
        
    def inBound(self, curR, curC, rows, cols):
        return 0 <= curR < rows and 0 <= curC < cols