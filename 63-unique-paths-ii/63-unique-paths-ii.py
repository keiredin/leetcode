# O(1)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:              
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])        
        
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            obstacleGrid[i][0] = 1 if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1 else 0
        
        for i in range(1,n):
            obstacleGrid[0][i] = 1 if obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1 else 0
            
        
        for row in range(1, m):
            for col in range(1, n):                
                obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1] if obstacleGrid[row][col] == 0 else 0
         
        return obstacleGrid[-1][-1]
    
    
    
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:              
#         m, n = len(obstacleGrid), len(obstacleGrid[0])        
        
#         dp=[[0] * (n+1) for _ in range(m+1)]        
#         dp[0][1]=1
                        
#         for row in range(1, m+1):
#             for col in range(1, n+1):
#                 if not obstacleGrid[row-1][col-1]:
#                     dp[row][col] = dp[row-1][col] + dp[row][col-1]
         
#         return dp[-1][-1]