class Solution:
    def findLength(self, A, B):
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1]+1
        return max(max(row) for row in dp)
            
        