from functools import cache
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        M = 10**9 + 7
        @cache
        def prefix(i, j):
            if j == -1: return 0
            return (prefix(i, j-1) + dfs(i,j))%M
        @cache
        def dfs(i, j):
            if j == 0: return 1
            if i == 1: return 0
            return (prefix(i-1,j) - prefix(i-1, max(j-i+1,0)-1))%M
        return dfs(n, k)