class Solution:
    def uniquePathsIII(self, A):
        res = 0
        m, n, emptyCellCount = len(A), len(A[0]), 1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    emptyCellCount += 1

        def backtrack(x, y, emptyCellCount):
            nonlocal res
            if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0): return
            if A[x][y] == 2:
                res += emptyCellCount == 0
                return
            A[x][y] = -2
            backtrack(x + 1, y, emptyCellCount - 1)
            backtrack(x - 1, y, emptyCellCount - 1)
            backtrack(x, y + 1, emptyCellCount - 1)
            backtrack(x, y - 1, emptyCellCount - 1)
            A[x][y] = 0
            
        backtrack(x, y, emptyCellCount)

        return res