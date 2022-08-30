# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix[0])
#         for i in range(n // 2 + n % 2):
#             for j in range(n // 2):
#                 tmp = matrix[n - 1 - j][i]
#                 matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
#                 matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
#                 matrix[j][n - 1 - i] = matrix[i][j]
#                 matrix[i][j] = tmp
        
    
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]