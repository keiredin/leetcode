class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i):
            if i == len(cost)-1:
                return cost[i]
            if i > len(cost)-1:
                return 0
            
            return cost[i] + min(dfs(i+1),dfs(i+2))
        
        return min(dfs(0),dfs(1))
        
        
        