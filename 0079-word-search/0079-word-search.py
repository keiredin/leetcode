class Solution(object):
    def exist(self, board, word):
        
        def dfs(row, col, i):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            temp = board[row][col]
            board[row][col] = '#'
            res = (dfs(row + 1, col, i + 1) or 
                   dfs(row - 1, col, i + 1) or 
                   dfs(row, col + 1, i + 1) or 
                   dfs(row, col - 1, i + 1))
            
            board[row][col] = temp
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False










# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         dir_arr = [[-1,0],[1,0],[0,-1],[0,1]]
#         inbound = lambda r,c: 0 <= r <len(board) and 0 <= c < len(board[0])
#         visited = set()
        
#         def backtrack(r,c,idx):
#             if idx == len(word):
#                 return True
#             if not inbound(r,c) or board[r][c] != word[idx] or (r,c) in visited:  #board[r][c] == "#"
#                 return False

#             # curChar = board[r][c]
#             # board[r][c] = "#"
#             visited.add((r,c))
            
#             res = False
#             for d in dir_arr:
#                 newR,newC = r + d[0], c + d[1]
#                 res |= backtrack(newR,newC,idx+1)

#             # board[r][c] = curChar
#             visited.remove((r,c))
#             return res
                
#         for row in range(len(board)):
#             for col in range(len(board[0])):
#                 if backtrack(row,col,0):
#                     return True
        
#         return False
        
            
            