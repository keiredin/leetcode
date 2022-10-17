class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            cost1 = dfs(i+1)
            cost2 = dfs(i+2)
            memo[i] = min(cost1,cost2) + cost[i]
            
            return memo[i]
        return min(dfs(0),dfs(1))
            
       
        
        
        