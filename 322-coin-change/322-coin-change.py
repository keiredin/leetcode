class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float(inf)] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # means dp[4] = 1 + dp[target-4]
                    
            
        return dp[amount] if dp[amount] != inf else -1
    
    #time = O(amount * len(coins))
    #space = O(amount)
        