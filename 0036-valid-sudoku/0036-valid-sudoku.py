class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        columns = defaultdict(set)
        rows = defaultdict(set)
        boxs = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = board[i][j]
                if cur != ".":
                    if (cur in rows[i] or cur in columns[j] or cur in boxs[(i //3,j // 3)]):
                        return False
                rows[i].add(cur)
                columns[j].add(cur)
                boxs[(i //3,j // 3)].add(cur)
        
        return True
                        