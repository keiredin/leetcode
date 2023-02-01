class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,r = 0,0
        op = 0
        minOp = inf
        while r < len(blocks):
            if blocks[r] == 'W':
                op += 1
            if r-l == k-1:
                minOp = min(minOp,op)
                if blocks[l] == 'W':
                    op -= 1
                l += 1
            r += 1
        return minOp
                
                
        