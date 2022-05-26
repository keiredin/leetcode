class Solution: 
    # memoization - top down
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def lcs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            elif text1[i] == text2[j]:
                dp[i+1,j+1] = lcs(i+1,j+1)
                return 1 + dp[i+1,j+1]
            else:
                dp[i+1,j] = lcs(i+1,j)
                dp[i,j+1] = lcs(i,j+1)
                return max( dp[i+1,j], dp[i,j+1])
            
        return lcs(0,0)
        