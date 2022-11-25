class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.cols = collections.defaultdict(set)
        self.rows = collections.defaultdict(set)
        self.squares = collections.defaultdict(set)  # key = (r /3, c /3)
        self.tobeVisited = collections.deque([])

        for r in range(9):
            for c in range(9):
                if self.board[r][c] != ".":
                    self.cols[c].add(board[r][c])
                    self.rows[r].add(board[r][c])
                    self.squares[(r // 3, c // 3)].add(board[r][c])
                else:
                    self.tobeVisited.append((r,c))
                

        self.backtrack()
                
    def backtrack(self):
        if not self.tobeVisited:
            return True
        
        r,c = self.tobeVisited[0]
        
        for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            if self.isSafe(r, c, dig):
                self.board[r][c] = dig
                self.rows[r].add(dig)
                self.cols[c].add(dig)
                self.squares[r//3, c//3].add(dig)
                self.tobeVisited.popleft()
                
                if self.backtrack():
                    return True
                else:
                    self.board[r][c] = "."
                    self.rows[r].discard(dig)
                    self.cols[c].discard(dig)
                    self.squares[r//3, c//3].discard(dig)
                    self.tobeVisited.appendleft((r, c))
                    
        return False
                
       

    def isSafe(self,r,c,dig):
        if (
            dig in self.rows[r]
            or dig in self.cols[c]
            or dig in self.squares[(r // 3, c // 3)]
        ):
            return False
        
        return True
    
        