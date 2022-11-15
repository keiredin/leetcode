class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board[0])
        m = len(board)
        d = defaultdict()
        dir_arr = [[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
        in_bound = lambda row,col: 0 <= row < m and 0 <= col < n        
        for row in range(m):
            for col in range(n):
                count1 = 0
                for neighbor in dir_arr:
                    newR = row + neighbor[0]
                    newC = col + neighbor[1]
                    
                    if in_bound(newR,newC):
                        if board[newR][newC] == 1:
                            count1 += 1
         
                if board[row][col] == 1:
                    if count1 == 2 or count1 == 3:
                        d[row,col] = 1
                    else:
                        d[row,col] = 0
                        
                else:
                    if count1 == 3:
                        d[row,col] = 1
                    
        for key in d:
            board[key[0]][key[1]] = d[key]
        
        
                
                