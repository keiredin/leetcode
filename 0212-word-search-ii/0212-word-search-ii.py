class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(x, y, path, hashmap):
            if board[x][y] not in hashmap:
                return
            
            path.append([board[x][y], hashmap[board[x][y]]])
            hashmap = hashmap[board[x][y]]
            # Remove the found word.
            if '#' in hashmap:
                res.append(''.join(ch for ch, _ in path))
                p = '#'
                for ch, node in path[::-1]:
                    if p == '#' or len(node[p]) == 0:
                        del node[p]
                    p = ch
            board[x][y] = '*'
                
            for dx, dy in {(1,0), (-1,0), (0,1), (0,-1)}:
                if 0<=x+dx<m and 0<=y+dy<n and board[x+dx][y+dy]!='*':
                    backtrack(x+dx,y+dy, path, hashmap)
            board[x][y] = path.pop()[0]
        
        m, n = len(board), len(board[-1])
        trie = {}
        res = []
        # Build a trie for words
        for word in words:
            cur = trie
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur['#'] = None
        # Backtrack each position in the board to find all existing words in the trie.
        for i in range(m):
            for j in range(n):
                backtrack(i, j, [], trie)
        return res