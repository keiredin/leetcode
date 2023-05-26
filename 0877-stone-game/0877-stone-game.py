class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = defaultdict(int)
        def aliceIsWinner(i,j):
            if i > j:
                return 0
            if (i,j) in memo:
                return memo[i,j]
            memo[i,j] = max(
                piles[i] - aliceIsWinner(i+1, j),
                piles[j] - aliceIsWinner(i, j-1)
            )
            
            return memo[i,j]
        
        return aliceIsWinner(0,len(piles)-1) >= 0
            
        