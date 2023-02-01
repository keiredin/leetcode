class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        rowLen = len(mat)
        colLen = len(mat[0])
        
        def prefixSum(arr):
            # vertical prefixsum
            for j in range(colLen):
                for i in range(1, rowLen):
                    arr[i][j] += arr[i - 1][j]

            # horizontal prefixsum
            for i in  range(rowLen):
                for j in range(1, colLen):
                    arr[i][j] += arr[i][j - 1]
                    
        
        # mat if now a prefixSum
        prefixSum(mat)
        answer = [[0]*colLen for _ in range(rowLen)]
        
        for i in range(rowLen):
            for j in range(colLen):
                r1,r2 = max(0,i-k)-1, min(i+k, rowLen-1)
                c1,c2 = max(0, j-k)-1, min(j+k, colLen-1)
                
                
                answer[i][j] = mat[r2][c2]
                if r1 >= 0 and c1 >= 0:
                    answer[i][j] += mat[r1][c1]
                if r1 >= 0:
                    answer[i][j] -= mat[r1][c2]
                if c1 >= 0:
                    answer[i][j] -= mat[r2][c1]
  
        return answer
                
                
                
                