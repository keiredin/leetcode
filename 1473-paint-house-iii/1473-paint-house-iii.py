class Solution:
    def minCost(self,houses, cost, m, n, target) -> int:
        memo = {}
        def dfs(i, k, t):
            if t < 0 or t > m-i:
                return float('inf')
            if i == m:
                return 0 if t == 0 else float('inf')
            if (i, k, t) not in memo:
                if houses[i]:
                    memo[i,k,t] = dfs(i+1, houses[i], t-(houses[i]!=k))
                else:
                    memo[i,k,t] = min(cost[i][j-1] + dfs(i+1, j, t-(j!=k)) for j in range(1, n+1))
            return memo[i,k,t]
        ans = dfs(0, 0, target)
        return ans if ans < float('inf') else -1
        
        
        
# class Solution:
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
#         @cache
#         def dp(i, p, h):
#             if (h > target) or (i == m and h != target):
#                 return inf
#             if i == m:
#                 return 0
#             if houses[i] != 0:
#                 return dp(i + 1, houses[i], h + int(p != houses[i]))

#             best = inf
#             for j, c in enumerate(cost[i], 1):
#                 best = min(best, dp(i + 1, j, h + int(p != j)) + c)
#             return best

#         res = dp(0, 0, 0)
#         return res if res != inf else -1