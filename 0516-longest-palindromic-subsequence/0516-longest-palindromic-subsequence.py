class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
#         memo = {}
#         def dp(l,r):
#             if (l,r) in memo:
#                 return memo[l,r]
#             if l == r:
#                 return 1
#             if l > r:
#                 return 0
            
#             if s[l] == s[r]:
#                 memo[l,r] = 2 + dp(l+1, r-1)
#             else:
#                 memo[l,r] = max(dp(l+1,r), dp(l,r-1))
#             return memo[l,r]
        
#         return dp(0,len(s)-1)
        
        