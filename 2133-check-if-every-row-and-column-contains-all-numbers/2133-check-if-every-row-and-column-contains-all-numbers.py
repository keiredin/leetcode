class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        row = defaultdict(set)
        col = defaultdict(set)
        for r in range(n):
            for c in range(n):
                if matrix[r][c] in row[r] or matrix[r][c] in col[c]:
                    return False
                row[r].add(matrix[r][c])
                col[c].add(matrix[r][c])
                
        return True
                
        