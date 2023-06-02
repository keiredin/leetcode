class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dp(idx, bought):
            if idx >= len(prices):
                return 0
            
            if (idx, bought) in memo:
                return memo[(idx,bought)]
            
            res = 0
            if bought:
                sell = prices[idx]  + dp(idx + 1, 0)
                notSell = dp(idx + 1, bought)
                res =  max(sell,notSell)
            else:
                buy = -prices[idx] + dp(idx+1, 1)
                notBuy = dp(idx+1, bought)
                
                res = max(buy,notBuy)
                
            memo[(idx,bought)] = res
            return memo[(idx,bought)] 
            
        return dp(0,0)
        