class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def helper(row,col):
            if (row,col) in dp:
                return dp[(row,col)]
            elif row == 1 or col == 1:
                dp[(row,col)] = 1
                return dp[(row,col)]
            
            dp[(row,col)] = helper(row-1,col)+ helper(row,col-1)
            return dp[(row,col)]
        
        return helper(m,n)
    
    
# class Solution:
#     def uniquePaths(self, m, n):
#         dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
#         print(dp)
        
#         def helper(m, n):
#             if dp[m][n]:
#                 return dp[m][n]
#             elif m == 1 or n == 1:
#                 dp[m][n] = 1
#                 return dp[m][n]
            
#             dp[m][n] = helper(m-1, n) + helper(m, n-1)
#             return dp[m][n]
        
#         return helper(m, n)
        