class Solution:
    def findMaxForm(self, S: List[str], M: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for str in S:
            zeros = str.count("0")
            ones = len(str) - zeros
            for i in range(M, zeros - 1, -1):
                for j in range(N, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[M][N]
    
    
            
# # Memoization(Top Down)
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         counter=[[s.count("0"), s.count("1")] for s in strs]
        
#         @cache
#         def dp(i,j,idx):
#             if i<0 or j<0:
#                 return -math.inf
            
#             if idx==len(strs):
#                 return 0
            
#             return max(dp(i,j,idx+1), 1 + dp(i-counter[idx][0], j-counter[idx][1], idx+1))
#         return dp(m,n,0)
    
#    #Tabulation(Bottom Up)
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:            
#         dp = [[0] * (n+1) for _ in range(m+1)]
#         counter=[[s.count("0"), s.count("1")] for s in strs]
        
#         for zeroes, ones in counter:
#             for i in range(m, zeroes-1, -1):
#                 for j in range(n, ones-1, -1):                   
#                     dp[i][j] = max(dp[i][j], 1+dp[i-zeroes][j-ones])
        
#         return dp[-1][-1]