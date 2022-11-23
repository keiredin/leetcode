class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if (i == j or i == n - 1 - j) and grid[i][j] == 0:
                    return False
                elif (i != j and i != n - 1 - j) and grid[i][j] != 0:
                    return False
        return True
        